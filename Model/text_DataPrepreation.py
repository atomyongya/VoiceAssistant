# import librarys
from nltk.tokenize import sent_tokenize
import re


# To read the text file
path_RawText_Data = "Text_Data/data_1.txt"

with open(path_RawText_Data, 'r') as f:
    data = f.read()
    
paragraphs = data.split("\n\n") # Since ebook also seperated by 2 \n

# Cleaning special characters and splitting sentence using NLTK
paragraph_sentence_list = []
for paragraph in paragraphs:
    paragraph = paragraph.replace("\n", " ")
    paragraph = paragraph.replace("-", "")
    paragraph = re.sub(r'[^a-zA-Z0–9_*.,?!åäöèÅÄÖÈÉçëË]', ' ', paragraph)
    paragraph_sentence_list.append(sent_tokenize(paragraph))

# Saving the aeneas text based file so that we can use force aligments
text = ""
count = 0
path_AeneasData = "Text_Data/Aeneas_"
for paragraph in paragraph_sentence_list:
    if " ".join(paragraph).isupper():
        with open(path_AeneasData + str(count) + ".txt", "w") as fw:
            fw.write(text)
            text = ""
            count += 1
            text += "\n".join(paragraph)
            text += "\n\n"
            
    elif "End of the Project Gutenberg EBook" in " ".join(paragraph):
        break
    
    else:
        text += "\n".join(paragraph)
        text += "\n\n"