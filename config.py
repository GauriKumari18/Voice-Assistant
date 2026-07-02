# Language settings (e.g., 'en-US', 'en-IN', 'es-ES')
LANGUAGE = "en-US"

# The minimum audio decibel level considered as speech. 
# Lower = more sensitive; higher = ignores more background noise.
ENERGY_THRESHOLD = 300  

# Seconds of silence that marks the end of a phrase
PAUSE_THRESHOLD = 0.8  

# Maximum seconds it will wait for you to start speaking before timing out
LISTENING_TIMEOUT = 5.0  

# Maximum seconds it will let you speak in a single phrase
PHRASE_TIME_LIMIT = 10.0