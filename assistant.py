import speech_recognition as sr
from speech import SpeechRecognizer

class Assistant:
    def __init__(self):
        """Initializes the assistant and its speech recognizer."""
        self.recognizer_tools = SpeechRecognizer()

    def run(self):
        """Starts the assistant, listens for input, and prints the recognized text."""
        # Call the listen method to open the mic and grab audio
        audio = self.recognizer_tools.listen()
        
        try:
            # Recognize the speech using Google's free web API
            text = self.recognizer_tools.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            
        except sr.UnknownValueError:
            # This happens if the audio was just background noise or static
            print("Sorry, I couldn't understand the audio.")
            
        except sr.RequestException as e:
            # This happens if your internet connection is down or the API fails
            print(f"Could not request results from the recognition service; {e}")

if __name__ == "__main__":
    # Quick test to run the assistant
    assistant = Assistant()
    assistant.run()