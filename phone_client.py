import socket
import pyaudio
import wave
import threading
import keyboard
import time
from pynput.keyboard import Key, Listener

class Phone:

    #Initializations for Microphone.
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 10240
    WAVE_OUTPUT_FILENAME = "file_client.wav"
    audio = pyaudio.PyAudio()

    #Socket Initializations.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_ADDRESS = "192.168.225.30"
    PORT_NUMBER = 8177

    #frames storage variables
    sending_frames = []
    receiving_frames = []

    #Initializations for creating of 'wav' files.
##    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
##    waveFile.setnchannels(CHANNELS)
##    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
##    waveFile.setframerate(RATE)

    #determines either sending or recieving
    flag = -1       #0 - Recording / 1 - Recieving / '-1' - Nothing

    #def _init_(self):

        #Socket Exception Handling incase of refused connection


    def on_key_press(self, key):
        #Verify that only 'G' is pressed otherwise do nothing.
        if(keyboard.is_pressed('space')):
            self.flag = 0
            print('Space Pressed')

        #This method sets the flag to 0. Indicating 'recording' starts.

    def on_key_release(self, key):
        pass
        #Verify that only 'G' is released otherwise do nothing.
##        if(keyboard.is_pressed('x')):
##            self.flag = 1
##            print('X pressed')
##            #Send the frames recorded in 'recorder_thread()' method over the socket.
##            size = len(self.sending_frames)
##
##            for i in range(size):
##                self.connected_socket.send(self.sending_frames[i])
##
##            print("\nframes sent")
##
##            self.sending_frames = [] #Emptying the sending_frames.
        #send a special symbol over socket to trigger receiver code.

    def keyboard_listener_thread(self):
        #Implement Keyboard Listener for listening to the 'G' key.
        with Listener(
               on_press=self.on_key_press,
               on_release=self.on_key_release) as listener:
               listener.join()


    def main(self):

        #Socket Connection code. Server Side.
        print("Connecting to Server...")
        self.connected_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))
        print("\nConnection to Server successful")

        #Setting up and Starting Keyboard Listener thread
        thread = threading.Thread(target=self.keyboard_listener_thread)
        thread.start()
        

        while True:
            time.sleep(.10)
            print('Do Nothing')

            self.sending_frames = []
            #Recorder Code
            while(self.flag == 0):
                #time.sleep(.10)


                print('\nRecording...')
                #Recorder Code Initializations.
                stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                    rate=self.RATE, input=True,
                                    frames_per_buffer=self.CHUNK)
                #Code to capture the microphone using stream.read() method
                data = stream.read(self.CHUNK)
                self.sending_frames.append(data)
                if(keyboard.is_pressed('x')):
                    print('X pressed')
                    #Send the frames recorded in 'recorder_thread()' method over the socket.
                    size = len(self.sending_frames)
                    
                    for i in range(size):
                        self.connected_socket.send(self.sending_frames[i])

                    print("\nframes sent")

                    self.sending_frames = [] #Emptying the sending_frames.

                    self.flag = -1
                stream.close()

            self.sending_frames = []

            self.connected_socket.setblocking(0)
            #reciever code
            while(True):

                try:
                    text = self.connected_socket.recv(10)
                    self.receiving_frames = []
                    self.receiving_frames.append(text)
                except socket.error:
                    break

                
                
                
                print("\n Recieving")
                #Receive all the frames using a while loop, breaking
                    #it when empty byte is recieved.
                while True:
                    try:
                        text = self.connected_socket.recv(1024)
                        self.receiving_frames.append(text)
                    except socket.error:
                        break                        

                #Make a 'wav' files using the recieved frames and save it.
                waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
                waveFile.setnchannels(self.CHANNELS)
                waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
                waveFile.setframerate(self.RATE)

                waveFile.writeframes(b''.join(self.receiving_frames))
                waveFile.close()

                #Play the saved 'wav' file.
                wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'rb')
                p = pyaudio.PyAudio()

                stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                                channels = wf.getnchannels(),
                                rate=wf.getframerate(),
                                output = True)

                data = wf.readframes(self.CHUNK)

                print("\nPlaying")
                while data != '':
                    stream.write(data)
                    data = wf.readframes(self.CHUNK)

                stream.close()
                p.terminate()
                wf.close()
                flag = -1
            self.connected_socket.setblocking(1)


        connected_socket.close()
        server_socket.close()

if __name__ == '__main__':
    Phone().main()
