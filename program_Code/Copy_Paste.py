
        # # def user_Input_Voice():
        # #     """
            
        # #     """
            
        # #     user_Input_Label = Label(main_Body, text="Output", width=20, height=2)
        # #     user_Input_Label.grid(row=2)

        
        # # def language_After_Selection(select_language):
        # #     """output_Label = Label(main_Body, text=selected)
        # #         output_Labele.grid()
            
        # #     """
            
        # #     selected_Language = select_Language.get()
            
             
        # #     if selected_Language == "Nepali":
        # #         """
        # #         selected_Language equal to Nepali Language (Call object of nepali_Object)
                
        # #         """
                
        # #         print("Nepali Langague")
        # #         user_Input_Voice()
                
            
        # #     elif selected_Language == "English":
        # #         """
        # #         selected langage equal to English Language (Call object of english_Object)
                
        # #         """
        # #         # object1 = main.english_Object
        # #         # object1.main()
        # #         print("English Langague")
                
        # #     else:
        # #         print("No langauge Selected.")
                
        # # user_Input_Voice()
        
        
        
        
        
        
        
        
        
        
        #  """
        # Making prediction using english model we create.

        # :param fps: frame per second.
        # :param duaration : Record time duration.
        # :param filename : audio path.
        # :param mapping_Data : Loding the data to compare with our real time audio.
        # """

        # fps = 44100
        # duration = 1
        # filename = "prediction.wav"
        # data = self.crossponding_Word()
        # mapping_Data = data["mappings"]
        
        # print("Prediction Started: ")
        # while True:
            
        #     """
        #     :param myrecording :  Audio to predict real time user voice.
        #     :param prediction :  Prediction of real time audio voice.
        #     :param predicted_index : Hold the max prediction value of our model.
        #     :param predicted_keyword : Text word with which our voice will get compared. 
        #     """
        #     try:
        #         # Real time audio recording.  
        #         print("Say Now: ")
        #         myrecording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
        #         sd.wait()
        #         write(filename, fps, myrecording)
                
        #         # Loading the recorded file using librosa.
        #         signal, sample_rate = librosa.load(filename)
                
        #         # Extracting the MFCC feature of an audio
        #         mfcc = librosa.feature.mfcc(signal, sample_rate, n_mfcc=13, hop_length=512, n_fft=2048)
                
        #         # Making prediction and comparing our audio mfcc with the mfcc of train audio data
        #         prediction = english_Model_Path.predict(tf.expand_dims(mfcc.T, axis=0))
                
        #         # Finding max prediction value and mapping with the index of mapping_Data from json. 
        #         predicted_index = np.argmax(prediction)
        #         predicted_keyword = mapping_Data[predicted_index]
        #         print(predicted_keyword)
                
        #         # To stop the audio record.
        #         stop = input("Enter S or s to stop: ")
        #         if stop == "s" or stop == "S":
        #             break

        #         else:
        #             continue
                    
        #     except Exception as error:
        #         print(error)
        #         continue