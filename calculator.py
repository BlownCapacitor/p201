from tkinter import *
window=Tk()

window.title('Interest Calculator')
window.geometry("500x600")
window.configure(bg='lightgreen')

  
def calculate_interest():
    pC = principle.get()
    p = float(pC.replace(",", ""))
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    ro = int(rounder.get())
    if ro == "no":
        interest = i
    else:
        interest = round(i, int(ro))
    result.destroy()
    
    message=Label(result_frame,text="Interest: " + str(interest), bg = "lightblue", font=("Calibri", 12), width=55)
    message.place(x=20,y=40)
    message.pack()

def calculate_compound_interest():
    pC = principle.get()
    p = float(pC.replace(",", ""))
    r = float(rate.get())
    t = float(time.get())
    i = (p*(1+r/100)**t)
    ro = rounder.get()
    if ro == "no":
        interest = i
    else:
        interest = round(i-p, int(ro))
    result.destroy()
    
    message=Label(result_frame,text="Interest: " + str(interest), bg = "lightblue", font=("Calibri", 12), width=55)
    message.place(x=20,y=40)
    message.pack()

app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lightblue", font=("Arial", 25),bd=5)
app_label.place(x=20, y=20)

principle_label=Label(window, text="Principle: ", fg = "black", bg = "lightblue", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=92)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=200, y=92)

rate_label=Label(window, text="Rate of Interest in %: ", fg = "black", bg = "lightblue", font=("Calibri", 12))
rate_label.place(x=20, y=140)

rate=Entry(window, text="", bd=2, width=10)
rate.place(x=200, y=142)

time_label=Label(window, text="Years: ", fg = "black", bg = "lightblue", font=("Calibri", 12))
time_label.place(x=20, y=185)

time=Entry(window, text="", bd=2, width=10)
time.place(x=200, y=187)

rounder_label=Label(window, text="Round: ", fg = "black", bg = "lightblue", font=("Calibri", 10))
rounder_label.place(x=20, y=215)

rounder=Entry(window, text="", bd=2, width=10)
rounder.place(x=200, y=215)

calculate=Button(window,text="CALCULATE SIMPLE",fg = "black", bg = "lightblue",bd=4,command=calculate_interest)
calculate.place(x=20,y=250)

calculateC=Button(window,text="CALCULATE COMPOUND",fg = "black", bg = "lightblue",bd=4,command=calculate_compound_interest)
calculateC.place(x=250,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightblue", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result=Label(result_frame,text="", bg = "lightblue", font=("Calibri", 12), width=55)
result.place(x=20,y=20)
result.pack()


warning_f = LabelFrame(window,text="", bg = "magenta")
warning_f.pack(padx=1, pady=1)
warning_f.place(x=280,y=140)
warning = Label(warning_f, text="Rounding: \n Set rounding to 2 for \n most currencies. \n If calculating interest \n on expensive crypto, \n rounding = 'no'.", font=("Calibri", 8))
warning.place(x=250, y = 187)
warning.pack()
window.mainloop()
