from pynput import keyboard
import socket
import numpy
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file2.wav"
audio = pyaudio.PyAudio()



flag = 0

def function2():
    print("Flag Reset!!!")
    global flag
    flag=0

def function1():
    print("Inside")
    
    
def on_press(key):
    try:
        global flag
        if(key.char == 'a' and flag == 0):
            flag = 1
            function1()
            print("Yes")
        #print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    function2()
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
