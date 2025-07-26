# 📸 Photo Booth Selfie App (Python + OpenCV + PIL)

A Python-based selfie photo booth app using your webcam. It supports a countdown timer, image retake/confirmation, and combines three photos into a pre-designed template with optional overlay effects.

---

## 🔧 Features

- ⏱ Countdown timer before capturing (3 seconds)
- 📷 Capture images from webcam
- 🔁 Option to **Retake** or **Continue** after each photo
- 🖼 Automatically resizes and positions images on a template background
- 🌟 Applies transparent PNG overlay (effects)
- 💾 Saves the final composed image to disk and opens it automatically

---

## 🖥 Output Example

*(Add your own sample image here)*  
```
photo_template/example_output.png
```

---

## 📁 Folder Structure

```plaintext
photo_booth-stupit/
│
├── Selfie/
│   ├── captured_image_1.jpg
│   ├── captured_image_2.jpg
│   ├── captured_image_3.jpg
│   └── result_image.png
│
├── photo_template/
│   ├── bg.jpeg      <-- Template background image
│   └── ef.png       <-- Transparent overlay (effect)
│
└── main.py          <-- Main script file
```

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install opencv-python pillow
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Follow the on-screen prompts:
   - A 3-second countdown will start
   - You'll be prompted to press:
     - `5` to **Retake**
     - `6` to **Continue**
   - The script saves the final photo composition in `Selfie/result_image.png`

---

## ⌨️ Key Controls

- `Esc` – Cancel countdown or exit camera view
- `5` – Retake the current image
- `6` – Confirm and proceed to next image

---

## ⚙️ Customization Tips

- You can change the layout by modifying the `overlay_positions` list in the code
- Swap `bg.jpeg` or `ef.png` to customize the photo style