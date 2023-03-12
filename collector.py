import pyaudio
import wave
import os
from pydub import AudioSegment
from pydub.utils import make_chunks
# matplotlib

chunk = 1024  # record in chunks of 1024 samples
channels = 2  # number of audio streams
rate = 44100  # number of frames per second (Hz)
sample_format = pyaudio.paInt16  # 16 bits per sample (=2 bytes)
chunk_length = 5000  # 5s


def Collector(seconds, name):

    filename = name + ".wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Start Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks
    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording')

    # save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')  # change
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


# Segmentation
def Segment(name):
    # path = 'C:\\Users\\84628\\PycharmProjects\\pythonProject1'
    # os.chdir(path)
    # folder = 'folder'
    # os.makedirs(folder)
    audiofile = AudioSegment.from_file(name + ".wav", "wav")  # change 1
    chunks = make_chunks(audiofile, chunk_length)

    # for i, Collector.chunk in enumerate(chunks):
    #     # path = (path + "\\" + folder)
    #     # os.chdir(path)
    #     chunk_name = "fragment{0}.wav".format(i+1)  # change 2
    #     print(chunk_name)
    #     chunk.export(chunk_name, format="wav")  # change 3

    for i, chunk in enumerate(chunks):
        chunk_name = ".\\data.\\chunk{0}.wav".format(i)
        print ("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")  # put recording in the same folder and check if the folder exists or not


if __name__ == "__main__":
    Collector(10, "recording")
    Segment("recording")