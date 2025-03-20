# Face Recognition Project

This project implements a face recognition system using the integrated camera on your laptop. It captures video frames, detects faces, and recognizes them using a pre-trained model.

## Project Structure

```
face-recognition-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── camera.py        # Camera integration
│   ├── face_recognition.py # Face detection and recognition
│   └── utils
│       └── helpers.py   # Utility functions
├── data
│   ├── raw              # Raw image data
│   └── processed        # Processed image data
├── models
│   └── model.pkl        # Serialized face recognition model
├── requirements.txt      # Python dependencies
├── .gitignore           # Files to ignore by Git
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd face-recognition-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure your laptop's camera is functional and accessible.

## Usage

To run the face recognition application, execute the following command:
```
python src/main.py
```

The application will start capturing video from your camera, detecting faces, and recognizing them in real-time.

## Model Information

The face recognition model is pre-trained and stored in `models/model.pkl`. It utilizes advanced algorithms to accurately identify faces from the captured frames.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.# face_rec_trial
