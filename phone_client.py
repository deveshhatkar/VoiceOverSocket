import socket
import pyaudio
import wave
import threading

class Phone:

    #Initialiations for Microphone
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    WAVE_OUTPUT_FILENAME = "file_client.wav"
    audio = pyaudio.PyAudio()

    #Socket Initializations
    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_ADDRESS = "192.168.0.103"
    PORT_NUMBER = 40404

    #Sound Frames storage variables
    frames = []

    #Initializations for creating of 'wav' files
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)

    #determines either sending or recieving
    flag = 0

    def __init__(self):

        #Socket Connection code

        self.connected_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))

        print("This is Client!!!")
        print("Hello World!")

    def main(self):
        print("Hello")
    

if __name__ == '__main__':
    Phone().main()
