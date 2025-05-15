import tkinter as tk
import csv
from random import randint




#data loading
words = {}
with open("french_words.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        words.update({row['English']:row['French']})
global keywords; keywords = []

for key in words.keys():
    keywords.append(key)
    




#know words, go back to keywords
def Newword():
    print(keywords)
    number = randint(0, len(keywords))
    global wordtomemorize
    wordtomemorize = keywords[number]
    canvas.itemconfig(label1, text=wordtomemorize, font=("Ariel", 40, "italic") )
    canvas.itemconfig(label2, text=len(keywords))
    print(len(keywords))
    if len(keywords) <= 2:
        studiedall()
        exit()
    keywords.remove(wordtomemorize)
    '''
    Obutton = tk.Button(text = "O", command=lambda: [knowit()]) 
    Xbutton = tk.Button(text = "X", command = notsure())
    Obutton.grid(row= 1, column = 0, pady = 2)
    Xbutton.grid(row =1, column = 1, pady = 2)
    '''

def notsure():
    keywords.append(wordtomemorize)
    answer = words[wordtomemorize]
    print(answer)
    canvas.itemconfig(label1, text=answer, font=("Ariel", 40, "italic") )
    

    #show the button for new word
    
def studiedall():
    label4 = tk.Message(flashcard, "You studied all! Well done!")
    label4.grid(row =0, column = 0, pady = 2)
    
    
    
'''
def refresh(self):
    self.destroy()
    self.__init__()
    flashcard = tk.Tk()
    flashcard.config(padx=50, pady=50, bg="pink")
    flashcard.title("Flash card")
    canvas = tk.Canvas(width=800, height=526)
    Newword()
'''

#make base and design

flashcard = tk.Tk()
flashcard.config(padx=50, pady=50, bg="Grey")
flashcard.title("Flash card")

canvas = tk.Canvas(width=800, height=400)
print(keywords)
number = randint(0, len(keywords))
wordtomemorize = keywords[number]
label1 = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic") )
label2 = canvas.create_text(400,200, text = "", font=("Ariel", 40, "italic") )
keywords.remove(wordtomemorize)
Obutton = tk.Button(text = "O", command=lambda: [Newword()]) 
Xbutton = tk.Button(text = "X", command=lambda: [notsure()])
newbutton = tk.Button(text= "Next", command = Newword() )
newbutton.grid(row =0, column = 3, pady = 2)
Obutton.grid(row= 1, column = 0, pady = 2)
Xbutton.grid(row =1, column = 1, pady = 2)
canvas.config(bg='skyblue', highlightthickness = 0 )
canvas.grid(row=0, column=0, columnspan=2)
number = randint(0, len(keywords))



#show the answer




        

flashcard.mainloop()
