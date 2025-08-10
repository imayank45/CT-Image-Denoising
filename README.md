# 🧠 CT Image Denoising & Tumor Detection  

## 🌟 Overview  
The **CT Image Denoising & Tumor Detection** project is an **autoencoder-based system** designed to denoise brain CT scans (**DICOM format**) and perform **tumor detection** on the enhanced images.  

- **Removes acquisition noise** while preserving anatomical details.  
- **Improves image clarity** and boosts tumor classification performance.  
- **Minimal Flask UI** for quick scan uploads and instant result viewing.  
- **Deployed on AWS EC2** (managed via PuTTY) for remote accessibility.  

---

## 📂 Repository Structure  

```plaintext
CT-Image-Denoising/
├── models/                # Trained models (autoencoder, tumor detector)
├── static/                # Flask static assets (CSS, JS, images)
├── templates/             # Flask templates (index.html, result.html)
├── README.md               # ← this file
├── app.py                  # Main app: preprocessing, model load, inference, evaluation
└── requirements.txt        # Python dependencies
```

**Note:**  
- `app.py` is the **main script** — handles DICOM reading, preprocessing, model inference,  
  SNR calculation, classification report generation, and serving the Flask UI.  

---

## ✨ Key Highlights  

- 🧠 **Autoencoder (CNN)** for denoising brain CT scans (DICOM).  
- 🩺 **Tumor detection** on denoised images with validated performance improvements.  
- ☁️ **Deployed on AWS EC2** (managed via PuTTY) for accessibility.  
- 📊 **Evaluation** includes classification reports & SNR metrics.  

---

## 📈 Evaluation — Classification Reports  

### 🖤 Noisy Image  
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.50      | 0.50   | 0.50     | 4       |
| 1     | 0.50      | 0.50   | 0.50     | 6       |
| 2     | 0.00      | 0.00   | 0.00     | 4       |
| 3     | 0.33      | 0.40   | 0.36     | 5       |
| **Accuracy**   |           |        | **0.37** | **19** |
| Macro Avg | 0.33 | 0.35   | 0.34     | 19      |
| Weighted Avg | 0.35 | 0.37 | 0.36   | 19      |

---

### 🤍 Denoised Image  
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.75   | 0.86     | 4       |
| 1     | 0.86      | 1.00   | 0.92     | 6       |
| 2     | 0.75      | 0.75   | 0.75     | 4       |
| 3     | 0.80      | 0.80   | 0.80     | 5       |
| **Accuracy**   |           |        | **0.84** | **19** |
| Macro Avg | 0.85 | 0.82   | 0.83     | 19      |
| Weighted Avg | 0.85 | 0.84 | 0.84   | 19      |

**Takeaway:** 📈 Accuracy improved **from 0.37 → 0.84** after denoising.  

---

## 🔬 SNR Comparison  

| Condition     | SNR (dB) |
|---------------|----------|
| Noisy Image   | 2.94     |
| Denoised Image| 15.58    |

---

## 📷 Screenshots  

Here are sample screenshots from the Flask UI and results:  


### 🔹 Noisy vs Denoised Image Comparison  
![Image Comparison](static/screenshots/noisy_vs_denoised.png)  

### 🔹 Tumor Detection Output  
![Tumor Detection](static/screenshots/tumor_detection_result.png)  

*(Ensure you place your actual screenshot images in `static/screenshots/` directory for these links to work.)*  

---

## ▶️ Usage (Local)  

1. **Install dependencies** from `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```  
2. **Place trained model files** in the `models/` directory.  
3. **Run the application**:  
   ```bash
   python app.py
   ```  
4. **Open the Flask UI** in your browser to upload DICOM scans and view results.  

---

## 📬 Contact  
👨‍💻 **Mayank Kathane**  
