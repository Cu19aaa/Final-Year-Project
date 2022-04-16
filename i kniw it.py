from tkinter import *

def closeApp():
    app.quit()


def calculateLabel(*args):
    loan = float(loanAmount.get())
    if loan == 0:
        messagebox.showerror(title = 'error', message='Please input an amount. Tuition loan amount cannot be 0')
    targetrepayment = int(loanTerm.get())
    yearlyinterest = float(loanInterest.get())
    interest = yearlyinterest
    term = int(loanTime.get())   
    receivedtotal = loan * term
    withInterest = ((loan * interest * term)/100) + receivedtotal
    Ypayment = withInterest/targetrepayment
    Mpayment = Ypayment/30
    Wpayment = Mpayment/7

    Received_total.set("£" + str(round(receivedtotal,2)))
    with_Interest.set("£" + str(round(withInterest,2)))
    Yearly_amount.set("£" + str(round(Ypayment,2)))
    Monthly_amount.set("£" + str(round(Mpayment,2)))
    Weekly_amount.set("£" + str(round(Wpayment,2)))

    
    

app = Tk()
app.title("Student debt calculator")
app.geometry('700x700')
app.bind("<Return>",calculateLabel)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

label2 = Label(app, text='Enter yearly sfe amount')
label2.grid(row=1)

loanAmount = IntVar()
loanAmount.set("")
loanAmount = Entry(app, textvariable=loanAmount)
loanAmount.focus_set()
loanAmount.grid(row=1, column=1)

label3 = Label(app, text='Enter time spent in university(In Years)')
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

timelabel = Label(app, text='->To repay within target time', font='times 16')
timelabel.grid(row = 13, column=0)

ypayLabel = Label(app, text='You make a yearly payment of: ', font='times 16')
ypayLabel.grid(row=16, column=0)

mpaylabel = Label(app, text='You make a monthly payment of:', font='times 16')
mpaylabel.grid(row = 14, column=0)

wpayLabel = Label(app, text='You make a weekly payment of:', font='times 16')
wpayLabel.grid(row = 15, column=0)

Received_total = StringVar()
Received_total.set(" ")
Label1 = Label(app, textvariable=Received_total, height=4)
Label1.grid(row=10, column=1)

with_Interest = StringVar()
with_Interest.set(" ")
label6 = Label(app, textvariable=with_Interest, height=4)
label6.grid(row=11, column=1)

Yearly_amount = StringVar()
Yearly_amount.set(" ")
LAbel7 = Label(app, textvariable=Yearly_amount, height=4)
LAbel7.grid(row=14, column=1)

Monthly_amount = StringVar()
Monthly_amount.set(" ")
LABel8 = Label(app, textvariable=Monthly_amount, height=4)
LABel8.grid(row=15, column=1)

Weekly_amount = StringVar()
Weekly_amount.set(" ")
LABEl9 = Label(app, textvariable=Weekly_amount, height=4)
LABEl9.grid(row=16, column=1)


calculateButton = Button(app, text="COMPUTE", width=20, command=calculateLabel)
calculateButton.grid(row=8,column=1)

app.config(menu=menubar)

app.mainloop()
