"""
CREATING PAYMENT RECEIPT
Creating payment receipts is a pretty common task, be it an e-commerce website or any local store for that matter.
Here, you have to create our own transaction receipts just by using python. We would be using reportlab to generate the PDFs. Generally, it comes as a built-in package but sometimes it might not be present too. If it is not present, then simply type the following in your terminal
"""

import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime,webbrowser

c0='SpringGreen4'
c1='SpringGreen2'
c4='#000000'
c5='white'
c6='green3'
c7='red2'
font1='Arial'
font2='Times-Roman'

root=tk.Tk()
root.title("PAYMENT RECEIPT")
root.geometry('1000x700')
root.configure(bg=c1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=5)
root.grid_columnconfigure(0,weight=1)
global itemdetailsdict,row_num,col_num
row_num=0
col_num=0

itemlist = ['Bread', 'Jam', 'Nutella', 'Egg', 'Milk', 'Juice', 'Butter', 'Cheese', 'Apples', 'Bananas', 'Chicken', 'Coffee',]
itemdetailsdict = {
    'Bread': [10,0],'Jam': [12,0],'Nutella': [25,0],'Milk': [15,0],'Egg': [3,0],'Juice': [15,0],'Butter': [8,0],'Cheese': [20,0],'Apples': [5,0],'Bananas': [6,0],'Chicken': [50,0],'Coffee': [5,0],
}
itemcount=len(itemlist)

def itemchanges(symbol,item):
  count=itemdetailsdict[item][1]
  if count==0 and symbol=='-':
      exit
  elif count==99 and symbol=='+':
      exit
  elif symbol=='-':
      count=count-1
      itemdetailsdict[item][1]=count
      display_items(itemdetailsdict)
  else:
      count=count+1
      itemdetailsdict[item][1]=count
      display_items(itemdetailsdict)

