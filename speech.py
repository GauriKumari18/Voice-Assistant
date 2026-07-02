import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        """Initializes the SpeechRecognizer by creating a Recognizer instance."""
        # Create the Recognizer object and store it as an instance variable
        self.recognizer = sr.Recognizer()

    def listen(self):
        """Opens the microphone and prints a listening message."""
        # Open the default microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")
            
            # This captures the audio data from the microphone
            audio_data = self.recognizer.listen(source)
            return audio_data