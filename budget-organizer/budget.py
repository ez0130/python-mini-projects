import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
import json
import ast


# create the root window
root = tk.Tk()
root.title('Budget')
root.resizable(True, True)
root.geometry('600x400')



def read_excel_file():
    global df2
    filetypes = (
        ('excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    budget = pd.read_excel(filename)
    

    keywords = ['date', 'description', 'amount']
    results = pd.DataFrame({})  
    budget.dropna(inplace = True)
    df1 = budget
    #budget.iloc[0].values
    headers = df1.iloc[0]
    df  = pd.DataFrame(df1.values[1:], columns=headers)
    df2 = pd.concat([df["Date"], df["Description"],df["Category"] ,df["Amount"]],  axis=1)

def keyword_add():
    x = 1
    y = str(E3.get()) +'  ' + Lb1.get((Lb1.curselection()))
    Lb2.insert(x, y )
    dsc_cat[E3.get()] = Lb1.get((Lb1.curselection()))
    E3.delete(0, 'end')
    save_list_json()
       
def delete_keyword():
    idx = Lb2.curselection()
    k = (str(Lb2.get(idx)).split(' '))[0]
    dsc_cat.pop(k)
    Lb2.delete(idx)
    save_list_json()
 
canvas3 = tk.Canvas(width=200, height=20)  # open file button
canvas4 = tk.Canvas(width=200, height=100) # Listbox L1
canvas6 = tk.Canvas(width=200, height=100) # scroll bar 
canvas7 = tk.Canvas(width=200, height=20) # save button

canvas3.place(x=250, y=0)
canvas4.place(x=30, y=150)
canvas6.place(x=250, y=50)
canvas7.place(x=350, y = 00)

# Description key add part
canvas1 = tk.Canvas(width=200, height=30) 
canvas1.place(x=20, y=20)
E3 = tk.Entry(canvas1, width = 15)
E3.place(x=0, y = 10)
B1 = tk.Button(canvas1, text="Add", command = keyword_add)
B1.place(x=100, y = 10)

Lb1 = tk.Listbox(canvas4)
Lb1.pack()

def add_category():
    global x
    x = 1
    Lb1.insert(x, E4.get())
    x += 1
    category_list.append(E4.get())
    E4.delete(0, 'end')
    save_category()

def delete_category():
    global x
    x -= 1
    idx = Lb1.curselection()
    if idx:
        category_list.pop(Lb1.get(idx))
        Lb1.delete(idx)
        save_category() 
    
    
E4 = tk.Entry(canvas4, width = 12)
E4.pack() 
B4 = tk.Button(canvas4, text='Add', command = add_category)
B5 = tk.Button(canvas4, text='Delete', command = delete_category)
B4.pack()
B5.pack()


scrollbar = tk.Scrollbar(canvas6)
scrollbar.pack(side="right")
Lb2 = tk.Listbox(canvas6, yscrollcommand = scrollbar.set )
scrollbar.config(command=canvas6.yview)
Lb2.pack()

B2 = tk.Button(canvas6, text= "delete", command = delete_keyword)
B2.pack()



# open button
open_button = ttk.Button(canvas3, text='Open a File', command=read_excel_file())
open_button.pack(expand=True)
'''
def motion(event):
  print("%s, %s" % (event.x, event.y))
  return
root.bind('<Button-1>', motion)
'''

# keeping the keyword list and options
try: 
    with open("keyword.json", "r") as f:
        dsc_cat = json.load(f)
        for key in dsc_cat:
                x = 1
                y = key +'  ' + dsc_cat[key]
                Lb2.insert(x, y )
                x += 1
    with open("category.txt", 'r') as f:
        contents = f.read()
        category_list = ast.literal_eval(contents)
        for x in category_list:
            a = 1
            Lb1.insert(a, x)
            a += 1
except:
    category_list = []
    dsc_cat = dict()
 
def save_file():
    for key in dsc_cat:
        mask = df2['Description'].str.contains(key)    
        df2.loc[mask, "Category"] = dsc_cat[key]
    print(df2.head(10))
    save_category()
    save_list_json()
    
  
    file_path = fd.asksaveasfilename(defaultextension='.xlsx', filetypes=[('excel', '*.xlsx'), ('All Files', '*.*')])
   
    if file_path:
        df2.to_excel(file_path, index=False)
        print(f'File saved to {file_path}')
    else:
        print('File save cancelled')


def save_list_json():
    with open("keyword.json", "w") as f:
        f.write(json.dumps(dsc_cat))
        print('List saved')
    for key in dsc_cat:
        mask = df2['Description'].str.contains(key)    
        df2.loc[mask, "Category"] = dsc_cat[key]

def save_category():
    with open("category.txt", 'w') as f:
        f.write(str(category_list))


B3 = tk.Button(canvas7, text="Save", command = lambda: (save_file(), save_list_json()))
B3.pack()

root.update()

# run the application
root.mainloop()
