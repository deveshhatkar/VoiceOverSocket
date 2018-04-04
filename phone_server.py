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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    flag = 0 # 0-active recorder thread / 1-active sender thread

    #----------------Methods-------------------

    def __init__(self):

        #Socket Connection code
        self.server_socket.bind(("192.168.0.103", 40404))
        self.server_socket.listen(5)
        (self.connected_socket, address) = self.server_socket.accept()

    #------------------------------------------

    def on_key_press():
        #Verify that only 'G' is pressed otherwise do nothing.

        #This method sets the flag to 1. Indicating 'recorder_thread()'
            #becomes active.

    #------------------------------------------

    def on_key_release():
        #Verify that only 'G' is released otherwise do nothing.
        
        #This mehtod sets the flag to 0.
        
        #Send the frames recorded in 'recorder_thread()' method over the socket.        
        
        #send a special symbol over socket to trigger receiver code.

    #-------------------------------------------

    def recorder_thread():
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print ("\nrecording...")
        while True:
            while(flag == 0):
                #Code to capture the microphone using stream.read() method
                data = stream.read(CHUNK)
                self.frames.append(data)
                

    #-------------------------------------------

    def receiver_thread():
        while True:
            while("Check if the special symbol has arrived over the socket"):

                #Receive all the frames using a while loop, breaking
                    #it when empty byte is recieved.

                #Make a 'wav' files using the recieved frames and save it.

                #Play the saved 'wav' file.

    #-------------------------------------------

    def main(self):
        print("Hello")
        
if __name__ == '__main__':
    Phone().main()
