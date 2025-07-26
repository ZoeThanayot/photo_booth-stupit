# 📸 Photo Booth Selfie App (Python + OpenCV + PIL)

A Python-based selfie photo booth app using your webcam. It features a countdown timer, image preview with option to retake, and composes three captured photos into a single photo template with overlay effects.

---

## 🔧 Features

- ⏱ 3-second countdown before each photo is captured
- 📷 Automatically captures webcam images
- 🔁 Lets users retake or confirm each image
- 🖼 Resizes and places images into a photo template background
- 🌟 Adds a transparent PNG overlay (effect) on top of the result
- 💾 Saves the final composed photo and displays it

---

## 🖥 Output Example

> *(Replace this path with your sample image if needed)*  
> `photo_template/example_output.png`

---

## 📁 Folder Structure

photo_booth-stupit/
│
├── Selfie/
│ ├── captured_image_1.jpg
│ ├── captured_image_2.jpg
│ ├── captured_image_3.jpg
│ └── result_image.png
│
├── photo_template/
│ ├── bg.jpeg <-- Background template image
│ └── ef.png <-- Overlay (transparent effect)
│
└── main.py <-- Main script

yaml
คัดลอก
แก้ไข

---

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install opencv-python pillow
Run the application:

bash
คัดลอก
แก้ไข
python main.py
Follow the process:

The app opens the webcam

Starts a countdown

Captures and shows each image

Press:

5 to Retake

6 to Continue

After 3 images are captured, they are composed onto a background and saved to:

bash
คัดลอก
แก้ไข
/Selfie/result_image.png
⌨️ Key Controls
Esc → Cancel countdown or exit camera

5 → Retake the current image

6 → Confirm and proceed to the next

⚙️ Customization
To adjust photo positions on the background, edit the overlay_positions list in main.py

To use a different background or overlay, replace bg.jpeg and ef.png in the photo_template/ folder