import os
import numpy as np
import joblib
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
from rembg import remove
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ==============================================================================
# 1. LOAD SEMUA MODEL (KLASIFIKATOR + SATPAM 1 & 2)
# ==============================================================================
MODEL_CNN_PATH = 'Arsitektur_MobileNetV2.keras'
MODEL_CAE_PATH = 'satpam_kopi_cae.keras'
SATPAM_IF_PATH = 'Satpam_IsolationForest.pkl'

print("⏳ Memuat seluruh infrastruktur model...")
full_model = load_model(MODEL_CNN_PATH, compile=False)
satpam_cae = load_model(MODEL_CAE_PATH, compile=False)
iso_forest = joblib.load(SATPAM_IF_PATH)

# Buat Feature Extractor untuk Satpam IF
feature_extractor = Sequential([
    full_model.layers[0],
    full_model.layers[1]
])
feature_extractor.build((None, 224, 224, 3))

classes = ['honey', 'natural', 'wash']
THRESHOLD_GOSONG = 51   
THRESHOLD_MSE = 0.0021  

print("✅ Sistem Keamanan Berlapis Berhasil Diaktifkan.")

# ==============================================================================
# 2. PIPELINE PENYARINGAN BERLAPIS
# ==============================================================================
def proses_gambar_strict(input_img):
    # A. Rembg & Crop
    output_rgba = remove(input_img)
    bbox = output_rgba.getbbox()
    if bbox: output_rgba = output_rgba.crop(bbox)
        
    # --------------------------------------------------------------------------
    # LAPIS 1: Filter Kecerahan
    # --------------------------------------------------------------------------
    img_rgba_np = np.array(output_rgba)
    mask_biji = img_rgba_np[:, :, 3] > 0
    kecerahan = np.median(img_rgba_np[mask_biji][:, :3]) if np.any(mask_biji) else 0
    if kecerahan < THRESHOLD_GOSONG:
        return None, "DITOLAK_GELAP", f"Kecerahan terlalu rendah ({kecerahan:.1f})"

    # Siapkan Kanvas Hitam Dasar
    max_dim = max(output_rgba.size)
    black_bg = Image.new("RGB", (max_dim, max_dim), (0, 0, 0))
    black_bg.paste(output_rgba, ((max_dim - output_rgba.size[0]) // 2, (max_dim - output_rgba.size[1]) // 2), mask=output_rgba.split()[3])

    # --------------------------------------------------------------------------
    # LAPIS 2: Satpam Bentuk (CAE 64x64) - Menyaring Geometri Kasar
    # --------------------------------------------------------------------------
    img_cae = black_bg.resize((64, 64))
    img_arr_cae = img_to_array(img_cae) / 255.0
    img_arr_cae = np.expand_dims(img_arr_cae, axis=0)
    
    rekonstruksi = satpam_cae.predict(img_arr_cae, verbose=0)
    mse_score = np.mean(np.square(img_arr_cae - rekonstruksi))
    if mse_score > THRESHOLD_MSE:
        return None, "DITOLAK_CAE", f"Struktur bentuk tidak sesuai standar (MSE: {mse_score:.5f})"

    # --------------------------------------------------------------------------
    # LAPIS 3: Satpam Semantik (Isolation Forest 224x224) - Menyaring Detail Fitur
    # --------------------------------------------------------------------------
    final_img = black_bg.resize((224, 224))
    img_array = img_to_array(final_img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    fitur = feature_extractor.predict(img_array, verbose=0)
    keputusan_if = iso_forest.predict(fitur)[0]
    if keputusan_if == -1:
        return None, "DITOLAK_IF", "Karakteristik objek bukan green bean kopi"

    return img_array, "LOLOS", "Semua pos pemeriksaan aman"

# ==============================================================================
# 3. ENDPOINT API
# ==============================================================================
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"status": "ERROR", "message": "File tidak ditemukan"}), 400
        
    try:
        img = Image.open(request.files['image'].stream).convert("RGBA")
        processed_img, status_satpam, keterangan = proses_gambar_strict(img)
        
        # Jika salah satu satpam menolak, langsung return kembalian status DITOLAK
        if status_satpam != "LOLOS":
            return jsonify({
                "status": "DITOLAK", 
                "label": "Tidak terdeteksi", 
                "pesan": f"Objek ditolak pada tahap {status_satpam.split('_')[1]}. Keterangan: {keterangan}."
            }), 200
            
        # Jika lolos semua satpam, panggil pakar klasifikasi utama
        preds = full_model.predict(processed_img, verbose=0)[0]
        confidence = float(np.max(preds))
        predicted_class = classes[np.argmax(preds)]
        entropy = -np.sum(preds * np.log(preds + 1e-9))
        
        if entropy > 0.85 or confidence < 0.70:
            return jsonify({"status": "DITOLAK", "label": "Tidak terdeteksi", "pesan": "Sistem ragu dengan objek ini."}), 200

        return jsonify({
            "status": "BERHASIL",
            "label": predicted_class,
            "confidence": str(round(confidence * 100, 2)),
            "pesan": f"Biji kopi proses {predicted_class.upper()} terdeteksi.",
            "details": {cls: round(float(p) * 100, 2) for cls, p in zip(classes, preds)}
        }), 200

    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)