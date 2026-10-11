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
