# Smart Agriculture System for Crop Recommendation, Disease Detection & Fertilizer Optimization

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

> A Machine Learning powered smart agriculture system that helps farmers make data-driven decisions — recommending the best crops, optimal fertilizers, and detecting plant diseases through a user-friendly web interface.

---

## 📌 Overview

This project uses Machine Learning to help farmers make better decisions by recommending:

- ✅ Suitable crops based on soil and climate conditions
- ✅ Required fertilizers based on nutrient deficiencies
- ✅ Detecting plant diseases from leaf images

---

## 🚀 Features

- 🌾 **Crop Prediction** using Random Forest — recommends the best crop based on N, P, K, temperature, humidity, pH, and rainfall
- 🧪 **Fertilizer Recommendation System** — suggests the right fertilizer based on soil nutrient levels and crop type
- 🦠 **Disease Detection using CNN** — identifies plant diseases from leaf images using a Convolutional Neural Network
- 🌐 **User-friendly Web Interface** — simple, clean Flask web app accessible from any browser

---

## 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Language | Python |
| Web Framework | Flask |
| Crop & Fertilizer ML | Scikit-learn (Random Forest) |
| Disease Detection | TensorFlow / Keras (CNN) |
| Frontend | HTML / CSS |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |

---

## 📁 Project Structure

```
Smart-Agriculture-System/
├── app.py                        # Main Flask application
├── crop_recommendation.py        # Crop prediction model
├── fertilizer_recommendation.py  # Fertilizer recommendation model
├── disease_detection.py          # CNN disease detection model
├── models/
│   ├── crop_model.pkl            # Trained Random Forest (crop)
│   ├── fertilizer_model.pkl      # Trained Random Forest (fertilizer)
│   └── disease_model.h5          # Trained CNN model
├── templates/
│   ├── index.html                # Home page
│   ├── crop.html                 # Crop recommendation page
│   ├── fertilizer.html           # Fertilizer recommendation page
│   └── disease.html              # Disease detection page
├── static/
│   └── style.css                 # Stylesheet
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/SAM-WESLEY/Smart-Agriculture-System
cd Smart-Agriculture-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## 📊 Input Parameters

### Crop Recommendation
| Parameter | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Ambient temperature (°C) |
| Humidity | Relative humidity (%) |
| pH | Soil pH value |
| Rainfall | Annual rainfall (mm) |

### Fertilizer Recommendation
| Parameter | Description |
|---|---|
| Soil Type | Sandy / Loamy / Black / Red / Clayey |
| Crop Type | Rice / Wheat / Maize / etc. |
| N, P, K | Current soil nutrient levels |
| Moisture | Soil moisture content (%) |

### Disease Detection
- Upload a **leaf image** (JPG/PNG)
- CNN model classifies it into the disease category
- Returns disease name + treatment recommendation

---

## 🌾 Supported Crops

Rice, Maize, Chickpea, Kidneybeans, Pigeonpeas, Mothbeans, Mungbean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

---

## 🦠 Detectable Diseases

Apple Scab, Black Rot, Cedar Apple Rust, Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Powdery Mildew, and more — trained on PlantVillage dataset.

---

## 📬 Contact

**Sam Wesley S**
📧 samwesley@karunya.edu.in
🔗 [LinkedIn](https://linkedin.com/in/samwesleys)
🐙 [GitHub](https://github.com/SAM-WESLEY)

---

<p align="center">
  <i>Built with ❤️ at Karunya Institute of Technology and Sciences</i>
</p>

<p align="center">If this project helped you, please give it a ⭐</p>
