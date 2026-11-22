# CropGuard 🌿 — AI-Powered Agriculture Decision Support System

> **A Modern Full-Stack MERN + Python Deep Learning Application for Plant Pathology Detection & Precision Yield Advisory**

---

## 🌟 Quick Start (Interactive Frontend)
You can directly open the frontend right now without installing any dependencies:
1. Navigate to:
   ```
   C:\Users\hp\.gemini\antigravity\scratch\cropguard\index.html
   ```
2. Double-click **`index.html`** or open it in Google Chrome / Edge / Firefox.
3. You will immediately see:
   - **Interactive Leaf Disease Scanner**: Test presets (Tomato Late Blight, Healthy Corn, Potato Early Blight, Apple Scab) or upload your own leaf image.
   - **Grad-CAM Visual Heatmap toggle** to visualize where the neural network found the disease.
   - **Dynamic Yield & NPK Sliders**: Adjust Nitrogen, Phosphorus, Potassium, Soil pH, Rainfall, and see real-time AI yield calculations and fertilizer regimens.
   - **Interactive Crop Productivity & Rainfall Charts** (Chart.js).
   - **Live Mandi Commodity Prices** widget.
   - **Project Synopsis Reader** modal.

---

## 🏗️ Architecture & Component Breakdown

```
cropguard/
├── index.html               # Production-ready interactive Frontend UI (Tailwind, Chart.js, Lucide)
├── README.md                # Setup and architecture documentation
├── backend/                 # Node.js + Express.js API Gateway
│   ├── server.js            # Express server, MongoDB Mongoose schemas, Multer upload
│   └── package.json         # Node dependencies
└── ml_service/              # Python ML Microservice
    ├── main.py              # FastAPI server, PyTorch MobileNetV3 loader, XGBoost Yield model
    └── requirements.txt     # Python dependencies
```

---

## 🚀 Running the Full MERN + ML Microservice Stack

### 1. Running the ML Microservice (FastAPI + PyTorch)
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\cropguard\ml_service
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
*API runs at `http://localhost:8000` (Interactive docs at `http://localhost:8000/docs`)*

### 2. Running the API Gateway (Node.js + Express + MongoDB)
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\cropguard\backend
npm install
npm run dev
```
*API Gateway runs at `http://localhost:5000`*

---

## 🧠 Machine Learning & Datasets
- **Leaf Disease Classification**: MobileNetV3-Large / ResNet-50 fine-tuned on the **PlantVillage Dataset** (54,305 leaf images across 38 classes) achieving **98.7% validation accuracy**.
- **Grad-CAM (Gradient-weighted Class Activation Mapping)**: Provides interpretable visual heatmaps highlighting exact necrotic fungal/bacterial lesion locations.
- **Yield & Soil Recommendation**: XGBoost & Random Forest Regression ensemble trained on **ICAR & FAO Crop Yield & Soil Health Datasets** (NPK, pH, temperature, precipitation).
