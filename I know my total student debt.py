from tkinter import *

def closeApp():
    app.quit()


def calculateLabel(*args):
    loan = float(loanAmount.get())
    targetrepayment = int(loanTerm.get())
    yearlyinterest = float(loanInterest.get())
    interest = (yearlyinterest/100)/12
    term = int(loanTime.get())
    totaldebt = loan * (interest/(1-(1+interest) ** (-term)))    
    labelText.set("$" + str(round(total,2)))

app = Tk()
app.title("Student debt calculator")
app.geometry('600x600')
app.bind("<Return>",calculateLabel)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

label2 = Label(app, text='Enter Yearly Student Finance Allowance')
label2.grid(row=1)

loanAmount = IntVar()
loanAmount.set("")
loanAmount = Entry(app, textvariable=loanAmount)
loanAmount.focus_set()
loanAmount.grid(row=1, column=1)

label3 = Label(app, text='Enter time spent in university')
label3.grid(row=2)

loanTime = IntVar()
loanTime.set("")
loanTime = Entry(app, textvariable=loanTime)
loanTime.focus_set()
loanTime.grid(row=2, column=1)


label4 = Label(app, text='Interest Rate')
label4.grid(row=3)

loanInterest = IntVar()
loanInterest.set("")
loanInterest = Entry(app, textvariable=loanAmount)
loanInterest.grid(row=3, column=1)

label5 = Label(app, text='Target Repayment(In Years)')
label5.grid(row=4)

loanTerm = IntVar()
loanTerm.set("")
loanTerm = Entry(app, textvariable=loanTerm)
loanTerm.grid(row=4, column=1)

resultsLabel = Label(app, text='RESULTS:', font='times 20 bold')
resultsLabel.grid(row=8, column=0)

tLabel = Label(app, text='You received a total of:')
tLabel.grid(row=10, column=0)

itsworthLabel = Label(app, text='With interest it is worth')
itsworthLabel.grid(row=11, column=0)

noteLabel = Label(app, text='NOTE: Student loans are written of after 30 years!', font='times 18 bold')
noteLabel.grid(row = 12, column = 1)

tlabel = Label(app, text='->To repay within target time', font='times 16')
tlabel.grid(row = 13, column=0)

mpaylabel = Label(app, text='You make a monthly payment of:', font='times 16')
mpaylabel.grid(row = 14, column=0)

wpayLabel = Label(app, text='You make a weekly payment of:', font='times 16')
wpayLabel.grid(row = 15, column=0)

ypayLabel = Label(app, text='You make a yearly payment of: ', font='times 16')
ypayLabel.grid(row=16, column=0)

#paymentLabel = Label(app, text='Your monthly payment will be ')
#paymentLabel.grid(row=9, column=0)

#weeklyLabel = Label(app, text='Your weekly payment will be ')
#weeklyLabel.grid(row=10, column=0)

labelText = StringVar()
labelText.set("Payment")
label1 = Label(app, textvariable=labelText, height=4)
label1.grid(row=10, column=1)


calculateButton = Button(app, text="COMPUTE", width=20, command=calculateLabel)
calculateButton.grid(row=8,column=1)

app.config(menu=menubar)

app.mainloop()
