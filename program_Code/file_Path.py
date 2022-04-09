"""
This file include path of the file and folder which is used by the system.
"""
from tensorflow.keras.models import load_model


chrome_Path = "/usr/bin/google-chrome"

folder_path = "/home/atomyongya"

save_Audio_Path = "user_Audio/prediction.wav"

save_Awarded_Audio = "user_Audio/awarded_Audio/"

wake_Word_Sound_Effect = "user_Audio/wake_Word_Sound_Effect/wake_Word_Sound_Effect.wav"

icon_Path = "image/icon.png"

"""
:var nepali_Model_Path (String) : Path of Nepali Langague Keyword detection model. 
:var english_Model_Path (String) : Path of English Language keyword detection model.
"""

# Model Path
nepali_Model_Path = ""
english_Model_Path = load_model("/home/atomyongya/Documents/Herald/Final Year Project/VoiceAssistant(Numa)/VoiceAssistant/_system_Model/2_English_KM/3_English_Model_File/english_Model.h5")
