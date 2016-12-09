import argparse
import tkinter as tk
import GUI as gui
import sys

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('typeID', help='The deliverable you wish to see(2-4)',type=int)
#     parser.add_argument('doctID', help='ID of the document whose histogram you wish to see')
#
#     args = parser.parse_args()

def runGUI():
    root = tk.Tk()
    interface = gui.displayGUI(root,'GUI')
    interface.mainloop()


if __name__ == '__main__':
    runGUI()
