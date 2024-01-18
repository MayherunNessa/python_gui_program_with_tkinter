## These are the problems I faced in this program and how I solved them

1. At first, I used the 'font' kwargs in every widgets in the input box frame section. However, it isn't a property of all of the widgets it seems, as it didn't run and showed a error instead.

2. I wanted to set the width and height for the widgets, but the width and height property doesn't seem to work.

3. The input taken from the entry needs to be integer. And getting the input directly from the entry was not efficient.
So, I used tk.IntVar and set the textvaribale to it (for the inputbox). This way the input is set as a integer in the inputBoxInt.

4. I was having trouble setting the output value. To set the output string, I used .set method on the outputString variable which was overwriting the output label value

5. For further ui customization, I imported ttkbootstrap as ttk and replaced it with tk.

