###### IMPORTS ###################
import threading
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3
import main_Backend


#### SETTING UP TEXT TO SPEECH ###
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 155)
engine.startLoop(False)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

##### CONSTANTS ################
fs = 22050
seconds = 2
model_path = "WakeWord_Model_Save/WWD.h5"
model = load_model(model_path)

##### LISTENING THREAD #########
def listener():
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction_thread(mfcc_processed)

def voice_thread():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()

##### PREDICTION THREAD #############
def prediction(y):
    try:
        prediction = model.predict(np.expand_dims(y, axis=0))
        if prediction[:, 1] > 0.96:
            if engine._inLoop:
                engine.endLoop()

            speak("Hello Atom, What can I do for you?")
            main_Backend.numa_System_Run()
            
    except Exception as error:
        print("Sorry atom, there is something wrong")
        

    time.sleep(0.1)

def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()

# def main_Backend_thread():
#     main_Backend_Threading = threading.Thread(target=main_Backend.numa_System_Run(), name="BackendFunction")
#     main_Backend_Threading.start()

if __name__ == '__main__':
        voice_thread()


