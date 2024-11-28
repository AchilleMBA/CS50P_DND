import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


import speech_recognition as sr
import cv2


def main():
    greeting_template, spoken_text = process_audio_and_text()
    if spoken_text is None:
        print("Speech recognition failed or no text was provided.")
        return
    print(f"You said: {spoken_text}")

    if compare_texts(greeting_template, spoken_text):
        play_video(video_path)
    else:
        print("The sentences do not match word by word.")

# Create a global Recognizer object
recognizer = sr.Recognizer()

def process_audio_and_text():
    try:
        with open("greetingTemplate.txt", "r") as file:
            greeting_template = file.read().strip()
    except FileNotFoundError:
        print("Error: 'greetingTemplate.txt' file not found.")
        return None, None

    print("Adjusting for background noise... please wait.")
    print("Please say the sentence below:")
    print(greeting_template)

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)

            # Save the audio
            with open("test_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            print("Audio saved to 'test_audio.wav'.")

            # Speech recognition
            spoken_text = recognizer.recognize_google(audio, language="en-US").strip().lower()

            with open("book.txt", "w") as file:
                file.write(spoken_text)
                print("Text has been saved to 'book.txt'.")

    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio.")
        return greeting_template, None
    except sr.RequestError:
        print("Unable to reach the speech recognition service.")
        return greeting_template, None

    return greeting_template, spoken_text

def compare_texts(greeting_template, spoken_text):
    template_words = greeting_template.split()
    spoken_words = spoken_text.split()
    if template_words == spoken_words:
        print("Perfect match with the template.")
        return True
    return False

video_path = "/Users/achmab/Desktop/CS50P_DND/VIDEO/hey_asl.mp4"

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return
    print("Playing the video...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video reached.")
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
