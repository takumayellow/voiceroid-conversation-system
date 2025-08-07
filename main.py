"""
main.py - Entry point for the VOICEROID conversation system.

This script listens for speech from the microphone, transcribes it to
Japanese text using the Google Speech Recognition API, and then
delegates the task of generating a response and speaking that
response aloud to `voiceroid_speaks.py`.

To run this script you will need a working microphone attached to
your computer and access to the Google Speech Recognition service.

Example:

    python main.py

When prompted, speak a question in Japanese. If the speech is
successfully recognized, the recognized text is passed to
`voiceroid_speaks.py` for further processing. If the speech is not
recognized, a message is printed.

Dependencies:
    - speech_recognition
    - requests (via voiceroid_speaks.py)

See README.md for full setup instructions.
"""

import subprocess
import speech_recognition as sr



def main() -> None:
    """Capture speech from the microphone and process it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Calibrate to account for ambient noise.
        recognizer.adjust_for_ambient_noise(source)
        print("あかりちゃんへの質問を喋ってね:")
        audio = recognizer.listen(source)

    # Attempt to recognize Japanese speech using Google's API.
    try:
        msg = recognizer.recognize_google(audio, language="ja-JP")
        print("-----------detect!----------\n", msg)
    except sr.UnknownValueError:
        print("Could not understand audio")
        msg = ""
    except sr.RequestError as exc:
        print(f"Could not request results; {exc}")
        msg = ""

    # If speech was recognized, pass it to voiceroid_speaks.py.
    if msg:
        # Use python executable to run the helper script with the message
        subprocess.run(["python", "voiceroid_speaks.py", msg])
    else:
        print("聞き取れなかったみたいです...")


if __name__ == "__main__":
    main()
