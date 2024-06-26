# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def record():
	# Sampling frequency
	freq = 44100

	# Recording duration
	duration = 5

	# Start recorder with the given values 
	# of duration and sample frequency
	recording = sd.rec(int(duration * freq), 
					samplerate=freq, channels=2)

	# Record audio for the given number of seconds
	print('Listening...')
	sd.wait()
	print('Stop speaking.')

	# This will convert the NumPy array to an audio
	# file with the given sampling frequency
	write("./testing scripts/recordings/recording0.wav", freq, recording)