import os 
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sample = "Background_Voice_WakeWord/1.wav"
data, sample_rate = librosa.load(sample)

plt.title("Wave form")
librosa.display.waveplot(data, sr=sample_rate)
plt.show()

mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
print("Shape of mfcc: ", mfccs.shape)

plt.title("MFCC")
librosa.display.specshow(mfccs, sr=sample_rate, x_axis="time")
plt.show()

all_data = [] # final data use for tranning and testing

data_path = {
    0: ["Background_Voice_WakeWord/" + file_path for file_path in os.listdir("Background_Voice_WakeWord/")],
    1: ["audioData_WakeWord/" + file_path for file_path in os.listdir("audioData_WakeWord/")],
}

for class_label, list_of_files in data_path.items():
    for single_file in list_of_files:
        data, sample_rate = librosa.load(single_file)
        mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
        mfcc_processed = np.mean(mfccs.T, axis = 0)
        all_data.append([mfcc_processed, class_label])

    print(f"Info: Successfully preprocessed class label {class_label}")
    
df = pd.DataFrame(all_data, columns=["features", "class_label"])
df.to_pickle("DataSet_Folder/audioData_WakeWord.csv")