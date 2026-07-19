import sounddevice as sd

print(sd.default.device)

print(sd.query_devices(sd.default.device[0]))