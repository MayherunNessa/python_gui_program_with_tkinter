import tkinter as tk


#fucntions
def convertCm_to_mm():
    sizeCm = inputBoxInt.get()
    sizeMm = sizeCm * 10
    outputString.set(sizeMm)

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

inputBoxInt = tk.IntVar()
inputBox = tk.Entry(master=inputFrame, textvariable=inputBoxInt)

convertBtn = tk.Button(master=inputFrame, text="Convert",command=convertCm_to_mm)

outputString = tk.StringVar()
outputLabel = tk.Label(master=parent, 
text="sizeMm", font="Calibri 18", textvariable=outputString)

inputFrame.pack(pady="20")
inputLabel.pack()
inputBox.pack(side="left")
convertBtn.pack(side= "right", padx="10")
outputLabel.pack()

parent.mainloop()