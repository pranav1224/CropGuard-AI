# 🚀 CropGuard AI - Complete Deployment & Operations Manual

This guide walks you through putting **CropGuard AI** into working condition immediately on your local machine and deploying it to the cloud for public access across web and mobile.

---

## ⚡ Option 1: Instant Local Execution (Working Condition Right Now)

Your local machine already has all necessary dependencies installed (`streamlit`, `opencv`, `numpy`, `scipy`, `pandas`, `pillow`, `reportlab`, `matplotlib`, `node`, `npm`).

### Method A: Interactive Master Launcher (Recommended)
Double-click [`launch_cropguard.bat`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/launch_cropguard.bat) in the project folder. You will be greeted with an interactive menu:
```text
  [1] Launch 3D Streamlit AI Platform (Port 8501)  [RECOMMENDED]
  [2] Launch Full-Stack Express & React App (Port 5000)
  [3] Open Instant Standalone Dashboard (index.html)
  [4] Launch Full Multi-Service Stack (Ports 8501 + 5000)
```
Press **`1`** to launch the 3D Streamlit AI platform, or **`2`** to launch the React + Express app.

---

### Method B: Command Line (PowerShell or Terminal)

#### 1. Streamlit 3D AI Platform
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\cropguard
streamlit run app.py
```
👉 Open your browser to: **`http://localhost:8501`**

#### 2. Express Backend & Compiled React App
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\cropguard\backend
node server.js
```
👉 Open your browser to: **`http://localhost:5000`**

#### 3. Standalone Offline Dashboard
Simply double-click [`index.html`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/index.html) or run [`launch_in_browser.bat`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/launch_in_browser.bat) to launch in your browser with zero server prerequisites.

---

## 📱 Option 2: Mobile / Farm LAN Deployment (Access via Phone or Tablet)

You can run CropGuard on your laptop or farm workstation and allow anyone on the same Wi-Fi network (or mobile hotspot) to scan crops and view predictions directly on their smartphones:

1. Open PowerShell and find your local IP address:
   ```powershell
   ipconfig
   ```
   *(Look for `IPv4 Address`, e.g., `192.168.1.45`)*

2. Start Streamlit bound to all network interfaces:
   ```powershell
   cd C:\Users\hp\.gemini\antigravity\scratch\cropguard
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

3. On any phone, tablet, or field laptop connected to the same Wi-Fi, open:
   ```text
   http://192.168.1.45:8501
   ```
   *(Replace with your actual IPv4 address)*

---

## ☁️ Option 3: Free Cloud Deployment (Streamlit Community Cloud)

**Streamlit Community Cloud** is the easiest, 100% free hosting platform for Streamlit applications with free automatic HTTPS/SSL certificates.

### Step-by-Step Instructions:

1. **Initialize Git & Push to GitHub**:
   Open PowerShell in the `cropguard` folder:
   ```powershell
   cd C:\Users\hp\.gemini\antigravity\scratch\cropguard
   git init
   git add .
   git commit -m "Initial CropGuard AI release"
   ```
   Create a new public or private repository on [GitHub](https://github.com/new) named `cropguard`, then link and push:
   ```powershell
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/cropguard.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and click **Sign In with GitHub**.
   - Click **Create App** (or **New app**).
   - Select your repository: `<YOUR_GITHUB_USERNAME>/cropguard`.
   - Branch: `main`.
   - Main file path: `app.py`.
   - Click **Deploy!**

3. **Live in 2 minutes**:
   Streamlit Cloud automatically installs `requirements.txt` and Debian dependencies in `packages.txt`. You will get a permanent public URL (e.g. `https://cropguard.streamlit.app`).

---

## 🤗 Option 4: Free Deployment on Hugging Face Spaces

Hugging Face provides free persistent hosting for machine learning and AI applications:

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and click **Create new Space**.
2. Name your space (e.g. `cropguard-ai`).
3. Select **Streamlit** as the Space SDK.
4. License: Apache 2.0 or MIT.
5. Space hardware: **Free (CPU basic - 2 vCPU, 16GB RAM)**.
6. Push your files using Git or upload directly via the web interface:
   ```bash
   git remote add space https://huggingface.co/spaces/<YOUR_USERNAME>/cropguard-ai
   git push space main
   ```
7. Hugging Face builds and deploys your space automatically with a permanent public link.

---

## 🐳 Option 5: Containerized Docker Deployment (Render, Railway, AWS, GCP)

The repository includes a ready-to-deploy [`Dockerfile`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/Dockerfile) and [`docker-compose.yml`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/docker-compose.yml).

### Local Docker Run:
```bash
docker compose up --build
```
Open **`http://localhost:8501`**.

### Render.com Free Cloud Hosting:
1. Push code to GitHub.
2. Sign in to [Render.com](https://render.com).
3. Click **New +** -> **Web Service**.
4. Connect your `cropguard` GitHub repository.
5. Select **Docker** environment.
6. Click **Create Web Service**. Render builds the Docker container and assigns a live HTTPS URL (e.g., `https://cropguard.onrender.com`).

---

## ⚙️ Configuration & Environment Variables

| Variable | Default | Purpose |
| :--- | :--- | :--- |
| `STREAMLIT_SERVER_PORT` | `8501` | Application port |
| `STREAMLIT_SERVER_ADDRESS` | `0.0.0.0` | Network binding interface |
| `GEMINI_API_KEY` | *(Optional)* | Google Gemini API key for multimodal second-opinion diagnosis |
| `PORT` (Node Backend) | `5000` | Express REST API gateway port |
| `MONGO_URI` | `mongodb://127.0.0.1:27017/cropguard_db` | MongoDB connection URI for history logging |

---

## 🧪 Verification Checklist

- [x] Python core engine verified with [`test_pipeline.py`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/test_pipeline.py).
- [x] 3D WebGL topography and elevation mesh verified with [`test_3d.py`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/test_3d.py).
- [x] React production bundle compiled into `frontend/dist`.
- [x] Express backend configured to serve the React frontend on port 5000.
- [x] `requirements.txt` and `packages.txt` verified for cloud hosting.
- [x] `Dockerfile` and `docker-compose.yml` configured for container deployment.
- [x] Interactive launcher [`launch_cropguard.bat`](file:///C:/Users/hp/.gemini/antigravity/scratch/cropguard/launch_cropguard.bat) verified.
