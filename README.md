CT Image Denoisig & Tumor Detection 🧠🩻✨
Autoencoder-based system that denoises brain CT scans (DICOM) and runs tumor detection on the denoised images. The pipeline preserves anatomical details while removing acquisition noise, improving image clarity and boosting classification performance for tumor detection. Simple Flask UI lets clinicians upload scans and view results quickly. Deployed on AWS EC2 (managed via PuTTY).

🔎 Repo snapshot (exact files / folders)
csharp
Copy
Edit
CT-Image-Denoising/
├── models/                 # Trained models (autoencoder, tumor detector)
├── static/                 # Flask static assets
├── templates/              # Flask templates (index.html, result.html, etc.)
├── README.md               # ← this file
├── app.py                  # ← main app: preprocessing, model load, inference, evaluation
└── requirements.txt        # Python dependencies
app.py is the main script — it handles DICOM reading, preprocessing, model inference, SNR calculation and classification report generation, and serves the Flask UI.

✨ Key highlights
🧠 Autoencoder (CNN) based denoising for brain CT (DICOM).

🩺 Tumor detection on denoised images with validated performance.

☁️ Deployed on AWS EC2 (access/managed via PuTTY).

🧾 Evaluation includes SNR and classification reports showing clear improvements.

📈 Evaluation — Classification reports
Noisy Image

Class	Precision	Recall	F1-Score	Support
0	0.50	0.50	0.50	4
1	0.50	0.50	0.50	6
2	0.00	0.00	0.00	4
3	0.33	0.40	0.36	5
Accuracy			0.37	19
Macro Avg	0.33	0.35	0.34	19
Weighted Avg	0.35	0.37	0.36	19

Denoised Image

Class	Precision	Recall	F1-Score	Support
0	1.00	0.75	0.86	4
1	0.86	1.00	0.92	6
2	0.75	0.75	0.75	4
3	0.80	0.80	0.80	5
Accuracy			0.84	19
Macro Avg	0.85	0.82	0.83	19
Weighted Avg	0.85	0.84	0.84	19

Takeaway: denoising increased accuracy from 0.37 → 0.84.

🔬 SNR comparison
Reported SNR values used for quantitative comparison:

Noisy Image SNR: 2.94 dB

Denoised Image SNR: 15.58 dB

Takeaway: SNR increased substantially after denoising, indicating effective noise reduction while preserving signal.

🖼️ Visuals — add screenshots
Place your screenshots in a docs/ (or static/) folder with these names so they render in the README:

docs/classification_noisy.png

docs/classification_denoised.png

docs/snr_comparison.png

Use simple markdown image links to show them in the README.

▶️ Minimal usage (how to run)
Install dependencies from requirements.txt.

Put trained model files into models/ (autoencoder + tumor detector).

Start the Flask app (app.py) and open the local UI to upload DICOM files.

For production, the app is deployed on AWS EC2 (managed via PuTTY).
