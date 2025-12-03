import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ----------------- MediaPipe Face Detection -----------------
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.6)

# ----------------- Tkinter GUI Setup -----------------
root = tk.Tk()
root.title("Real-Time Face Blur Tool")

# Variables
mode_var = tk.IntVar(value=3)        # 3 = Soft Polygon, 4 = Full Facial Mask
blur_level_var = tk.IntVar(value=3)  # 1 to 5

# Video display label
video_label = tk.Label(root)
video_label.pack()

# ----------------- Control Panel -----------------
control_frame = tk.Frame(root)
control_frame.pack(fill=tk.X, padx=10, pady=5)

# Blur Mode
tk.Label(control_frame, text="Blur Mode:").grid(row=0, column=0, sticky="w")
mode_combo = ttk.Combobox(control_frame, textvariable=mode_var, values=[3, 4], width=5)
mode_combo.grid(row=0, column=1, padx=5)

# Blur Intensity
tk.Label(control_frame, text="Blur Intensity:").grid(row=1, column=0, sticky="w")
blur_slider = tk.Scale(control_frame, from_=1, to=5, orient=tk.HORIZONTAL, variable=blur_level_var)
blur_slider.grid(row=1, column=1, padx=5)

# ----------------- Webcam Capture -----------------
cap = cv2.VideoCapture(0)

# Map blur intensity to kernel size
kernel_map = [15, 25, 45, 75, 99]

def apply_blur(face_region, mode, kernel_size):
    blurred_face = cv2.GaussianBlur(face_region, (kernel_size, kernel_size), 30)
    h, w = face_region.shape[:2]

    if mode == 3:
        # Soft Polygon Blur (approximated as ellipse)
        mask = np.zeros((h, w, 3), dtype=np.uint8)
        center = (w // 2, h // 2)
        axes = (w // 2, int(h * 0.60))
        cv2.ellipse(mask, center, axes, 0, 0, 360, (255, 255, 255), -1)
    elif mode == 4:
        # Full Facial Mask Blur (rectangle covering full face)
        mask = np.ones((h, w, 3), dtype=np.uint8) * 255
    else:
        # Fallback: full rectangle
        mask = np.ones((h, w, 3), dtype=np.uint8) * 255

    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    face_bg = cv2.bitwise_and(face_region, face_region, mask=cv2.bitwise_not(mask_gray))
    face_fg = cv2.bitwise_and(blurred_face, blurred_face, mask=mask_gray)
    return cv2.add(face_bg, face_fg)

def update_frame():
    ret, frame = cap.read()
    if not ret:
        root.after(10, update_frame)
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    kernel_size = kernel_map[blur_level_var.get() - 1]
    mode = mode_var.get()

    if results.detections:
        height, width = frame.shape[:2]
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x = int(bbox.xmin * width)
            y = int(bbox.ymin * height)
            w = int(bbox.width * width)
            h = int(bbox.height * height)

            x = max(0, x)
            y = max(0, y)
            w = max(1, w)
            h = max(1, h)

            face_region = frame[y:y+h, x:x+w]
            frame[y:y+h, x:x+w] = apply_blur(face_region, mode, kernel_size)

    # Convert to ImageTk
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    # Schedule next frame
    video_label.after(10, update_frame)

# Start the loop
update_frame()
root.mainloop()

# Release camera on exit
cap.release()
