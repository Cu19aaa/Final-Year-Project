import tkinter as tk
from tkinter import ttk

class Tab_Contol:
  def __init__(self, root):
      root = tk.Tk()
      root.title("Student debt calculator")
      root.geometry('500x200+200+200')
      
      
      tabControl = ttk.Notebook(root)
      
      self.tab1 = ttk.Frame(tabControl)
      tabControl.add(tab1, text="I know my complete student debt")
      tabControl.pack(expand=1, fill="both")
      
      MainFrame = Frame(self.tab1 , bd=10, width = 1350, height=700, bg="gainboro", relief= RIDGE)
      MainFrame.grid()
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

      resultsLabel = Label(app, text='RESULTS:', font='times 18 bold')
      resultsLabel.grid(row=9, column=0)

      totalgivenLabel =Label(app, text='Total Loan Received:')
      totalgivenLabel.grid(row=10, column=0)

      itsworthLabel = Label(app, text='Its worth in todays money is:')
      itsworthLabel.grid(row=11, column=0)


      paymentLabel = Label(app, text='Your monthly payment will be ')
      paymentLabel.grid(row=17, column=0)

      labelText = StringVar()
      labelText.set("Payment")
      label1 = Label(app, textvariable=labelText, height=4)
      label1.grid(row=10, column=7)


      calculateButton = Button(app, text="Compute", width=20, command=calculateLabel)
      calculateButton.grid(row=9,column=1)


     
     MainFrame = Frame(self.tab2 , bd=10, width = 1350, height=700, bg="gainboro", relief= RIDGE)
     MainFrame.grid()
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

     label5 = Label(app, text='Target Repayment')
     label5.grid(row=4)

     loanTerm = IntVar()
     loanTerm.set("")
     loanTerm = Entry(app, textvariable=loanTerm)
     loanTerm.grid(row=4, column=1)

     BreakdownLabel = Label(app, text='The break down of your payment is as follows')
     BreakdownLabel.grid(row=8, column=0)

     paymentLabel = Label(app, text='Your monthly payment will be ')
     paymentLabel.grid(row=9, column=0)

     weeklyLabel = Label(app, text='Your weekly payment will be ')
     weeklyLabel.grid(row=10, column=0)

     labelText = StringVar()
     labelText.set("Payment")
     label1 = Label(app, textvariable=labelText, height=4)
     label1.grid(row=8, column=1)


     calculateButton = Button(app, text="calculate", width=20, command=calculateLabel)
     calculateButton.grid(row=10,column=1)

if __name__=='main__':
    root =Tk()
    application =Tab_Control(root)
    root.mainloop()
