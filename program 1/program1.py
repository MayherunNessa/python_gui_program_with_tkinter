import tkinter as tk
from tkinter import ttk

sizeCm = sizeMm = None

#fucntions
def convertCm_to_mm():
    sizeCm = inputBox.get()
    

#gui widgets
#window frame
parent = tk.Tk()
parent.title("Convert CM to MM")
parent.geometry("600x250")

#Frame header
titleLabel = tk.Label(master=parent, text="Centimeter to Milimeter Converter", font="Georgia 22 bold")
titleLabel.pack()

#Input box frame
inputFrame = tk.Frame(master=parent)
inputLabel = tk.Label(master=inputFrame, text="Enter size in cm:", font="Calibri 18")
inputBox = tk.Entry(master=inputFrame)
convertBtn = tk.Button(master=inputFrame, text="Convert",command=convertCm_to_mm)
outputLabel = tk.Label(master=parent, text="output in mm", font="Calibri 18")

inputFrame.pack(pady="20")
inputLabel.pack()
inputBox.pack(side="left")
convertBtn.pack(side= "right", padx="10")
outputLabel.pack()

parent.mainloop()