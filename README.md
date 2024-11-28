# 🤟🏽 Deaf_Not_Dead

![LOGO](https://github.com/user-attachments/assets/85d86f53-c233-46d3-8545-f61d22bf4bc6)  

https://youtu.be/cUp5QKGdM64



------------------------------------------------

This project aims to develop an software application that leverages speech-to-text technology to translate spoken language into sign language(ASL)

### Text Template Loading: 
The program reads a text template from the greetingTemplate.txt file, which serves as a reference sentence.

### Speech Capture: 
Using a microphone, the program listens to the user’s spoken input and adjusts for background noise to improve recognition accuracy.
### Audio Processing: 
The captured audio is saved as a .wav file, and speech recognition converts it into text, saving the output to book.txt.
### Text Comparison: 
The spoken text is compared to the text template. If the words match perfectly, the program proceeds.
### Video Playback: 
Upon a successful match, a video file specified by the video_path variable is played using OpenCV.
### Error Handling: 
The program accounts for various errors, such as missing files, speech recognition failures, or issues with video playback.
### Feedback: 
Clear messages guide the user throughout the process, from speaking to watching the video.
### Exit Option: 
The video playback can be stopped anytime by pressing the 'Q' key.
This project is an excellent demonstration of combining real-time speech recognition with multimedia interaction.








PROJECT STRUCTURE :
-------------------

project.py

test_project.py

book.txt

greetingTemplate.txt

requirements.txt

VIDEO

README.md


IN THIS PROJECT WE'RE GOING TO TEST A SPECIFIC GREETING SENTENCE BELOW 👇🏿
-------------------------------------------------------------------
                                     "Hello world"

                                  "i am from america," 

                                   " nice to meet you"

                                      "Welcome CS50"

--------------------------------------------------------------------

STEPS
------

### Step 1: launch the program : python3 project.py

### Step 2: follow the instruction, said the greeting template sentence

### Step 3: Enjoy the asl video if your words == greeting template.

 🇺🇸the greeting phrase will be translated in ASL.


![aslcover](https://github.com/user-attachments/assets/d2283f22-e8c4-4ee9-8202-0f9db4cc9c64)

LIBRAIRIES
-----------

# 📚 Libraries Used and Installation
## 1. SpeechRecognition == 3.10.4

This library enables converting audio to text using speech recognition engines like Google Speech API.
Installation:
pip install SpeechRecognition==3.10.4

## 2. pyaudio == 0.2.14
Used to capture or stream real-time audio from a microphone or speakers.

Installation:
On Windows:

pip install pipwin

pipwin install pyaudio


On Linux/macOS:

pip install pyaudio


## 3. pytest == 8.3.2
   
A testing framework to verify the proper functioning of the code.

### Installation:

pip install pytest==8.3.2


## 4. opencv-python == 4.10.0.84

A library for computer vision and processing images/videos.

### Installation:

pip install opencv-python==4.10.0.84


## 5. standard-aifc == 3.13.0
Used to read and write audio files in AIFF (Audio Interchange File Format).

### Installation:

pip install standard-aifc==3.13.0

## OR

### There is a requirements.txt file that has all the libraries used.

### and simply can be install by this pip command:

### pip install  requirements.txt


# Usage
Run the program python script project.py with python.

## python project.py
Test the program python script test_project.py with pytest.

## pytest test_project.py