# importing libraries
from aeneas.executetask import ExecuteTask
from aeneas.task import Task

# create Task object
config_string = "task_language=eng|is_text_type=plain|os_task_file_format=json"
task = Task(config_string=config_string)    # To work with text it must be a unicode string which is store in config_string 

task.audio_file_path_absolute = "Audio_Data/1.wav"  # Path of audio file
task.text_file_path_absolute = "Text_Data/Aeneas_3.txt"   # path of text file
task.sync_map_file_path_absolute = "Json_Data/Without_Tuned_Data1.json"   # Path to save the output file in json format

# Process Task
ExecuteTask(task).execute()

# Output sync map to file
task.output_sync_map_file()