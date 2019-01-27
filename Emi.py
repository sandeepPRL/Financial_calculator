# loan_amount=200000
# time=5
# intrest_rate=15
# def emi_cal(p,n,r):
#     n=n*12
#     print(n)
#     r=r/(12*100)
#     print(r)
#     emi_cal=(p*r*pow(1+r,n))/(pow(1+r,n)-1)
#     return emi_cal
# Emi=emi_cal(loan_amount,time,intrest_rate)
# print(Emi)

from tkinter import *
# fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')
fields = ('Loan Amount', 'Tenure(Time)', 'Intrest Rate', 'Total EMI')
def emi_cal(entries):
    p=float(entries['Loan Amount'].get())
    n= float(entries['Tenure(Time)'].get())*12
    # n=n*12
    print(n)
    r=float(entries['Intrest Rate'].get())/(12*100)
    # r=r/(12*100)
    print(r)
    # emi_cal=float(entries['Total EMI'].get())
    emi_cal = (p*r*pow(1+r,n))/(pow(1+r,n)-1)
    entries['Total EMI'].delete(0, END)
    entries['Total EMI'].insert(0, emi_cal)
    print('emi----',emi_cal)
    # return emi_cal

# def monthly_payment(entries):
#    # period rate:
#    r = (float(entries['Annual Rate'].get()) / 100) / 12
#    print("r", r)
#    # principal loan:
#    loan = float(entries['Loan Principle'].get())
#    n =  float(entries['Number of Payments'].get())
#    remaining_loan = float(entries['Remaining Loan'].get())
#    q = (1 + r)** n
#    monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
#    monthly = ("%8.2f" % monthly).strip()
#    entries['Monthly Payment'].delete(0,END)
#    entries['Monthly Payment'].insert(0, monthly )
#    print("Monthly Payment: %f" % float(monthly))

# def final_balance(entries):
#    # period rate:
#    r = (float(entries['Annual Rate'].get()) / 100) / 12
#    print("r", r)
#    # principal loan:
#    loan = float(entries['Loan Principle'].get())
#    n =  float(entries['Number of Payments'].get())
#    q = (1 + r)** n
#    monthly = float(entries['Monthly Payment'].get())
#    q = (1 + r)** n
#    remaining = q * loan  - ( (q - 1) / r) * monthly
#    remaining = ("%8.2f" % remaining).strip()
#    entries['Remaining Loan'].delete(0,END)
#    entries['Remaining Loan'].insert(0, remaining )
#    print("Remaining Loan: %f" % float(remaining))

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Please Click For Total EMI',
          command=(lambda e=ents: emi_cal(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   # b2 = Button(root, text='Monthly Payment',
   #        command=(lambda e=ents: monthly_payment(e)))
   # b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()