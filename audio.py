import pyaudio
import wave

def generate_audio(chunk=1024, fs=44100, save_audio=False):
    
    """_summary_
    fs: sampling rate
    Returns:
        _type_: _description_
    """
    
    channels=2
    sample_format = pyaudio.paInt16  # 16 bits per sample
    filename = "output.wav"


    audio = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    stop = False
    while not stop:
        data = stream.read(chunk)
        frames.append(data)

        # Check for stop condition
        # Here, we check if the user has typed "stop" and pressed enter
        if len(frames) % (fs // chunk) == 0:
            user_input = input("Press enter to continue recording, or type 'stop' to stop recording.")
            if user_input.lower() == "stop":
                stop = True

    print("Finished recording.")

    # Stop and close microphone stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio object
    audio.terminate()

    print('Finished recording')
    if save_audio:
    # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
    
    return frames
    
generate_audio(save_audio=True)