def display_items(itemdetailsdict):
  row_num=0
  col_num=0
  for item in itemdetailsdict.keys():
    tk.Label(frame3,text=itemdetailsdict[item][1],padx=5,pady=1,width=2,font=(font1,15,'bold'),bg=c1,fg=c4,).grid(row=row_num,column=col_num+2,sticky='news',pady=4)
    row_num=row_num+1
    if row_num<(itemcount//2):
      continue
    else:
      row_num=0
      col_num=4

def gen_bill_pdf(name,mob,total_bill):
  global billname
  current_time=datetime.datetime.now().strftime("%d %B %Y %H_%M_%S")
  billname=f'{name.upper()} {current_time}.pdf'

  """
  a point is a unit of measurement equivalent to 1/72 of an inch.
  Width: 8.5*72=612
  Height:11*72=792
  """
  c = canvas.Canvas(billname, pagesize=letter)
  width, height = letter
    
  c.setFont(font2,30)
  y=height-60
  c.drawCentredString(width/2,y,text="BILL")
  
  c.setFont(font2,15)
  y=y-40
  c.drawString(50, y, "CUSTOMER NAME")
  c.drawRightString(width-50, y, name.upper())
  c.drawString(50, y-20, "MOBILE NUMBER")
  c.drawRightString(width-50, y-20, mob)

  y = y-60
  c.drawCentredString(width/2, y, "Items Purchased")

  y=y-40
  c.drawString(50, y, f"ITEM")
  c.drawRightString(width-180, y, f"PRICE")
  c.drawRightString(width-115, y, f"COUNT")
  c.drawRightString(width-50, y, f"TOTAL")
  y=y-30
  for item in itemdetailsdict.keys():
    if itemdetailsdict[item][1]==0:
      continue
    else:
      c.drawString(50, y, f"{item}")
      c.drawRightString(width-180, y, f"{itemdetailsdict[item][0]}")
      c.drawRightString(width-115, y, f"${itemdetailsdict[item][1]}")
      c.drawRightString(width-50, y, f"${itemdetailsdict[item][0]*itemdetailsdict[item][1]}")
      y=y-20

  y=y-40
  c.setFont(font2,20)
  c.drawString(50, y, f"TOTAL AMOUNT")
  c.drawRightString(width-50, y, f"${total_bill}")

  c.showPage()
  c.save()  
  return 


def print_bill(name_entry,mob_entry):
  global billname
  name=name_entry.get()
  mob=mob_entry.get()

  if name=='' or mob=='':
    messagebox.showwarning("WARNING","DETAILS CAN'T BE EMPTY")
    return
  elif len(mob)!=10:
    messagebox.showwarning("MOBILE NO. WARNING","ENTER PROPER NUMBER") 
    return
  elif not mob.isdigit():
    messagebox.showwarning("MOBILE NO. WARNING","ENTER PROPER NUMBER")
    return
  for subname in name.split():
    if not subname.isalpha():
      messagebox.showwarning("NAME WARNING","ENTER PROPER NAME")
      return

  global itemdetailsdict
  bill=0
  total_bill=0
  for item in itemdetailsdict.keys():
    bill=itemdetailsdict[item][0]*itemdetailsdict[item][1]
    total_bill=total_bill+bill

  gen_bill_pdf(name,mob,total_bill)

  for item in itemdetailsdict.keys():
      itemdetailsdict[item][1]=0
  
  print("BIll = ",total_bill)
  message_text=f"BILL PRINTED SUCCESSFULLY\nBILL = {total_bill}\nNAME = {name} \nMOB= {mob}"
  webbrowser.open(billname)
  messagebox.showinfo("BILL", message_text)
  
  name_entry.delete(0,tk.END)
  mob_entry.delete(0,tk.END)
  row_num=0
  col_num=0
  for item in itemdetailsdict.keys():
    tk.Label(frame3,text=itemdetailsdict[item][1],padx=5,pady=1,width=2,font=(font1,15,'bold'),bg=c1,fg=c4,).grid(row=row_num,column=col_num+2,sticky='news',pady=4)
    row_num=row_num+1
    if row_num<(itemcount//2):
      continue
    else:
      row_num=0
      col_num=4


frame1=tk.LabelFrame(root,border=0,bg=c1)
frame1.grid(row=0,column=0,)
frame1.grid_columnconfigure(0,weight=1)
heading=tk.Label(frame1,text="GROCERY",padx=10,pady=10,font=(font1,55,'bold'),bg=c1,fg=c4)
heading.grid(row=0,padx=10,pady=10,sticky='ew')

frame2=tk.LabelFrame(root,border=0,bg=c1)
frame2.grid(row=1,column=0,sticky='ew')
frame2.grid_columnconfigure(0,weight=5)
frame2.grid_columnconfigure(1,weight=2)


frame3=tk.LabelFrame(frame2,border=0,bg=c1,height=500,width=300)
frame3.grid(column=0,row=0,sticky='news')
frame3.grid_propagate(False)
for i in range(8):
  if i%4==0:
    frame3.grid_columnconfigure(i,weight=3)
  else:
    frame3.grid_columnconfigure(i,weight=1)
for j in range(itemcount//2):
  frame3.grid_rowconfigure(j,weight=1)


for item in itemdetailsdict.keys():
  itemtext=f"{item}  (${itemdetailsdict[item][0]})"
  tk.Label(frame3,text=itemtext,padx=5,pady=1,font=(font1,15,'bold'),bg=c1,fg=c4,).grid(row=row_num,column=col_num,sticky='news',pady=4)
  tk.Button(frame3,text='-',bg=c4,fg=c1,font=(font1,25,'bold'),pady=0,padx=0,width=1,height=1,command=lambda i=item:itemchanges('-',i),anchor='center').grid(row=row_num,column=col_num+1,pady=25,padx=9,sticky='ew')
  tk.Label(frame3,text=itemdetailsdict[item][1],padx=5,pady=1,width=2,font=(font1,15,'bold'),bg=c1,fg=c4,).grid(row=row_num,column=col_num+2,sticky='news',pady=4)
  tk.Button(frame3,text='+',bg=c4,fg=c1,font=(font1,25,'bold'),pady=0,padx=0,width=1,height=1,command=lambda i=item:itemchanges('+',i),anchor='center').grid(row=row_num,column=col_num+3,pady=25,padx=9,sticky='ew')
  row_num=row_num+1
  if row_num<(itemcount//2):
    continue
  else:
    row_num=0
    col_num=4

frame4=tk.LabelFrame(frame2,border=0,bg=c1,height=500)
frame4.grid(column=1,row=0,sticky='news',pady=40)
frame4.grid_columnconfigure(0,weight=1)
for z in range(6):
  frame4.grid_rowconfigure(z,weight=1)
frame4.grid_rowconfigure(6,weight=6)  

tk.Label(frame4,text="ENTER DETAILS",padx=10,pady=10,font=(font1,20,'bold'),fg=c4,bg=c1).grid(row=1,column=0,sticky='ew')
tk.Label(frame4,text="NAME",padx=10,pady=10,font=(font1,15,'bold'),fg=c4,bg=c1).grid(row=2,column=0,columnspan=1)
name_entry=tk.Entry(frame4,text="ENTER NAME",font=(font1,15,'bold'),bg=c5,fg=c4)
name_entry.grid(row=3,column=0,pady=5)
tk.Label(frame4,text="MOBILE NUMBER",padx=10,pady=10,font=(font1,15,'bold'),fg=c4,bg=c1).grid(row=4,column=0,columnspan=1)
mob_number=tk.Entry(frame4,font=(font1,15,'bold'),bg=c5,fg=c4)
mob_number.grid(row=5,column=0,)


tk.Button(frame4,text="PRINT BILL",bg=c4,fg=c1,command=lambda:print_bill(name_entry,mob_number),anchor='center',padx=30,pady=10).grid(row=6,column=0,pady=10)

root.mainloop()