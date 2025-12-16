# Real-Time Face Blur Tool

A professional-grade real-time face detection and blurring application built with Python. This tool uses advanced machine learning to detect faces in live video streams and applies customizable blur effects to protect privacy.

## Features

- **Real-Time Face Detection**: Leverages Google's MediaPipe for fast and accurate face detection
- **Multiple Blur Modes**:
  - **Soft Polygon Blur (Mode 3)**: Elliptical mask for a natural, soft appearance
  - **Full Facial Mask Blur (Mode 4)**: Complete face coverage with rectangular masking
- **Adjustable Blur Intensity**: 5-level intensity control for precise blur customization
- **Live Preview**: Interactive GUI with real-time video feed display
- **Low Latency**: Optimized for responsive performance with minimal lag

## Technical Stack

- **OpenCV**: Video capture and image processing
- **MediaPipe**: Face detection and localization
- **NumPy**: Numerical operations and array manipulation
- **Tkinter**: Cross-platform GUI framework
- **Pillow**: Image format conversion and display

## Requirements

- Python 3.7+
- Webcam or video capture device
- 4GB RAM (recommended)

## Installation

1. Clone or download the project:
```bash
cd real-time-tkinter-blur-app
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

**Dependencies:**
- opencv-python==4.8.1.78
- mediapipe==0.10.9
- numpy==1.25.2
- Pillow==10.1.0

## Usage

Run the application:
```bash
python main.py
```

### Controls

| Control | Description |
|---------|-------------|
| **Blur Mode** | Select between Soft Polygon (3) or Full Facial Mask (4) blur effects |
| **Blur Intensity** | Adjust blur level from 1 (subtle) to 5 (maximum) |

The application window displays your live video feed with detected faces automatically blurred according to your settings.

## How It Works

1. **Face Detection**: The application continuously captures video frames and uses MediaPipe's face detection model to identify faces
2. **Region Extraction**: Detected face regions are extracted as bounding boxes with pixel-perfect coordinates
3. **Blur Application**: Gaussian blur is applied to each face region based on the selected mode and intensity
4. **Masking**: Depending on the blur mode, either an elliptical or rectangular mask is applied to blend the blurred region naturally
5. **Display**: The processed frame is converted to RGB and displayed in the Tkinter GUI with ~100ms refresh rate

### Blur Intensity Mapping

| Level | Kernel Size |
|-------|-------------|
| 1 | 15×15 |
| 2 | 25×25 |
| 3 | 45×45 |
| 4 | 75×75 |
| 5 | 99×99 |

## Key Features Explained

### Soft Polygon Blur (Mode 3)
Uses an elliptical mask to create a natural-looking blur effect that respects face proportions and reduces artifacts at edges.

### Full Facial Mask Blur (Mode 4)
Applies blur to the entire detected face region with a rectangular coverage, providing maximum privacy protection.

## Performance Considerations

- **Frame Rate**: Optimized for ~100ms per frame on standard hardware
- **Detection Confidence**: Set to 60% minimum for balanced accuracy and performance
- **CPU Usage**: Efficient processing suitable for real-time applications
- **Memory**: Lightweight design with minimal memory footprint

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Processor**: Intel i3 or equivalent
- **RAM**: 4GB minimum
- **GPU**: Optional (CPU inference is sufficient for real-time performance)

## Exit

Close the application window or press the window close button to stop the program and release the webcam.

## License

Open source project available for educational and privacy-protection purposes.

## Contributing

Feel free to extend this project with:
- Additional blur effects or filters
- Multi-face optimization
- Frame rate improvements
- Recording and export functionality
- Face detection model switching

## Support

For issues with face detection, ensure:
- Your webcam is properly connected and functional
- Adequate lighting conditions
- Valid camera permissions

---

**Built with** ❤️ **for privacy and security**
