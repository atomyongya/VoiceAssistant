import IPython.display as ipd

predicted_keyword = ""
filename = ""       
#########################
def award(predicted_keyword, filename): 
    
    # Voice we will save        
    audio = ipd.Audio(filename, autoplay=True)
    return audio
        
    ###########################
def result(predicted_keyword, filename):
    award_Penelty = input("Enter 'enter' keyword for penelty else award: ")

    if award_Penelty == "a" or award_Penelty == "A":
        audio = award()
        audio
        
    else:
        print("Bad word. Give Penelty.")


        