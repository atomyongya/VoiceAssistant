"""
This include all the path and folder necessary for the system.

"""
import os

class Folder_Directory():
    
    def __init__(self, path):
        self.path = path
    
    def file_Path(self):
        """
        
        """
        
        path = os.listdir(self.path)
        
        return path

# Path of folder where all the English audio data are stored.
english_Audio_Path = "../../1_System_Model/2_English_KM/1_English_Audio_Data/"
english_Audio_Directory_Object = Folder_Directory(english_Audio_Path)
english_Audio_Directory = english_Audio_Directory_Object.file_Path()

# Path of folder where all the Nepali data are stored.
nepali_Mapping_Data = ""


