import pyaudio
import wave
import audioop
import sys

sys.path.append("external/tts")
from external.tts.models.tacotron2 import Tacotron2Wave
import torchaudio
import mishkal.tashkeel

from tashkeel import tashkeel

vocalizer = mishkal.tashkeel.TashkeelClass()
model_tts = Tacotron2Wave('pretrained/tacotron2_ar_adv.pth')
model_tts = model_tts.cuda()

def record_audio(chunk=1024, fs=44100, save_audio=False, audio_name="output"):
    
    """_summary_
    THRESHOLD: controls the threshold of to decide if a frame is a silent frame
    fs: sampling rate
    Returns:
        _type_: _description_
    """
    
    channels=2
    sample_format = pyaudio.paInt16  # 16 bits per sample
    filename = f"{audio_name}.wav"
    THRESHOLD = 1000  # Adjust this value as needed


    audio = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = audio.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    silence_frames = 0
    while silence_frames < 100:  # Adjust this value as needed
        data = stream.read(chunk)
        frames.append(data)

        # Check if audio input is below threshold value
        rms = audioop.rms(data, 2)
        if rms < THRESHOLD:
            silence_frames += 1
        else:
            silence_frames = 0
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
    
def generate_audio(text, filename):
    text = vocalizer.tashkeel(text)
    wave = model_tts.tts(text)
    torchaudio.save(f"{filename}.wav", wave.unsqueeze(0), 22050)
    return 200