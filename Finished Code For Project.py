from tkinter import *
from tkinter import messagebox

def closeApp():
    app.quit()
    
    
        
def calculateLabel(*args):
    tloan = int(tuitionLoan.get()) #input of yearly tuition loan
    if tloan == 0:  #check to ensure tutition loan field is not set to 0
        messagebox.showerror(title = 'error', message='Please input an amount. Tuition loan amount cannot be 0')
    mloan = int(maintainanceLoan.get())  #Input of yearly maintainance loan
    cduration = int(courseDuration.get()) #input for time in university
    if cduration == 0:            #check to make sure field is not set to 0
        messagebox.showerror(title = 'error', message='Please input an amount. Course duration cannot be 0')
    yearlyinterest = float(loanInterest.get())          #input for interest rate
    targetrepayment = int(loanTime.get())                #input for goal repayment period
    interest = yearlyinterest 

    receivedYearly = tloan + mloan
    totalloan = (tloan + mloan) * cduration
    withInterest = ((totalloan * interest * cduration)/100) + totalloan
    Ypayment = withInterest/targetrepayment
    Mpayment = Ypayment/30
    Wpayment = Mpayment/7  
    Received_yearly.set("£" + str(round(receivedYearly,2)))
    Total_loan.set("£" + str(round(totalloan,2)))
    With_interest.set("£" + str(round(withInterest,2)))
    Yearly_payment.set("£" + str(round(Ypayment,2)))
    Monthly_payment.set("£" + str(round(Mpayment,2)))
    Weekly_payment.set("£" + str(round(Wpayment,2)))
    
#initializing the tk import
app = Tk()
#title description
app.title("Student Debt Calculator")
#screen size description
app.geometry('700x700')
app.bind("<Return>",calculateLabel)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

#creation of tuition fee label
label2 = Label(app, text='Tuition fee loan(per year)')
label2.grid(row=1)

#input label for tuition fee
tuitionLoan = IntVar()
tuitionLoan.set("")
tuitionLoan = Entry(app, textvariable=tuitionLoan)
tuitionLoan.focus_set()
tuitionLoan.grid(row=1, column=1)

#creation of maintainace fee label
label3 = Label(app, text='Maintainace loan(per year)')
label3.grid(row=2)

#input label for maintainace fee
maintainanceLoan = IntVar()
maintainanceLoan.set("")
maintainanceLoan = Entry(app, textvariable=maintainanceLoan)
maintainanceLoan.focus_set()
maintainanceLoan.grid(row=2, column=1)

#creation of course duration label
label4 = Label(app, text='Course Duration(In Years)')
label4.grid(row=3)

#input label for course duration
courseDuration = IntVar()
courseDuration.set("")
courseDuration = Entry(app, textvariable=courseDuration)
courseDuration.grid(row=3, column=1)

#creation of interest rate label
label5 = Label(app, text='Interest rate')
label5.grid(row=4)

#input label for interest rate
loanInterest = IntVar()
loanInterest.set("")
loanInterest = Entry(app, textvariable=loanInterest)
loanInterest.grid(row=4, column=1)

label6 = Label(app, text='Target Repayment Time(In Years)')
label6.grid(row=5)

loanTime = IntVar()
loanTime.set("")
loanTime = Entry(app, textvariable=loanTime)
loanTime.grid(row=5, column=1)

resultsLabel = Label(app, text='RESULTS:', font='times 20 bold')
resultsLabel.grid(row=9, column=0)

yearlygivenLabel =Label(app, text='You received yearly:', font='times 16')
yearlygivenLabel.grid(row=10, column=0)

totalgivenlabel = Label(app, text='You received a total of:', font='times 16')
totalgivenlabel.grid(row=11, column=0)

itsworthLabel = Label(app, text='With interest it is worth:', font='times 16')
itsworthLabel.grid(row=12, column=0)

noteLabel = Label(app, text='NOTE: Student loans are written of after 30 years!', font='times 18 bold')
noteLabel.grid(row = 13, column = 1)

tlabel = Label(app, text='->To repay within target time', font='times 16')
tlabel.grid(row = 14, column=0)

ypayLabel = Label(app, text='You make a yearly payment of: ', font='times 16')
ypayLabel.grid(row=15, column=0)

mpaylabel = Label(app, text='You make a monthly payment of:', font='times 16')
mpaylabel.grid(row = 16, column=0)

wpayLabel = Label(app, text='You make a weekly payment of:', font='times 16')
wpayLabel.grid(row = 17, column=0)



Received_yearly = StringVar()
Received_yearly.set("Payment")
label8 = Label(app, textvariable=Received_yearly, height=4)
label8.grid(row=10, column=1)

Total_loan = StringVar()
Total_loan.set("Payment")
Label7 = Label(app, textvariable=Total_loan, height=4)
Label7.grid(row=11, column=1)

With_interest = StringVar()
With_interest.set("Payment")
label9 = Label(app, textvariable=With_interest, height=4)
label9.grid(row=12, column=1)

Yearly_payment = StringVar()
Yearly_payment.set("Payment")
LAbel10 = Label(app, textvariable=Yearly_payment, height=4)
LAbel10.grid(row=15, column=1)

Monthly_payment = StringVar()
Monthly_payment.set("Payment")
LABel11 = Label(app, textvariable=Monthly_payment, height=4)
LABel11.grid(row=16, column=1)

Weekly_payment = StringVar()
Weekly_payment.set("Payment")
LABEl12 = Label(app, textvariable=Weekly_payment, height=4)
LABEl12.grid(row=17, column=1)


calculateButton = Button(app, text="COMPUTE", width=20, command=calculateLabel)
calculateButton.grid(row=9,column=1)
  



app.config(menu=menubar)

app.mainloop()
