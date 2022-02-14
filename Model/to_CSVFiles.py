from pydub import AudioSegment
import pandas as pd
import json

path_AudioData = "Audio_Data/1.wav"
path_JsonData = "Json_Data/With_Tuned_Data1.json"

# Doing slicing of audio files
audio_Segmentation = AudioSegment.from_wav(path_AudioData)
with open(path_JsonData) as f:
    with_Tuned_Data = json.loads(f.read())
    
# Looping through all the segments, fragments and sentences in With_Tuned_Data1.json file
sentences = []
for fragment in with_Tuned_Data["fragments"]:
    if ((float(fragment['end'])*1000) - float(fragment['begin'])*1000) > 400:
        sentences.append({"audio":audio_Segmentation[float(fragment['begin'])*1000:float(fragment['end'])*1000], "text":fragment['lines'][0]})

# Creating placeholder dataframe 
columns_List = ["filename", "text", "up_votes", "down_votes", "age", "gender", "accent", "duration"]
df = pd.DataFrame(columns=columns_List)


# export audio segment 
for audio_id, sentence in enumerate(sentences):
    text = sentence["text"].lower()
    # sentence["audio"].export("Audio_Data/Audio_Output/audio-" + str(audio_id) + ".wav", format="wav")
    temp_df = pd.DataFrame([{"filename":"audio-" + str(audio_id) + ".wav", "text":text, "up_votes":0, "down_votes":0, "age":0, "gender":"male", "accent":"", "duration":""}], columns=columns_List)
    df = df.append(temp_df)

# Exporting the csv file to the folder 
df.to_csv("CSV_Folder/csv_File-1.csv", index=False)
