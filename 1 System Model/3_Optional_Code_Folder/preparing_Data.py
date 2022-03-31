import librosa
import os
import json
import IPython.display as ipd

# path of dataset audio and json file to store 
audio_Data_Path = "Audio_Data/english_Audio_Data"
json_path = "English_AM/json_Folder/english.json"
sample_to_consider = 22050 # Librosa default load of audio sample rate

def prepare_dataset(audio_Data_Path, json_path, n_mfcc=13, hop_length=512, n_fft=2048):
    #data dictionary
    data = {
        "mappings": [],
        "labels": [],
        "MFCCs": [],
        "files": []
    }
    
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(audio_Data_Path)):
        try:
            # we need to ensure that we're not at root level
            if dirpath is not audio_Data_Path:
                category = dirpath.split("/")[-1]
                data["mappings"].append(category)
                # loop through all the filename and extract MFCCs
                for f in filenames:
                    # Get file path
                    file_path = os.path.join(dirpath, f)
                    
                    # Load audio file
                    signal, sample_rate = librosa.load(file_path)
                    
                    # ensure the audio file is at least one second
                    # if len(signal) >= sample_to_consider:
                        # enforce 1 second long signal
                    signal = signal[:sample_to_consider]
                    # extract the MFCCs
                    MFCCs = librosa.feature.mfcc(y=signal, n_mfcc=n_mfcc,
                                                    hop_length=hop_length,
                                                    n_fft=n_fft)
                    
                    # store data
                    data["labels"].append(i-1)
                    data["MFCCs"].append(MFCCs.T.tolist())
                    data["files"].append(file_path) 
                    print(f"{file_path}: {i-1}")
            
        except Exception as error:
            continue    
                    
    # store in json file
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)
        
if __name__ == "__main__":
    prepare_dataset(audio_Data_Path, json_path)
                
                
