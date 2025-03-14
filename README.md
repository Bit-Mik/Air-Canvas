# Air Canvas

## Overview
This project implements a **hand tracking system** using OpenCV and MediaPipe to recognize hand gestures. It allows users to draw on a canvas using their index and middle fingers and send the drawn image to an AI model for interpretation.

## Features
- **Hand Tracking**: Uses MediaPipe to detect and track hands in real time.
- **Gesture Recognition**: Recognizes specific finger gestures to perform actions.
- **Drawing Functionality**: Allows users to draw by moving their hand.
- **AI Interaction**: Sends the drawn image to an AI model for interpretation.
- **Clear Canvas**: Users can reset the drawing canvas using a specific gesture.

## Requirements
Make sure you have the following installed:
- **Python 3.x**
- **OpenCV** (`cv2` module)
- **NumPy**
- **Pillow** (`PIL` module for image handling)
- **Google Generative AI SDK**

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install -r requirements.txt
```

## How to Run the Script
1. Clone or download the project.
2. Open a terminal and navigate to the project directory.
3. Set up the API key for Google Generative AI by setting the environment variable `API_KEY`.
4. Run the script:
   ```sh
   python main.py
   ```
5. The webcam feed will appear.
6. Use the following hand gestures:
   - **[0,1,1,0,0]**: Draw on the canvas.
   - **[0,1,0,0,1]**: Clear the canvas.
   - **[1,1,1,0,1]**: Send the canvas to AI for interpretation.
   - **'q'**: Quit the application.

## Folder Structure
```
air-canvas/
│── .gitignore          # Git ignore file
│── IMPORTS.py          # Module for imports and configuration
│── main.py             # Main script
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

## How It Works
- The script initializes a webcam feed and detects hands using MediaPipe.
- Specific hand gestures control drawing, clearing, and sending to AI.
- The drawn image is processed and sent to the AI model for interpretation.

## Possible Enhancements
- **Multiple Hand Support**: Extend tracking for multiple users.
- **Gesture Customization**: Allow users to define their own gestures.
- **Different Brush Sizes**: Add the ability to change the drawing thickness.
- **Save Drawings**: Option to save drawn images locally.

## License
This project is open-source. Feel free to modify and improve it!

## Author
Biswajit Mallik
