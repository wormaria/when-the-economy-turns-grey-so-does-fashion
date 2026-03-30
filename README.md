# fashion neutrality trends on the runway

![status](https://img.shields.io/badge/status-in%20progress-blue)
![python](https://img.shields.io/badge/python-3.10+-blue)
![focus](https://img.shields.io/badge/focus-computer%20vision%20%7C%20data%20science-lightgrey)

---

## tl;dr

- built a computer vision pipeline to **quantify fashion aesthetics** using color (chroma)  
- validated that the metric captures **real differences in visual style**  
- found clear time trends in runway color intensity (2013–2023)  
- extended the analysis to test whether **fashion becomes more neutral during economic downturns**  
- early results suggest a relationship between **economic stress and muted color palettes**

---

## about this project

i started this project in november 2025 after noticing a recurring idea online: that fashion has been “getting more neutral” over time — fewer bold colors, more beige, gray, black, and muted tones.

people often link this shift to things like minimalism, sustainability, social media aesthetics, or even economic uncertainty.

i wanted to test whether that idea actually shows up in the data.

but instead of just visually inspecting trends, this project asks a deeper question:

> **can we *quantitatively measure* how “neutral” fashion is — and does that measure change in meaningful ways over time?**

to answer that, i built a computer vision pipeline that extracts color information from runway images and constructs a metric of **fashion neutrality** based on chroma (color intensity).

---

## core idea

this project has two main components:

### 1. measuring fashion aesthetics

i use computer vision and unsupervised learning to extract dominant color palettes from runway looks and compute:

- **mean chroma** → how vivid or saturated colors are  
- **neutral color share** → how much of an image is near-gray  

together, these serve as a proxy for how visually “loud” or “muted” fashion is in a given year.

### 2. validating the metric

before using these measures in downstream analysis, i test whether they actually capture meaningful aesthetic differences.

i compare periods that are visually distinct (e.g., high-contrast vs low-contrast eras) and show that the chroma-based metric detects statistically significant differences between them.

this step ensures the metric reflects real variation in fashion, not noise.

---

## data

- runway images from the **internet archive "vogue runway" dataset**
- images sampled across years for temporal balance
- processed into per-image metrics and aggregated yearly

---

## methodology

the pipeline:

1. **image preprocessing**
   - cropping + background reduction

2. **color extraction**
   - k-means clustering (dominant colors)

3. **feature construction**
   - perceptual color space conversion
   - mean chroma
   - neutral share

4. **aggregation**
   - yearly averages

---

## results

the time series shows clear structure:

- **2013–2015:** more muted  
- **2016–2020:** strong shift toward vibrant, high-contrast styles  
- **2023:** noticeable drop in chroma → possible return to neutrality  

mean chroma and neutral share move in opposite directions, reinforcing that both metrics capture the same underlying aesthetic shift.

---

## extending the analysis: economics

after validating the chroma metric, i test:

> **does fashion become more neutral during economic stress?**

i combine fashion data with:

- unemployment rates  
- recession indicators  

and run regression + lag models.

this turns the project into an exploration of how **macroeconomic conditions may influence aesthetic trends**.

---

## project structure

# ***** TO DO *****



---

## current status

- pipeline built end-to-end  
- chroma metric constructed + validated  
- time series trends established  
- economic data integrated  
- regression + lag models implemented  

still exploratory, but structurally complete.

---

## next steps

- extend dataset to **2024–2025**  
- improve garment segmentation  
- refine chroma metric  
- strengthen statistical validation  
- explore additional economic/cultural variables  
- build interactive visualizations  

---

## why this matters

fashion is usually analyzed qualitatively.

this project shows that it’s possible to:

> **quantify aesthetic change and study it like a time series**

it reframes fashion as not just style — but as a measurable reflection of broader social and economic conditions.

---

## setup

```bash
pip install -r requirements.txt