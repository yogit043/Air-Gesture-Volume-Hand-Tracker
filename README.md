# Hand Gesture Volume Control

This project uses computer vision to control the system volume using hand gestures. The implementation leverages OpenCV and MediaPipe for hand tracking and gesture recognition, and PyCaw for controlling the system audio.

## Features

- Real-time hand tracking and gesture recognition.
- Control system volume using the distance between the thumb and index finger.
- Display current volume level as a percentage on the screen.
- Display frames per second (FPS) for performance monitoring.

## Requirements

- Python 3.6 or higher
- OpenCV
- MediaPipe
- PyCaw
- comtypes

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yogit043/Air-Gesture-Volume-Hand-Tracker.git
    cd Air-Gesture-Volume-Hand-Tracker
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install opencv-python mediapipe numpy comtypes pycaw
    ```

## HandTrackingModule.py

This module defines the `handDetector` class, which is responsible for detecting hands and their landmarks using MediaPipe.

### Methods

- `findHands(img, draw=True)`: Detects hands in the provided image and optionally draws landmarks.
- `findPosition(img, handNo=0, draw=True)`: Returns a list of landmarks positions for the specified hand.

## Dependencies

- **OpenCV**: For image processing and computer vision tasks.
- **MediaPipe**: For hand tracking and gesture recognition.
- **PyCaw**: For controlling the system audio.
- **comtypes**: Required by PyCaw for interfacing with Windows COM.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyCaw](https://github.com/AndreMiras/pycaw)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

