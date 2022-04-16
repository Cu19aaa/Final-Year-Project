
from tkinter import *
from tkinter import ttk
 
 
 
 
class App(Tk):
    def __init__(self):
        super(App, self).__init__()
 
        self.title("Student Debt Calculator")
        self.minsize(600,400)
        self.wm_iconbitmap("icon.ico")
 
 
        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text = "I Dont Know My Student Debt")
 
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text = "I Know My Total Student Debt")
        tabControl.pack(expand = 1, fill = "both")
 
        self.widgets()
        
    def idontknowit(*args):
        
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
        withinterest = ((totalloan * interest * cduration)/100) + totalloan
        Yearlypayment = withinterest/targetrepayment
        Monthlypayment = Yearlypayment/30
        Weeklypayment = Monthlypayment/7
       
        labeltext.set("£" + str(round(receivedYearly,2)))
        Labeltext.set("£" + str(round(totalloan,2)))
        LAbeltext.set("£" + str(round(withInterest,2)))
        LABeltext.set("£" + str(round(Ypayment,2)))
        LABEltext.set("£" + str(round(Mpayment,2)))
        LABELtext.set("£" + str(round(Wpayment,2)))

    def iknowit(*args):
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

        LabelText.set("£" + str(round(receivedtotal,2)))
        LAbelText.set("£" + str(round(withInterest,2)))
        LABelText.set("£" + str(round(Ypayment,2)))
        LABElText.set("£" + str(round(Mpayment,2)))
        LABELText.set("£" + str(round(Wpayment,2)))
 
    def widgets(self):

        
        labelFrame = LabelFrame(self.tab1, text = "I Dont know My Total Student Debt")
        labelFrame.grid(column = 0, row = 0, padx = 8, pady = 4)
 
        label = Label(labelFrame, text = "Tuition fee loan:")
        label.grid(column = 0, row = 0, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 0)
        
        label2 = Label(labelFrame, text = "Maintainace fee loan:")
        label2.grid(column = 0, row = 1, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column= 1, row = 1)

        label3 = Label(labelFrame, text = "Course Duration(In years):")
        label3.grid(column = 0, row = 2, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 2)

        label4 = Label(labelFrame, text = "Interest Rate:")
        label4.grid(column = 0, row = 3, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 3)

        label5 = Label(labelFrame, text = "Target Repayment(In Years):")
        label5.grid(column = 0, row = 4, sticky = 'W')
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 4)

        #myButton = Button(text = "compute", command =idontknowit)
        #myButton.grid(column =1, row = 5)
        #myButton.pack()

        label6 = Label(labelFrame, text = "RESULTS:", font = 'times 20 bold')
        label6.grid(column = 0, row = 6, sticky = 'W')

        label7 = Label(labelFrame, text = "You Received Yearly:", font = 'times 16 ')
        label7.grid(column = 0, row = 7, sticky = 'W')

        label8 = Label(labelFrame, text = "You Received A Total Of:", font = 'times 16 ')
        label8.grid(column = 0, row = 8, sticky = 'W')

        label9 = Label(labelFrame, text = "With Interest Its Worth:", font = 'times 16 ')
        label9.grid(column = 0, row = 9, sticky = 'W')

        label10 = Label(labelFrame, text = "NOTE: Student loans are written of after 30 years!", font='times 18 bold')
        label10.grid(column = 0, row = 10, sticky = 'W')

        label11 = Label(labelFrame, text = "To Repay Within Target Time", font = 'times 16 ')
        label11.grid(column = 0, row = 11, sticky = 'W')

        label12 = Label(labelFrame, text = "Make A Yearly Payment Of:", font = 'times 16 ')
        label12.grid(column = 0, row = 12, sticky = 'W')

        label13 = Label(labelFrame, text = "Make A Monthly Payment Of:", font = 'times 16 ')
        label13.grid(column = 0, row = 13, sticky = 'W')

        label14 = Label(labelFrame, text = "Make A Weekly Payment Of:", font = 'times 16 ')
        label14.grid(column = 0, row = 14, sticky = 'W')

        #labelText = StringVar()
        #labelText.set("Payment")
        #label15 = Label(app, textvariable=labelText, height=4)
        #label15.grid(row=7, column=1)

        

 

################################################################################################################################################################################################       

        
        
        labelFrame2 = LabelFrame(self.tab2, text = "Second Tab")
        labelFrame2.grid(column = 0, row = 0, padx = 8, pady = 4)
        
        label = Label(labelFrame2, text="Enter Yearly Student Loan Allowance:")
        label.grid(column=0, row=0, sticky='W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=0)
        
        label2 = Label(labelFrame2, text="Course Duration:")
        label2.grid(column=0, row=1, sticky = 'W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=1)

        label3 = Label(labelFrame2, text="Interest Rate:")
        label3.grid(column=0, row=2, sticky = 'W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=2)

        label4 = Label(labelFrame2, text="Target Repayment(In Years):")
        label4.grid(column=0, row=3, sticky = 'W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=3)

        label5 = Label(labelFrame2, text="RESULTS:", font = 'times 20 bold')
        label5.grid(column=0, row=5, sticky = 'W')

        label6 = Label(labelFrame2, text = "You Received A Total Of:", font = 'times 16')
        label6.grid(column = 0, row = 6, sticky = 'W')

        label7 = Label(labelFrame2, text = 'With Interest It Is Worth:', font = 'times 16')
        label7.grid(column = 0, row = 7,sticky = 'W')

        label8 = Label(labelFrame2, text = 'NOTE: Student loans are written of after 30 years!', font = 'times 20 bold')
        label8.grid(column = 0, row = 8, sticky = 'W')

        label9 = Label(labelFrame2, text = 'To repay within target time', font = 'times 16')
        label9.grid(column = 0, row = 9,sticky = 'W')

        label10 = Label(labelFrame2, text = 'Make A Yearly Payment Of:', font = 'times 16')
        label10.grid(column = 0, row = 10,sticky = 'W')

        label11 = Label(labelFrame2, text = 'Make A Monthly Payment Of:', font = 'times 16')
        label11.grid(column = 0, row = 11,sticky = 'W')

        label12 = Label(labelFrame2, text = 'Make A Weekly Payment Of:', font = 'times 16')
        label12.grid(column = 0, row = 12,sticky = 'W')

        
      

       

        
 
 
 
 
 
 
 
 
#app.config(menu=menubar)
app = App()
app.mainloop()
