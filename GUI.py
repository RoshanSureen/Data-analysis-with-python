from tkinter import *
import tkinter as tk
import firstTask as ft

root = tk.Tk()
root.geometry("400x250+500+300")

root.title("This is the Main User GUI")

docID_Label = Label(root,text="Enter document ID")
docID_entry = Entry(root, width=30)
docID_Label.grid(row=0)
docID_entry.grid(row=0,column=1)

def viewByCountry():
    ID = docID_entry.get()
    ft.taskOne(ID,1)

def viewByContinent():
    ID = docID_entry.get()
    ft.taskOne(ID,2)

countryButton = Button(root,text='View by country',command= viewByCountry)
countryButton.grid(row=2)
continentButton = Button(root,text='View by continent',command= viewByContinent)
continentButton.grid(row=2,column=1)

root.mainloop()

