<div align="center">

# 🌿🍌 AgroScan AI
### 🔬 Multimodal Crop Pathology, Deterministic Lesion Quantification & Yield Risk Engine

*Built for **Banana Hacks 2026** 🏆 • Core Thematic Spotlight: **Banana Black Sigatoka*** 🍌⚡

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-FBE8A6?style=flat)](LICENSE)

🎥 [Demo Video (YouTube)](#-demo-video) • 🏗️ [Architecture](#-system-architecture) • ⚡ [Key Features](#-key-capabilities) • 🚀 [Quickstart](#-installation--local-deployment) • 📊 [Test Cases](#-pre-configured-test-cases)

---

</div>

## 📌 Executive Summary 🌍💡

Over **30% of global crop yields are lost every year** 🌾 to foliar plant pathogens such as *Pseudocercospora fijiensis* (Banana Black Sigatoka) 🍌 and *Phytophthora infestans* (Late Blight) 🥔🍅. 

Most mobile agriculture apps act as superficial black-box classification wrappers: they return a single text label without explaining:
- 📉 How widespread the necrosis is,
- 💰 How much harvest yield is in danger,
- 🧪 Or the exact pesticide volume required without poisoning soil runoff.

**AgroScan AI** converts raw visual pixels into measurable agronomic intelligence 🚜. By combining botanical foliage verification with **deterministic HSV color-space pixel thresholding**, it:
1. 📐 Calculates exact foliar lesion surface damage (%),
2. ⛅ Queries real-time microclimate conditions via the **Open-Meteo REST API**,
3. 💵 Estimates direct financial risk ($/acre),
4. 🗣️ Delivers multi-tiered agronomic action plans in English and localized Urdu with native voice synthesis!

---

## 🏗️ System Architecture 🔄

```text
                                  📸 User Leaf Image (Upload / Preset)
                                                 │
                                                 ▼
                               ┌───────────────────────────────────┐
                               │   🌿 Botanical Leaf Validator     │
                               │  (HSV Green-Yellow Spectrum Check)│
                               └─────────────────┬─────────────────┘
                                                 │
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                 ▼
        ┌───────────────────────────────┐                 ┌───────────────────────────────┐
        │ 🔬 Deterministic Lesion Engine│                 │   ⛅ Live Microclimate Engine │
        │ • HSV Necrotic Tissue Filter  │                 │ • Open-Meteo Geocoding REST   │
        │ • Morphological Ellipse Clean │                 │ • Ambient Temperature (°C)   │
        │ • Mask: Damaged vs Healthy    │                 │ • Relative Humidity (%)       │
        └───────────────┬───────────────┘                 └───────────────┬───────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 ▼
                               ┌───────────────────────────────────┐
                               │     📊 Quantitative Diagnostics   │
                               │  Severity % = (Lesion / Foliage)  │
                               │  Pathology Classification Logic   │
                               └─────────────────┬─────────────────┘
                                                 │
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                 ▼
        ┌───────────────────────────────┐                 ┌───────────────────────────────┐
        │   💵 Economic Loss Modeler    │                 │ 📋 Agronomic Clinical Advisory│
        │ • Projected Yield Deficit %   │                 │ • 1. 🧪 Chemical Protocol     │
        │ • Direct Risk ($ / acre)      │                 │ • 2. 🌾 Cultural Sanitation   │
        │ • 5-Day Untreated Exposure    │                 │ • 3. 🛡️ Preventative Action   │
        └───────────────┬───────────────┘                 └───────────────┬───────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 ▼
                               ┌───────────────────────────────────┐
                               │   💻 Interactive Responsive UI    │
                               │ • 🌐 Dual English & Urdu RTL Mode │
                               │ • 🔊 Native Web Speech TTS Audio  │
                               │ • 📄 Instant PDF Clinical Report  │
                               │ • 🤖 AI Agronomist Co-Pilot Q&A   │
                               └───────────────────────────────────┘





---

## ⚡ Key Capabilities 🌟

### 1. 🔬 Dual-Branch Computer Vision & Real Quantification

* **🌿 Vegetation Filtering:** Automatically filters out non-plant images (faces, buildings, inanimate items) by checking chlorophyll presence ($>5\%$).
* **📐 Mathematical Severity Index:** Computes exact damage:

$$\text{Severity Index (\%)} = \left(\frac{\text{Lesion Pixel Count}}{\text{Leaf Lamina Pixel Count}}\right) \times 100$$


* **🎨 Multi-Layer Diagnostic Overlay:** Displays high-contrast yellow contour vectors around lesion margins and bright red highlights over active necrotic tissue.

### 2. ⛅ Live Microclimate Synchronization (Open-Meteo API)

* 📡 Queries live ambient weather worldwide without API keys.
* ⚠️ Automatically flags high humidity ($>70\%$ RH) to alert farmers about accelerated fungal sporulation risk.

### 3. 💵 Economic Risk & Yield Deficit Modeling

* 📊 Translates infection percentage into real-world business impact:
* 📉 Estimated yield deficit percentage.
* 💰 Direct financial exposure ($/acre) if left untreated for 5 days.



### 4. 🍌 Banana Hacks Thematic Alignment (*Banana: Black Sigatoka*)

* 🎯 Dedicated clinical detection pipeline for *Pseudocercospora fijiensis* (Black Sigatoka), featuring tailored systemic triazole formulations and leaf-stripping sanitation rules.

### 5. 🌐 Inclusive Localization & Native Accessibility

* **🇵🇰 100% RTL Urdu Support:** Full right-to-left UI designed specifically for rural farmers.
* **🔊 Audio Prescriptions:** Browser-level Web Speech Synthesis API vocalizes treatment steps out loud in localized speech.
* **📄 One-Click Field Export:** Instant print-to-PDF diagnostic card for field documentation.

---

## 🔬 Computer Vision & Agronomic Methodology 🧪

```text
🌿 HSV Leaf Bounds:     Lower [18,  25,  25]  ──►  Upper [88, 255, 255]
🍂 HSV Lesion Bounds:   Lower [ 8,  50,  20]  ──►  Upper [28, 255, 200]

```

1. **🎨 Color-Space Conversion:** Converts RGB to HSV (Hue, Saturation, Value) to separate color chrominance from outdoor shadows and sunlight glare.
2. **🧼 Lamina Cleaning:** Applies morphological closing operations to eliminate specular reflection holes.
3. **🎯 Lesion Extraction:** Isolates necrotic brown/black tissue strictly inside the leaf mask using bitwise operations.
4. **📏 Distance & Scale Detection:** Warns the user if the leaf occupies $<15\%$ of the camera frame, requesting a close-up photo.

---

## 📂 Project Repository Structure 📁

```text
agroscan-ai/
│
├── 🚀 app.py              # Primary Streamlit dashboard, state manager & UI
├── 🔬 severity.py         # OpenCV HSV segmentation, leaf verification & overlays
├── 📚 disease_data.py     # Pathology database, 3-pillar prescriptions & Q&A
├── 📦 requirements.txt    # Pinned runtime dependencies
├── 🙈 .gitignore          # Ignored system & cache binaries
└── 📖 README.md           # Technical project documentation

```

---

## 💻 Installation & Local Deployment 🚀

### 📋 Prerequisites

* 🐍 Python 3.10, 3.11, or 3.12
* 🐙 Git

### ⚙️ Step-by-Step Setup

```bash
# 1. Clone repository 📥
git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/agroscan-ai.git
cd agroscan-ai

# 2. Create virtual environment 🛠️
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies 📦
pip install -r requirements.txt

# 4. Launch AgroScan AI 🌟
python -m streamlit run app.py

```

🌐 Open your browser at `http://localhost:8501`.

---

## 🧪 Pre-Configured Test Cases 🔍

Use the **Quick Test Cases** radio menu for instant live demonstration:

| 🧪 Test Case | 🔬 Primary Pathology | 📊 Severity Profile | 💊 Recommended Clinical Action |
| --- | --- | --- | --- |
| **🍌 Banana: Black Sigatoka** | *Pseudocercospora fijiensis* | ~13.6% (Moderate) 🟡 | Azoxystrobin + Mineral Oil; De-leafing infected fronds ✂️ |
| **🍅 Tomato: Late Blight** | *Phytophthora infestans* | >30.0% (Critical) 🔴 | Cymoxanil + Mancozeb; Immediate isolation 🚨 |
| **🥔 Potato: Early Blight** | *Alternaria solani* | ~8.4% (Mild) 🟢 | Mancozeb protectant; Balanced nitrogen management 🌿 |
| **🌱 Healthy Leaf** | None (Intact Lamina) | 0.0% (Nominal) 🟢 | Routine fertigation; Bi-weekly field scouting 🔍 |

---

## 🗺️ Future Roadmap 🔮

* [ ] 📱 **Offline Edge Deployment:** Quantize segmentation pipelines to run on edge hardware (Raspberry Pi 5 + Coral TPU) for remote offline fields.
* [ ] 🛸 **Drone Fleet Dispatch:** Emit GeoJSON coordinates to autonomous crop-dusting drones.
* [ ] 🧠 **DeepLabV3+ Integration:** Train multi-spectral vision checkpoints for drone aerial imaging.

---

## 📄 License 📜

Distributed under the **MIT License**. See `LICENSE` for details.

---
