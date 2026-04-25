import os
import io
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)

# 1. SETUP PATH MODEL
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model_efficientNet.keras')

# 2. DUMMY PREPROCESS (Agar tidak error saat load Lambda layer)
def preprocess_input(x):
    return x

print("⏳ Sedang memuat 'Otak AI'...")

try:
    # Menggunakan parameter Keras 3 untuk memuat model lama
    model = tf.keras.models.load_model(
        MODEL_PATH,
        custom_objects={'preprocess_input': preprocess_input},
        compile=False,
        safe_mode=False  # Kunci agar Keras 3 mau menerima config Keras lama
    )
    print("✅ BERHASIL: Model AI siap digunakan!")
except Exception as e:
    print(f"❌ GAGAL: {str(e)}")
    print("--- SOLUSI ---")
    print("Jika error 'Unrecognized keyword arguments', silakan info ke saya.")

# Label klasifikasi kopi kamu
labels = ['Honey', 'Natural', 'Washed']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        
        # 1. Load Gambar & Resize ke 224x224
        img = Image.open(file.stream).convert('RGB')
        img = img.resize((224, 224))
        
        # 2. Konversi ke Array
        img_array = np.array(img).astype('float32')
        
        # 3. JURUS SAKTI: Gunakan preprocessing asli EfficientNet
        # Ini akan menangani scaling warna agar sama persis dengan saat training
        img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)

        # 4. Prediksi
        preds = model.predict(img_array, verbose=0)
        class_idx = np.argmax(preds[0])
        confidence = float(np.max(preds[0]))
        
        print(f"📥 Prediksi: {labels[class_idx]} ({confidence*100:.2f}%)")

        return jsonify({
            'label': labels[class_idx],
            'confidence': f"{confidence * 100:.2f}%",
            'status': 'success'
        })
    except Exception as e:
        print(f"❌ ERROR PREDIKSI: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Jalankan di port 5001 agar tidak diblokir Windows AirPlay
    app.run(host='127.0.0.1', port=5001, debug=True)