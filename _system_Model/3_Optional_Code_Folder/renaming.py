import os

data_Path = "/home/atomyongya/Documents/Herald/Final Year Project/VoiceAssistant(Numa)/VoiceAssistant/1 System Model/2_English_KM/1_English_Audio_Data/youtube  /"
i = int(input("Enter the start number: "))

for old_filename in os.listdir(data_Path):
    if i == 0:
        break
    
    else:
        source = data_Path + old_filename
        new_filename = data_Path + str(i) + ".wav"
        os.rename(source, new_filename)
        
        i = i + 1
        

print(len(os.listdir(data_Path)))
    
    