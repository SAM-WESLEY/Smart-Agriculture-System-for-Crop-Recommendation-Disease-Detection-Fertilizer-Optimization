from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)

# ── Load Models ────────────────────────────────────────────────────────────────
def load_pkl(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    return None

crop_model       = load_pkl('models/crop_model.pkl')
fertilizer_model = load_pkl('models/fertilizer_model.pkl')

try:
    from tensorflow.keras.models import load_model
    disease_model = load_model('models/disease_model.h5') if os.path.exists('models/disease_model.h5') else None
except Exception:
    disease_model = None

# ── Labels ─────────────────────────────────────────────────────────────────────
CROPS = [
    'Rice','Maize','Chickpea','Kidneybeans','Pigeonpeas','Mothbeans',
    'Mungbean','Blackgram','Lentil','Pomegranate','Banana','Mango',
    'Grapes','Watermelon','Muskmelon','Apple','Orange','Papaya',
    'Coconut','Cotton','Jute','Coffee'
]

FERTILIZERS = [
    'Urea', 'DAP', '14-35-14', '28-28', '17-17-17', '20-20', '10-26-26'
]

DISEASES = [
    'Apple Scab', 'Apple Black Rot', 'Cedar Apple Rust', 'Apple Healthy',
    'Bacterial Spot', 'Early Blight', 'Late Blight', 'Tomato Healthy',
    'Powdery Mildew', 'Leaf Mold', 'Septoria Leaf Spot'
]

DISEASE_TREATMENT = {
    'Apple Scab':          'Apply fungicides containing myclobutanil or captan.',
    'Apple Black Rot':     'Remove infected fruit and apply copper-based fungicide.',
    'Cedar Apple Rust':    'Apply fungicide at bud break. Remove nearby juniper trees.',
    'Early Blight':        'Use chlorothalonil or copper fungicide. Remove infected leaves.',
    'Late Blight':         'Apply mancozeb or metalaxyl fungicide immediately.',
    'Powdery Mildew':      'Apply sulfur-based or potassium bicarbonate fungicide.',
    'Leaf Mold':           'Improve ventilation. Apply copper fungicide.',
    'Septoria Leaf Spot':  'Remove infected leaves. Apply chlorothalonil fungicide.',
    'Bacterial Spot':      'Apply copper-based bactericide. Avoid overhead watering.',
}


# ── Routes ─────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crop')
def crop_page():
    return render_template('crop.html')


@app.route('/fertilizer')
def fertilizer_page():
    return render_template('fertilizer.html')


@app.route('/disease')
def disease_page():
    return render_template('disease.html')


@app.route('/predict/crop', methods=['POST'])
def predict_crop():
    try:
        d = request.json
        features = np.array([[
            float(d['N']), float(d['P']), float(d['K']),
            float(d['temperature']), float(d['humidity']),
            float(d['ph']), float(d['rainfall'])
        ]])
        if crop_model:
            result = str(crop_model.predict(features)[0])
        else:
            # Demo fallback
            idx = int(sum(features[0]) * 7) % len(CROPS)
            result = CROPS[idx]
        return jsonify({'crop': result, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})


@app.route('/predict/fertilizer', methods=['POST'])
def predict_fertilizer():
    try:
        d = request.json
        features = np.array([[
            float(d['temperature']), float(d['humidity']),
            float(d['moisture']),    int(d['soil_type']),
            int(d['crop_type']),     float(d['N']),
            float(d['K']),           float(d['P'])
        ]])
        if fertilizer_model:
            result = str(fertilizer_model.predict(features)[0])
        else:
            idx = int(sum(features[0])) % len(FERTILIZERS)
            result = FERTILIZERS[idx]
        return jsonify({'fertilizer': result, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})


@app.route('/predict/disease', methods=['POST'])
def predict_disease():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded', 'status': 'error'})

        file = request.files['image']
        img_bytes = file.read()

        if disease_model:
            import io
            from PIL import Image
            from tensorflow.keras.preprocessing.image import img_to_array
            img = Image.open(io.BytesIO(img_bytes)).resize((224, 224))
            arr = img_to_array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)
            preds = disease_model.predict(arr)
            idx   = int(np.argmax(preds))
            disease = DISEASES[idx] if idx < len(DISEASES) else 'Unknown'
        else:
            disease = 'Early Blight'  # Demo fallback

        treatment = DISEASE_TREATMENT.get(disease, 'Consult a local agricultural expert.')
        return jsonify({
            'disease':   disease,
            'treatment': treatment,
            'status':    'success'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
