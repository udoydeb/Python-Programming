
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty('rate', 150)  # Speed percent (can go over 100)

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Text to speak
text = "Hello Udoy! Welcome to Python Programming. Let's learn together and have fun with coding!"

# Speak the text
engine.say(text)
engine.runAndWait()
