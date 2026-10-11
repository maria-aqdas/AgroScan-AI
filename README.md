<div align="center">

# 🌿 AgroScan AI
### Multimodal Crop Pathology, Deterministic Lesion Quantification & Yield Risk Engine

*Submitted to **Banana Hacks 2026** • Core Thematic Case: **Banana Black Sigatoka***

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-FBE8A6?style=flat)](LICENSE)

[Demo Video (YouTube)](#-demo-video) • [System Architecture](#-system-architecture) • [Key Capabilities](#-key-capabilities) • [Local Setup](#-installation--local-deployment) • [Agronomic Methodology](#-agronomic-and-computer-vision-methodology)

---

</div>

## 📌 Executive Summary

Over **30% of global crop yields are lost annually** to foliar plant pathogens such as *Pseudocercospora fijiensis* (Banana Black Sigatoka) and *Phytophthora infestans* (Late Blight). 

Most commodity agricultural AI applications function as superficial black-box classification wrappers: they return a single textual class label without contextualizing how widespread the necrosis is, how much harvest tonnage is endangered, or what exact fungicide dilution is required. This forces growers into blind, excessive chemical applications that poison groundwater, accelerate antifungal resistance, and drain capital.

**AgroScan AI** bridges computer vision and real-world farm decision-making. By pairing botanical foliage validation with **deterministic HSV color-space pixel thresholding**, the platform computes mathematical foliar lesion severity percentages, integrates real-time ambient microclimate data via the **Open-Meteo REST API**, forecasts financial exposure per acre, and serves multi-tiered agronomic action plans in both English and localized Urdu with native voice assistance.

---


## 🏗️ System Architecture

```text
                                  User Leaf Image (Upload / Preset)
                                                 │
                                                 ▼
                               ┌───────────────────────────────────┐
                               │     Botanical Leaf Validator      │
                               │  (HSV Green-Yellow Spectrum Check)│
                               └─────────────────┬─────────────────┘
                                                 │
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                 ▼
        ┌───────────────────────────────┐                 ┌───────────────────────────────┐
        │  Deterministic Lesion Engine  │                 │    Live Microclimate Engine   │
        │ • HSV Necrotic Tissue Filter  │                 │ • Open-Meteo Geocoding REST   │
        │ • Morphological Ellipse Clean │                 │ • Ambient Temperature (°C)   │
        │ • Mask: Damaged vs Total Foli │                 │ • Relative Humidity (%)       │
        └───────────────┬───────────────┘                 └───────────────┬───────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 ▼
                               ┌───────────────────────────────────┐
                               │      Quantitative Diagnostics     │
                               │  Severity % = (Lesion / Foliage)  │
                               │  Pathology Classification Logic   │
                               └─────────────────┬─────────────────┘
                                                 │
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                 ▼
        ┌───────────────────────────────┐                 ┌───────────────────────────────┐
        │    Economic Loss Modeler      │                 │  Agronomic Clinical Advisory  │
        │ • Projected Yield Deficit %   │                 │ • 1. Chemical Control Protocol│
        │ • Direct Risk ($ / acre)      │                 │ • 2. Cultural Sanitation      │
        │ • 5-Day Untreated Exposure    │                 │ • 3. Preventative Scouting    │
        └───────────────┬───────────────┘                 └───────────────┬───────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 ▼
                               ┌───────────────────────────────────┐
                               │   Interactive Responsive UI       │
                               │ • Dual English & Urdu (RTL) Modes │
                               │ • Native Web Speech TTS Audio     │
                               │ • Instant PDF Clinical Field Card │
                               │ • AI Agronomist Co-Pilot Q&A      │
                               └───────────────────────────────────┘

```

---

## 🎯 Key Capabilities

### 1. Dual-Branch Computer Vision & Real Quantification

* **Vegetation Filtering:** Automatically rejects out-of-distribution inputs (faces, buildings, inanimate items) by enforcing minimum plant chlorophyll chromatic presence ($>5\%$).
* **Mathematical Severity Index:** Computes:

$$\text{Severity Index (\%)} = \left(\frac{\text{Lesion Pixel Count}}{\text{Leaf Lamina Pixel Count}}\right) \times 100$$


* **Multi-Layer Diagnostic Overlay:** Renders high-contrast yellow contour vectors around lesion margins and bright red warning tints over active necrotic tissue.

### 2. Live Microclimate Synchronicity (Open-Meteo API)

* Queries live global weather without API keys.
* Flags high-humidity scenarios ($>70\%$ relative humidity), which trigger sporulation risk heuristics and alter fungicide spray windows.

### 3. Economic Exposure & Yield Deficit Modeling

* Connects pathological severity to financial risk metrics ($/acre and percentage yield loss over an untreated 5-day cycle), enabling farm supervisors to justify treatment ROI.

### 4. Banana Hacks Thematic Alignment (*Banana: Black Sigatoka*)

* Features specialized handling for *Pseudocercospora fijiensis* (Black Sigatoka), the primary threat to global banana cultivation, featuring systemic triazole formulations and leaf-stripping sanitation rules.

### 5. Inclusive Localization & Native Accessibility

* **100% RTL Urdu Support:** Full right-to-left layout featuring native typography for underserved growers.
* **Hands-Free Audio Guidance:** Browser-level Web Speech Synthesis API vocalizes treatment steps in local dialects.
* **One-Click Diagnostic Export:** Formatted printable summary ready for agricultural extension workers.

---

## 🔬 Agronomic and Computer Vision Methodology

```text
HSV Leaf Bounds:     Lower [18,  25,  25]  ──►  Upper [88, 255, 255]
HSV Lesion Bounds:   Lower [ 8,  50,  20]  ──►  Upper [28, 255, 200]

```

1. **Color-Space Conversion:** The RGB image is converted to HSV (Hue, Saturation, Value) to separate color chrominance from uneven outdoor lighting and shadows.
2. **Lamina Segmentation:** Morphological closing operations clean specular reflection voids across the leaf blade.
3. **Lesion Extraction:** Necrotic tissue filters run strictly within the segmented leaf mask via bitwise conjunction, preventing non-foliar background artifacts from skewing pathology metrics.
4. **Distance & Scale Detection:** Identifies when a leaf occupies $<15\%$ of total frame pixels and issues an alert prompting close-up inspection.

---

## 📂 Project Repository Structure

```text
agroscan-ai/
│
├── app.py                  # Primary Streamlit dashboard, state manager & UI
├── severity.py             # OpenCV HSV segmentation, verification & overlays
├── disease_data.py         # Pathology repository, 3-pillar prescriptions & Q&A
├── requirements.txt        # Pinned runtime dependencies
├── .gitignore              # Ignored system & cache binaries
└── README.md               # Technical project documentation

```

---

## 💻 Installation & Local Deployment

### Prerequisites

* Python 3.10, 3.11, or 3.12
* Git

### Step-by-Step Setup



Open your browser at `http://localhost:8501`.

---

## 🧪 Pre-Configured Test Cases

For rapid hackathon judge review, use the **Quick Test Cases** radio menu:

| Test Case | Primary Pathology | Severity Profile | Recommended Clinical Intervention |
| --- | --- | --- | --- |
| **Banana: Black Sigatoka** | *Pseudocercospora fijiensis* | ~13.6% (Moderate) | Azoxystrobin + Mineral Oil; De-leafing infected fronds |
| **Tomato: Late Blight** | *Phytophthora infestans* | >30.0% (Critical) | Cymoxanil + Mancozeb; Immediate isolation |
| **Potato: Early Blight** | *Alternaria solani* | ~8.4% (Mild) | Mancozeb protectant; Balanced nitrogen management |
| **Healthy Leaf** | None (Intact Lamina) | 0.0% (Nominal) | Routine nutritional fertigation; Bi-weekly scouting |

---

## 🗺️ Future Roadmap

* [ ] **Edge Deployment:** Quantize segmentation pipelines to run on edge hardware (e.g., Raspberry Pi 5 with Coral TPU) for zero-connectivity offline fields.
* [ ] **Drone Fleet API:** Automatically emit GeoJSON coordinate boundary tags to automated drone sprayers.
* [ ] **DeepLabV3+ Fine-Tuning:** Integrate transformer segmentation checkpoints trained on multi-spectral drone aerial imagery.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---


