import speech_recognition as sr
import config

class SpeechRecognizer:
    def __init__(self):
        """Initializes the SpeechRecognizer with configurations."""
        self.recognizer = sr.Recognizer()
        
        # We still set a baseline pause threshold from config
        self.recognizer.pause_threshold = config.PAUSE_THRESHOLD

    def listen(self):
        """Calibrates for background noise and captures audio with strict limits."""
        with sr.Microphone() as source:
            # 1. Ambient Noise Calibration
            print("Calibrating microphone...")
            # duration="2" satisfies the "wait a couple of seconds" requirement
            self.recognizer.adjust_for_ambient_noise(source, duration=2.0)
            
            # 2. Capture the speech
            print("Listening...")
            
            # timeout: stops if you don't say anything within X seconds
            # phrase_time_limit: stops recording after X seconds of continuous speech
            audio_data = self.recognizer.listen(
                source, 
                timeout=config.LISTENING_TIMEOUT, 
                phrase_time_limit=config.PHRASE_TIME_LIMIT
            )
            return audio_data