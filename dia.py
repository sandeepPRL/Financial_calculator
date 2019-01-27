from tkinter import *
x=10
y=50
def emi_cal(entries):
    entries['X'].delete(0, END)
    entries['X'].insert(0, x)
    # emi_cal=float(entries['Total EMI'].get())
    entries['Y'].delete(0, END)
    entries['Y'].insert(0, y)
    entries['LAT'].delete(0, END)
    entries['LAT'].insert(0, y)
    entries['LOG'].delete(0, END)
    entries['LOG'].insert(0, y)

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
    fields = ('X','Y','LAT','LOG')
    ents = makeform(root, fields)
    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Please Click For Total EMI',
          command=(lambda e=ents: emi_cal(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    # b2 = Button(root, text='Monthly Payment',
    #        command=(lambda e=ents: monthly_payment(e)))
    # b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
