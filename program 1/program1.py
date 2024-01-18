import tkinter as tk
import ttkbootstrap as ttk

#fucntions
def convertCm_to_mm():
    sizeCm = inputBoxInt.get()
    sizeMm = sizeCm * 10
    outputString.set(sizeMm)

#gui widgets
#window frame
parent = ttk.Window(themename="darkly")
parent.title("Convert CM to MM")
parent.geometry("600x250")

#Frame header
titleLabel = ttk.Label(master=parent, text="Centimeter to Milimeter Converter", font="Georgia 22 bold")
titleLabel.pack()

#Input box frame
inputFrame = ttk.Frame(master=parent)
inputLabel = ttk.Label(master=inputFrame, text="Enter size in cm:", font="Calibri 18")

inputBoxInt = ttk.IntVar()
inputBox = ttk.Entry(master=inputFrame, textvariable=inputBoxInt)

convertBtn = ttk.Button(master=inputFrame, text="Convert",command=convertCm_to_mm)

outputString = ttk.StringVar()
outputLabel = ttk.Label(master=parent, 
text="sizeMm", font="Calibri 18", textvariable=outputString)

inputFrame.pack(pady="20")
inputLabel.pack()
inputBox.pack(side="left")
convertBtn.pack(side= "right", padx="10")
outputLabel.pack()

parent.mainloop()