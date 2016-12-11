from tkinter import *
import tkinter as tk
import firstTask as ft
import secondTask as st
import thirdTask as tt

def viewByCountry():
    ID = docID_entry.get()
    ft.taskOne(ID, 1)

def viewByContinent():
    ID = docID_entry.get()
    ft.taskOne(ID, 2)

def viewTopReaders():
    returned_DF = tt.taskThree()
    for index, value in returned_DF.iterrows():
        reader = value['visitor_uuid'] + '\t' + ':' + '\t' + str(value['event_readtime'])
        listBox.insert('end', reader)

def viewByBrowser():
    st.taskTwo()

root = tk.Tk()
root.title("This is the Main User GUI")

docID_Label = Label(root,text="Enter document ID")
docID_entry = Entry(root, width=30)
docID_Label.grid(row=0,sticky=W)
docID_entry.grid(row=0,column=1,sticky=['W','E'])

countryButton = Button(root,text='View by country',command= viewByCountry)
countryButton.grid(row=2,sticky=W)
continentButton = Button(root,text='View by continent',command= viewByContinent)
continentButton.grid(row=2,column=1)
browserButton = Button(root,text='View top browsers Used', command= viewByBrowser)
browserButton.grid(row=3,sticky=W)
listBox = Listbox(root,width=38,height=11)
listBox.grid(row=4,column=1,sticky=W)
topReadersBtn = Button(root,text='Show top 10 avid readers',command= viewTopReaders)
topReadersBtn.grid(row=4,sticky=W)

root.mainloop()

