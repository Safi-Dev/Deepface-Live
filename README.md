# Webcam Analysis with DeepFace and OpenCV

This Python script uses the DeepFace library and OpenCV to perform real-time analysis of faces detected in a webcam feed. It displays bounding boxes around detected faces and provides information about the dominant emotion, age, gender, and race.

## Requirements

- Python 3.x
- OpenCV
- DeepFace
- Pygame

To install the required libraries, run the following commands:

```bash
pip install opencv-python
pip install deepface
pip install pygame
```

## Usage

1. Clone the repository or download the script.
    ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory.
3. Run the script:
    ```bash
   python webcam_analysis.py
   ```
    The script will open a window displaying the webcam feed with bounding boxes and analysis results for detected faces.
4. Press 'q' to quit the program.

## License

Shield: [![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg
