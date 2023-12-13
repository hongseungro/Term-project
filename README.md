# Snapshot_with_V
This program uses OpenCV and Mediapipe to detect hand gestures and captures a photo when all of users forms the hand shape 'V'.
## Usage
1. **Install python**
```bash
$ pip install python
```
2. **Install Dependencies**
```bash
$ pip install mediapipe
```
3. Run
```bash
$ python Snapshot_with_V.py
```
4. Save Photos
When the program detects a 'V' hand shape with the user's face detected, the current screen is saved as 'frame_(frame_number).jpg'
For example, if there are four people in screen of webcam (or connected camera), and all of them pose 'V' hand shape, the screen that 4 people posing 'V' is captured. And the shot is saved named by 'frame_(frame_number).jpg'.
Although three people pose 'V', if just one person don't pose, the screen is not saved.

# Result
![Result](https://i.ibb.co/9GWRmrk/result-Of-Runnung.jpg)
# Key Features
- Use of Harr Cascade classifier for face detection
- Hand shape detection using the Mediapipe library
- Capture of the current screen when a 'V' hand shape is detected

# Requirements
- Python 3.xx
- OpenCV
- Mediapipe

# Source of reference
- detect human's face
[Source of detecting face](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- detect posing hand shape 'V'
[Source of detecting V](https://www.gongdo.kr/play/wEOG72foET9YR97nFG6S?t=cn)
