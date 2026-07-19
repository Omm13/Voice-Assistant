import sounddevice as sd
import numpy as np


device_id = 2
samplerate = 44100

print("Speak now...")


with sd.InputStream(
    samplerate=samplerate,
    channels=1,
    device=device_id,
    dtype="int16"
) as stream:

    for i in range(50):

        audio, overflow = stream.read(1024)

        volume = np.abs(audio).mean()

        print("Volume:", int(volume))