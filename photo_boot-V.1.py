import cv2
import time
from PIL import Image

def countdown(timer, cap):
    font = cv2.FONT_HERSHEY_SIMPLEX
    start_time = time.time()
    while timer > 0:
        ret, frame = cap.read()
        if not ret:
            print("ไม่สามารถอ่านภาพจากกล้องได้")
            break
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            timer -= 1
            start_time = time.time()

        # แสดงการนับถอยหลังบนภาพ
        frame_copy = frame.copy()
        cv2.putText(frame_copy, str(timer), (50, 50), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Press Space to Capture', frame_copy)
        if cv2.waitKey(1) & 0xFF == 27:  # กดปุ่ม ESC เพื่อออกจากการนับถอยหลัง
            break

def capture_image(cap, filename):
    print("Starting countdown...")
    countdown(3, cap)

    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
    else:
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ไม่สามารถเปิดกล้องได้")
        return
    
    # ตั้งค่าความกว้างและความสูงของวิดีโอ
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # ปรับความกว้างของวิดีโอ (เช่น 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # ปรับความสูงของวิดีโอ (เช่น 480)

    image_paths = []
    for i in range(3):
        captured_image_path = f"/Users/thanayot/Documents/photobooth/captured_image_{i + 1}.jpg"
        
        while True:
            capture_image(cap, captured_image_path)
            img = Image.open(captured_image_path)
            img.show()

            print("Press '5' to retake the picture or '6' to continue.")
            while True:
                key = cv2.waitKey(0) & 0xFF  # Wait for a key press
                if key == 53:  # Key '5'
                    print("Retaking the picture...")
                    img.close()
                    break
                elif key == 54:  # Key '6'
                    print("Continuing...")
                    img.close()
                    image_paths.append(captured_image_path)
                    break

            if key == 54:  # If '6' was pressed, continue to the next image
                break

    cap.release()
    cv2.destroyAllWindows()

    # Load background image
    background = Image.open("/Users/thanayot/Documents/photobooth/bg.jpeg").convert("RGBA")
    ef = Image.open("/Users/thanayot/Documents/photobooth/ef.png").convert("RGBA")

    # List of images to overlay with positions
    overlay_positions = [
        (35, 250),  # Position for first image
        (35, 750),  # Position for second image
        (35, 1250)  # Position for third image
    ]

    # Overlay each image onto the background while maintaining aspect ratio
    for index, position in enumerate(overlay_positions):
        overlay = Image.open(image_paths[index]).convert("RGBA")
        
        # Calculate new size maintaining aspect ratio
        max_width, max_height = 530, 530
        width_ratio = max_width / overlay.width
        height_ratio = max_height / overlay.height
        scaling_factor = min(width_ratio, height_ratio)
        new_size = (int(overlay.width * scaling_factor), int(overlay.height * scaling_factor))
        
        overlay = overlay.resize(new_size, Image.Resampling.LANCZOS)

        # Paste overlay onto background
        background.paste(overlay, position, overlay)

    # Overlay ef image
    ef = ef.resize(background.size, Image.Resampling.LANCZOS)
    background.paste(ef, (0, 0), ef)

    # Save the result
    background.save("/Users/thanayot/Documents/photobooth/result_image.png")

    # Show the result
    background.show()

if __name__ == "__main__":
    main()
