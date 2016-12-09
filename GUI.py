from tkinter import *
import tkinter as ttk
import histogram as hist

class displayGUI(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack()
        Label(self,Text="enter document uuid").grid(row = 0, sticky =W)
        self.docID = Entry(self,width = 30)
        self.docID.pack()
        countryBtn = Button(self,Text="View by country",COMMAND=self.viewByCountry())




    #     master.grid(column=0, row=0, sticky=(N, W, E, S))
    #     master.columnconfigure(0, weight=1)
    #     master.rowconfigure(0, weight=1)
    #
    #     ttk.Label(master, text="Enter valid Document ID").grid(column=1, row=1, sticky=W)
    #     self.docID = ttk.StringVar
    #     docID_entry = ttk.Entry(master, width=20, textvariable=self.docID)
    #     docID_entry.grid(column=2, row=1, sticky=W)
    #
    #     self.docIDSubmit = ttk.Button(master, text="View By Country", command=self.viewByCountry)
    #     self.docIDSubmit.grid(column=1, row=3, sticky=W)
    #     #ttk.Button(mainframe, text="View By Continent", command=lambda :self.viewByContinent(docID.get())).grid(column=2, row=3, sticky=W)
    #     #ttk.Button(mainframe, text="View By Browser", command=lambda :self.viewByBrowser(docID.get())).grid(column=3, row=3, sticky=W)
    #
    #     for child in master.winfo_children(): child.grid_configure(padx=5, pady=5)
    #     docID_entry.focus()
    #
    #
    #
    def viewByCountry(self):
        try:
            value = self.docID.get()
            countryData = ret.getCountryData(value)
            hist.drawCountry(countryData)
        except:ValueError
        pass


    # def viewByContinent(doc_ID):
    #     value = doc_ID
    #
    # def viewByBrowser(doc_ID):
    #     value = doc_ID

root = Tk()
root.geometry("400x200+500+300")
app = displayGUI(root)
root.mainloop()