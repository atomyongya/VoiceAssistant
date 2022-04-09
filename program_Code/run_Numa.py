"""
Code to execute the program.
"""

# Importing Inbuilt Libarary.
import time
from threading import Thread
from queue import Queue


# Importing other class and function/method.
import file_Path
from front_End_Code import gui_Object
import mostly_Used_Function
import main 

class Run_Numa():
    """
    Run_Numa class contain the the function to execute the application.
    
    """
    
    def __init__(self):
        """
        
        """
        pass
    
    def wake_Word_Detect(self, object_Backend):
        """
        
        """


        print("Say Wake Word: ")
        wake_Word = "numa"
            
        queue_Thread_Prediction = Queue()
            
        thread_Prediction = Thread(target=object_Backend.prediction, args=(queue_Thread_Prediction,))
        thread_Prediction.start()
            
        wake_Word_Prediction = queue_Thread_Prediction.get()
        print(wake_Word_Prediction)
        
            
    def run_Numa():
        """
        run_Numa function contain the code to execute the application.
        """
        
        object_Backend = main.english_Object
        
        wake_Word = "numa"
        
        
        
        mostly_Used_Function.play_Audio(file_Path.wake_Word_Sound_Effect)
        
        

gui_Object.numa_gui()

# object_English = main.english_Object
# object_English.main()

# object_Numa = Run_Numa()
# object_Numa.run_Numa()

