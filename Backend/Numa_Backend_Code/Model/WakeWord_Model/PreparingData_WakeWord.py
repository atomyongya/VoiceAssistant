import sounddevice as sd
from scipy.io.wavfile import write

# To record audio data of wake word
def record_AudioData_WakeWord_Save(path_Save_Audio, n_times=100):
    input("To start recording audio data press Enter: ")
    for i in range(n_times):
        sampleRate_Wakeword = 44100
        record_time_Second = 2
        wakeWord_Recording = sd.rec(int(record_time_Second * sampleRate_Wakeword), samplerate = sampleRate_Wakeword, channels = 2)
        sd.wait()
        write(path_Save_Audio + str(i) + ".wav", sampleRate_Wakeword, wakeWord_Recording)
        input(f"Press to record next or to stop press ctrl + c ({i+1}/{n_times})")
        
# To record background noise 
def record_BackgroundNoise_Save(path_Save_Background, n_times=100):
    input("To start your background sounds press Enter: ")
    for i in range(n_times):
        sampleRate_Background = 44100
        record_time_Second = 2
        background_Recording = sd.rec(int(record_time_Second * sampleRate_Background), samplerate = sampleRate_Background, channels = 2)
        sd.wait()
        write(path_Save_Background+ str(i) + ".wav", sampleRate_Background, background_Recording)
        print(f"Currently on {i + 1}/{n_times} ")
        
# print("Recording the audio for wake word: \n")
# record_AudioData_WakeWord_Save("audioData_WakeWord/")

print("Recording background Noise: \n")
record_BackgroundNoise_Save("Background_Voice_WakeWord/")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            