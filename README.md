# When the Economy Turns Grey, So Does Fashion  
### A Machine Learning Analysis of Color Trends and Macroeconomic Conditions

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-KMeans-orange" />
  <img src="https://img.shields.io/badge/Computer%20Vision-OpenCV-green" />
  <img src="https://img.shields.io/badge/Data-FRED%20API-lightgrey" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## Overview

Fashion is often described as a reflection of economic sentiment—but most evidence remains anecdotal (e.g., the “lipstick effect”).

This project takes a **data-driven approach**.

Using **computer vision and unsupervised machine learning**, I analyze **2,400 runway images (2000–2023)** to quantify changes in color intensity and test whether fashion becomes more “neutral” during economic downturns.

> **Key Question:**  
> When the economy weakens, does fashion become more muted?

---

## Key Results

- 📉 Higher unemployment → **lower color intensity (chroma)**
- ⚫ Recession periods → **more neutral color palettes**
- ⏳ Evidence of **lagged response** in fashion trends
- 📊 Statistically significant difference between recession vs expansion periods  
  *(t = 3.91, p < 0.001)*

---

## Methodology

### 1. Image Processing Pipeline
- Removed backgrounds using **deep learning segmentation (`rembg`)**
- Isolated garments from runway noise (lighting, staging, audience)

### 2. Color Extraction
- Applied **K-Means clustering (k=8)** per image
- Converted to **CIELab color space** for perceptual accuracy

### 3. Feature Engineering

**Mean Chroma (Color Intensity):**

C = √(a² + b²)


- Lower → muted / neutral tones  
- Higher → vivid / saturated tones  

**Neutral Share:**
- % of palette below chroma threshold  
- Captures dominance of neutral colors  

### 4. Modeling

Built regression models linking fashion metrics to:

- Unemployment rate (FRED)
- Recession indicators (NBER)
- Lagged macroeconomic variables
- Time trend (year)

---

## Data

| Source | Description |
|------|--------|
| Vogue Runway | 100 images/year (2000–2023) |
| FRED | U.S. unemployment rates |
| NBER | Recession indicators |

---

## Model Performance

| Model | Variables | R² |
|------|----------|----|
| Model 1 | Unemployment + Recession | 0.087 |
| Model 2 | + Year Trend | 0.104 |
| Model 3 | + Lagged Recession | 0.062 |

---

## Tech Stack

- **Python 3.11**
- `scikit-learn` – KMeans clustering  
- `OpenCV`, `rembg` – image processing  
- `pandas`, `NumPy` – data manipulation  
- `Matplotlib` – visualization  
- FRED API – macroeconomic data  

---

## Why This Project Matters

This project reframes fashion as **quantifiable data**, showing that:

- Aesthetic trends can be measured systematically  
- Machine learning can uncover patterns in **non-traditional datasets**  
- Cultural signals (like fashion) may track macroeconomic conditions  

> This bridges **computer vision, economics, and cultural analytics**.

---

## Limitations

- Runway ≠ consumer purchasing behavior  
- Fashion influenced by design cycles, culture, and seasonality  
- Chroma simplifies complex visual aesthetics  

---

## Future Work

- Incorporate **texture, silhouette, and fabric features**
- Expand to **consumer / retail datasets**
- Validate metrics with **human perception studies**
- Build **brand-level “style fingerprints”**

---

## Author

**Maria Workman**  
UNC Chapel Hill — Statistics & Computer Science  

---

## TL;DR

> Fashion doesn’t just reflect the economy —  
> it can be **measured as part of it**.