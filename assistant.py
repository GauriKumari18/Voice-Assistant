import speech_recognition as sr
from speech import SpeechRecognizer
import config

class Assistant:
    def __init__(self):
        """Initializes the assistant and its speech recognizer."""
        self.recognizer_tools = SpeechRecognizer()

    def run(self):
        """Starts the assistant, listens for input, and prints the recognized text."""
        try:
            audio = self.recognizer_tools.listen()
            
            # Pass the language parameter from the config file
            text = self.recognizer_tools.recognizer.recognize_google(
                audio, 
                language=config.LANGUAGE
            )
            print(f"You said: {text}")
            
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestException as e:
            print(f"Could not request results from the recognition service; {e}")