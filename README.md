# 📸 Photo Booth Selfie App

A Python-based interactive photo booth application that captures three selfies using your webcam and combines them into a stylized photo strip with custom backgrounds and overlay effects.

## ✨ Features

- **📷 Webcam Integration**: Real-time camera feed with OpenCV
- **⏱️ Countdown Timer**: 3-second countdown before each photo capture
- **🔄 Retake Option**: Review and retake photos before proceeding
- **🖼️ Photo Composition**: Combines 3 photos into a vertical photo strip layout
- **🎨 Custom Templates**: Background and overlay effects support
- **💾 Auto-Save & Display**: Saves final result and opens it automatically

## 🛠️ Requirements

- Python 3.6+
- OpenCV (`cv2`)
- PIL/Pillow
- Webcam/Camera

## 📦 Installation

1. **Clone or download this repository**

2. **Install required dependencies:**
   ```bash
   pip install opencv-python pillow
   ```

3. **Verify your webcam is connected and working**

## 🚀 Quick Start

1. **Run the application:**
   ```bash
   python photo_boot-V.1.py
   ```

2. **Follow the photo booth process:**
   - Position yourself in front of the camera
   - Wait for the 3-second countdown
   - Review your photo when it appears
   - Press `5` to retake or `6` to continue
   - Repeat for all 3 photos
   - Your final photo strip will be saved and displayed

## 📁 Project Structure

```
photo_booth-stupit/
├── photo_boot-V.1.py          # Main application script
├── Selfie/                     # Output directory
│   ├── captured_image_1.jpg    # Individual captured photos
│   ├── captured_image_2.jpg
│   ├── captured_image_3.jpg
│   └── result_image.png        # Final photo strip
├── photo_template/             # Template assets
│   ├── bg.jpeg                 # Background template
│   └── ef.png                  # Overlay effects (PNG with transparency)
└── README.md                   # This file
```

## ⌨️ Controls

| Key | Action |
|-----|--------|
| `ESC` | Cancel countdown or exit camera view |
| `5` | Retake current photo |
| `6` | Confirm photo and continue |

## 🎨 Customization

### Background Template
- Replace `photo_template/bg.jpeg` with your custom background
- Recommended size: 600x1800 pixels (or adjust code accordingly)

### Overlay Effects
- Replace `photo_template/ef.png` with your custom overlay
- Must be PNG format with transparency support
- Will be resized to match background dimensions

### Photo Positions
Modify the `overlay_positions` list in `photo_boot-V.1.py`:
```python
overlay_positions = [
    (35, 250),   # First photo position (x, y)
    (35, 750),   # Second photo position
    (35, 1250)   # Third photo position
]
```

### Photo Size
Adjust the maximum photo dimensions in the code:
```python
max_width, max_height = 530, 530  # Change these values
```

## 🔧 Technical Details

- **Camera Resolution**: 640x480 (configurable)
- **Image Format**: JPEG for captures, PNG for final output
- **Aspect Ratio**: Maintained during photo resizing
- **Resampling**: LANCZOS for high-quality image scaling

## 🐛 Troubleshooting

### Camera Issues
- **Camera not found**: Ensure your webcam is connected and not used by other applications
- **Permission denied**: Grant camera access permissions to your terminal/Python

### Image Quality
- **Blurry photos**: Ensure good lighting and stable positioning
- **Dark images**: Improve room lighting or adjust camera settings

### File Path Issues
- **File not found**: Ensure the `photo_template/` directory and assets exist
- **Permission errors**: Check write permissions for the `Selfie/` directory

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements:
- Add more photo layouts
- Implement different countdown styles
- Add photo filters or effects
- Improve the user interface

## 📄 License

This project is open source. Feel free to modify and distribute as needed.

## 🙏 Acknowledgments

- Built with OpenCV for computer vision
- PIL/Pillow for image processing
- Designed for fun photo booth experiences