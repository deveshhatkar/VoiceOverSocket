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
    IP_ADDRESS = "localhost"
    PORT_NUMBER = 4040

    #Sound Frames storage variables
    frames = []

    #Initializations for creating of 'wav' files
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)

    #determines either sending or recieving
    flag = 0

##    def connect_as_server(self):
##        try:
##            self.connecting_socket.bind((self.IP_ADDRESS, self.PORT_NUMBER))
##            self.connecting_socket.listen(1)
##            self.connected_socket = self.connecting_socket.accept()
##            print("\nThis is a server")
##        except:
##            print("\nThis is a client")
##            
##        
##
##    def connect_as_client(self):
##        try:
##            connected_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))
##            print("\nThis is a client")
##        except:
##            print("\nThis is a server")

    def __init__(self):

        #Socket Connection code
        self.server_socket.bind((self.IP_ADDRESS, self.PORT_NUMBER))
        self.server_socket.listen(5)
        (self.connected_socket, address) = self.server_socket.accept()
##        thread_server = threading.Thread(self.connect_as_server())
##        thread_client = threading.Thread(self.connect_as_client())
##
##        thread_client.start()
##        thread_server.start()                
        print("This is Server")
        print("Hello World!")

    def main(self):
        obj = Phone()
    

if __name__ == '__main__':
    Phone().main()
