from tkinter import *

def closeApp():
    app.quit()


def calculateLabel(*args):
    tloan = float(tuitionloan.get())
    mloan = float(maintainanceloan.get())
    cduration = int(courseduration.get())
    yearlyinterest = float(loanInterest.get())
    targetrepayment = int(loanTime.get())
    interest = (yearlyinterest/100)/12
    term = int(loanTerm.get())
    #total = loan * (interest/(1-(1+interest) ** (-term)))
    totalloan = (tloan + mloan) * cduration   
    labelText.set("$" + str(round(totalloan,2)))

app = Tk()
app.title("Loan Calculator")
app.geometry('700x500')
app.bind("<Return>",calculateLabel)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

label2 = Label(app, text='Tuition fee loan(per year)')
label2.grid(row=1)

loanAmount = IntVar()
loanAmount.set("")
loanAmount = Entry(app, textvariable=loanAmount)
loanAmount.focus_set()
loanAmount.grid(row=1, column=1)

label3 = Label(app, text='Maintainace loan(per year)')
label3.grid(row=2)

loanAmount = IntVar()
loanAmount.set("")
loanAmount = Entry(app, textvariable=loanAmount)
loanAmount.focus_set()
loanAmount.grid(row=2, column=1)


label4 = Label(app, text='Course Duration')
label4.grid(row=3)

loanInterest = IntVar()
loanInterest.set("")
loanInterest = Entry(app, textvariable=loanAmount)
loanInterest.grid(row=3, column=1)

label5 = Label(app, text='Interest rate')
label5.grid(row=4)

loanTerm = IntVar()
loanTerm.set("")
loanTerm = Entry(app, textvariable=loanTerm)
loanTerm.grid(row=4, column=1)

label6 = Label(app, text='Target Repayment Time')
label6.grid(row=5)

loanTerm = IntVar()
loanTerm.set("")
loanTerm = Entry(app, textvariable=loanTerm)
loanTerm.grid(row=5, column=1)

resultsLabel = Label(app, text='RESULTS:', font='times 20 bold')
resultsLabel.grid(row=9, column=0)

yearlygivenLabel =Label(app, text='You received yearly:', font='times 16')
yearlygivenLabel.grid(row=10, column=0)

totalgivenlabel = Label(app, text='You received a total of:', font='times 16')
totalgivenlabel.grid(row=11, column=0)

itsworthLabel = Label(app, text='Its worth in todays money is:', font='times 16')
itsworthLabel.grid(row=12, column=0)

noteLabel = Label(app, text='NOTE: Student loans are written of after 30 years!', font='times 18 bold')
noteLabel.grid(row = 13, column = 1)

tlabel = Label(app, text='->To repay within target time', font='times 16')
tlabel.grid(row = 14, column=0)

mpaylabel = Label(app, text='You make a monthly payment of:', font='times 16')
mpaylabel.grid(row = 15, column=0)

wpayLabel = Label(app, text='You make a weekly payment of:', font='times 16')
wpayLabel.grid(row = 16, column=0)

ypayLabel = Label(app, text='You make a yearly payment of: ', font='times 16')
ypayLabel.grid(row=17, column=0)

labelText = StringVar()
labelText.set("Payment")
label1 = Label(app, textvariable=labelText, height=4)
label1.grid(row=10, column=1)


calculateButton = Button(app, text="Compute", width=20, command=calculateLabel)
calculateButton.grid(row=9,column=1)
  



app.config(menu=menubar)

app.mainloop()
