import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # WAJIB UNTUK MOBILENETV2
from PIL import Image
from rembg import remove
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Agar bisa diakses dari Frontend Vue.js atau Laravel

# ==============================================================================
# 1. KONFIGURASI MODEL & KELAS
# ==============================================================================
# Pastikan file model .keras hasil training sudah dipindahkan ke folder ini
MODEL_PATH = 'Arsitektur_MobileNetV2.keras' 

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
    print(f"✅ Model {MODEL_PATH} berhasil dimuat.")
else:
    print(f"❌ ERROR: File {MODEL_PATH} tidak ditemukan!")

# Urutan kelas sesuai dengan training di Colab
classes = ['honey', 'natural', 'wash']

# ==============================================================================
# 2. FUNGSI PREPROCESSING (Sesuai Standar MobileNetV2 + Rembg)
# ==============================================================================
def preprocess_robust_mobilenet(input_img):
    # A. Hapus Background (Mengubah objek acak menjadi transparan)
    output_rgba = remove(input_img)
    
    # B. Auto-Crop ke Bounding Box (Menghilangkan sisa ruang kosong)
    bbox = output_rgba.getbbox()
    if bbox:
        output_rgba = output_rgba.crop(bbox)
        
    # C. Center Padding (Membuat kanvas hitam persegi 1:1)
    max_dim = max(output_rgba.size)
    black_bg = Image.new("RGB", (max_dim, max_dim), (0, 0, 0))
    
    # Hitung posisi agar biji kopi tepat di tengah
    paste_x = (max_dim - output_rgba.size[0]) // 2
    paste_y = (max_dim - output_rgba.size[1]) // 2
    
    # Tempelkan gambar menggunakan mask (untuk menjaga transparansi)
    black_bg.paste(output_rgba, (paste_x, paste_y), mask=output_rgba.split()[3])
    
    # D. Resize Standar MobileNetV2 (224x224)
    final_img = black_bg.resize((224, 224))
    
    # E. Konversi ke Array & Normalisasi Khusus MobileNetV2 (-1 hingga 1)
    img_array = img_to_array(final_img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array) # INI KUNCINYA
    
    return img_array

# ==============================================================================
# 3. ENDPOINT API PREDIKSI
# ==============================================================================
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"status": "ERROR", "message": "File gambar tidak ditemukan"}), 400
        
    image_file = request.files['image']
    
    try:
        # Load gambar sebagai RGBA agar rembg bekerja maksimal
        img = Image.open(image_file.stream).convert("RGBA")
        
        # Jalankan Preprocessing
        processed_img = preprocess_robust_mobilenet(img)
        
        # Prediksi menggunakan model
        preds = model.predict(processed_img, verbose=0)[0]
        confidence = float(np.max(preds))
        predicted_class = classes[np.argmax(preds)]
        
        # Hitung Entropy (Mengukur tingkat kebingungan model)
        entropy = -np.sum(preds * np.log(preds + 1e-9))
        
        # Detail Probabilitas untuk ditampilkan di Frontend
        prob_details = {}
        for i, cls_name in enumerate(classes):
            prob_details[cls_name] = round(float(preds[i]) * 100, 2)
            
        # --- LOGIKA PENYARINGAN STATUS ---
        
        # 1. Kasus: Gambar Tidak Jelas (Entropy Terlalu Tinggi)
        if entropy > 0.85:
            return jsonify({
                "status": "DITOLAK",
                "label": "Tidak terdeteksi",
                "confidence": str(round(confidence *  100, 2)),
                "pesan": "Sistem bingung. Pastikan foto hanya berisi satu biji kopi dengan latar belakang yang tidak terlalu ramai.",
                "details": prob_details
            }), 200

        # 2. Kasus: Model Ditolak (Confidence < 70%)
        if confidence < 0.70: 
            return jsonify({
                "status": "DITOLAK",
                "label": "Tidak terdeteksi",
                "confidence": str(round(confidence *  100, 2)), 
                "pesan": f"Sistem ditolak. Tingkat keyakinan hanya {str(round(confidence * 100, 2))}%.",
                "details": prob_details
            }), 200

        # 3. Kasus: Berhasil (Sukses, Confidence >= 70%)
        return jsonify({
            "status": "BERHASIL",
            "label": predicted_class,
            # DIBUNGKUS STRING AGAR .replace() DI VUE.JS TIDAK ERROR
            "confidence": str(round(confidence * 100, 2)), 
            "pesan": f"Biji kopi berhasil diidentifikasi sebagai proses {predicted_class.upper()}.",
            "details": prob_details
        }), 200

    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == '__main__':
    # Jalankan pada port 5001 (sesuaikan dengan settingan Laravel/Vue kamu)
    app.run(host='0.0.0.0', port=5001, debug=False)