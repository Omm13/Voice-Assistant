import sounddevice as sd
from scipy.io.wavfile import write

frequency = 44100
duration = 5

device_id = 2   # Realtek laptop microphone

print("Using device:")
print(sd.query_devices(device_id))

print("Recording started... Speak now")

recording = sd.rec(
    int(duration * frequency),
    samplerate=frequency,
    channels=1,
    device=device_id
)

sd.wait()

write(
    "recording.wav",
    frequency,
    recording
)

print("Recording saved")