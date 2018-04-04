import socket
import pyaudio
import wave
import threading

#================================================================================
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
    PORT_NUMBER = 40400

    #Sound Frames storage variables
    sending_frames = []
    receiving_frames = []
    
    #Initializations for creating of 'wav' files
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    #determines either sending or recieving
    flag = 0 # 0-active receiver_thread() / 1-active recorder_thread()

    #----------------Methods-------------------

    def __init__(self):

        #Socket Connection code
        self.connected_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))

    #------------------------------------------

    def on_key_press(key, self):
        #Verify that only 'G' is pressed otherwise do nothing.
        #This method sets the flag to 1. Indicating 'recorder_thread()'
            #becomes active.
        try:
            if(key.char == 'g'):
                self.flag = 1
        except:
            print ("a")
    #------------------------------------------

    def on_key_release(key, self):
        #Verify that only 'G' is released otherwise do nothing.
        if(key.char == 'g'):
        
            #This mehtod sets the flag to 0.
            self.flag = 0
            
            #Send the frames recorded in 'recorder_thread()' method over the socket.
            size = len(self.sending_frames)
            for i in range(size):
                self.connected_socket.send(self.sending_frames[i])

            self.sendding_frames = [] # Emptying the sending_frames

    #-------------------------------------------

    def recorder_thread(self):
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print ("\nrecording...")
        while True:
            while(self.flag == 1):
                #Code to capture the microphone using stream.read() method
                data = stream.read(CHUNK)
                self.sending_frames.append(data)
                

    #-------------------------------------------

    def receiver_thread(self):
        while True:
            self.receiving_frames = [] #Emptying the receiving frames
            while(self.connected_socket.recv(1) != ''):

                #Receive all the frames using a while loop, breaking
                    #it when empty byte is recieved.
                while True:
                    text = self.connected_socket.recv(1024)
                    self.receiving_frames.append(text)
                    if text == '':
                        break                    

                #Make a 'wav' files using the recieved frames and save it.
                self.waveFile.writeframes(b''.join(self.receiving_frames))
                waveFile.close()

                #Play the saved 'wav' file.
                wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'rb')

                p = pyaudio.PyAudio()

                stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                                channels = wf.getchannels(),
                                rate=wf.getframerate(),
                                output = True)

                data = wf.readframes(self.CHUNK)

                while data != '':

                    stream.write(data)
                    data = wf.readframes(self.CHUNK)

                stream.close()
                p.terminate()

    #-------------------------------------------

##    def __del__(self):
##        self.recoder_thread.stop()
##        self.receiver_thread.stop()

    #-------------------------------------------

    def main(self):
        #Create a 'Phone' object.

        #starting the 'recorder_thread()'thread and 'receiver_thread()'thread
        thread1 = threading.Thread(self.recorder_thread)
        thread2 = threading.Thread(self.receiver_thread)

        thread1.start()
        thread2.start()

        #Implement Keyboard Listener for listening to the 'G' key.
        with keyboard.listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
            listener.join()
            
        print("Hello")

#================================================================================
        
if __name__ == '__main__':
    Phone().main()
