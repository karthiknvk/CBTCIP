"""
***ROCK PAPER SCISSOR GAME***
Winning Rules as follows:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
"""
import tkinter as tk
from PIL import Image,ImageTk
import random
from tkinter import messagebox

c0='sky blue'
c1='deep sky blue'
c2='DodgerBlue3'
c3='DeepSkyBlue4'
c4='#000000'
c5='white'
c6='green3'
c7='red2'

font1='Comic Sans MS'
font2='Arial'

root=tk.Tk()
root.title("RPS")
root.geometry('1000x700')
root.configure(bg=c4,)

root.grid_columnconfigure(0,weight=1)
for i in range(3):
  if i==1:
    root.grid_rowconfigure(i,weight=3)
  else:
    root.grid_rowconfigure(i,weight=1)


player_score=0
cpu_score=0
cpu_move_image=None
player_move=None

def game_mode(mode):
  global player_score,cpu_score,gmode
  player_score=0
  cpu_score=0
  gmode=mode
  global max_score,frame8_available
  if gmode==5:
    max_score=5
  elif gmode==10:
    max_score=10
  elif gmode=='E':
    max_score=None
  frame8_available=False
  game_play()

def game_play():
  global rockimg,paperimg,scissorimg,frame2,frame4,frame5,rockbutton1,paperbutton1,scissorbutton1,frame6,score_board,frame8,cpu_move_label,status_label,player_move_label,cpu_move_image,your_move_image,frame8_available,frame9,frame2copy,score_label

  if frame2copy:
    frame2copy.destroy()

  rockimg=ImageTk.PhotoImage(Image.open("oldrock.png").resize((125,125)))
  paperimg=ImageTk.PhotoImage(Image.open("oldpaper.png").resize((125,125)))
  scissorimg=ImageTk.PhotoImage(Image.open("oldscissor.png").resize((125,125)))

  #center layer
  frame2=tk.LabelFrame(root,text=None,border=0,bg=c4)
  frame2.grid(row=1,column=0,sticky='ew')
  frame2.grid_columnconfigure(0,weight=1)
  frame2.grid_columnconfigure(1,weight=2)

  #center left layer
  frame4=tk.LabelFrame(frame2,text=None,border=0,bg=c4)
  frame4.grid(row=0,column=0,sticky='ew')
  frame4.grid_rowconfigure(0,weight=1)
  frame4.grid_rowconfigure(1,weight=1)
  frame4.grid_columnconfigure(0,weight=1)

  #center left top layer
  frame5=tk.LabelFrame(frame4,border=0,text=None,bg=c4)
  frame5.grid(row=0,column=0,)
  frame5.grid_rowconfigure(0,weight=1)
  frame5.grid_rowconfigure(1,weight=1)
  frame5.grid_columnconfigure(0,weight=1)
  frame5.grid_columnconfigure(1,weight=1)

  rockbutton1=tk.Button(frame5,image=rockimg,command=lambda:player_move("ROCK"),bg=c4,borderwidth=0,padx=10,pady=10,activebackground='yellow')
  rockbutton1.grid(row=0,padx=10,columnspan=2,pady=20)
  paperbutton1=tk.Button(frame5,image=paperimg,command=lambda:player_move("PAPER"),bg=c4,borderwidth=0,padx=10,pady=10,activebackground='red')
  paperbutton1.grid(row=1,column=0,padx=10,pady=30)
  scissorbutton1=tk.Button(frame5,image=scissorimg,command=lambda:player_move("SCISSOR"),bg=c4,borderwidth=0,padx=10,pady=10,activebackground='green')
  scissorbutton1.grid(row=1,column=1,padx=30,pady=20)

  #center left bottom layer
  frame6=tk.LabelFrame(frame4,border=0,text=None,bg=c4)
  frame6.grid(row=1,column=0,pady=20)
  frame6.grid_columnconfigure(0,weight=1)
  frame6.grid_rowconfigure(0,weight=1)
  score_label=f"CPU {cpu_score} : {player_score} YOU"
  score_board=tk.Label(frame6,text=score_label,borderwidth=5,anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5)
  score_board.grid(pady=10)

  #center right layer
  if frame8_available==False:
    frame8=tk.LabelFrame(frame2,border=0,text=None,padx=50,pady=50,width=50, height=50,bg=c4)
    frame8.grid_propagate(False)
    frame8.grid(row=0,column=1,sticky='news')
    for l in range(4):
      frame8.grid_rowconfigure(l,weight=1)
    frame8.grid_columnconfigure(0,weight=1)
    frame8.grid_columnconfigure(1,weight=2)
    frame8_available=True
    cpu_move_label=tk.Label(frame8,text="CPU",anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5)
    cpu_move_label.grid(row=0,column=0,columnspan=3,padx=0,pady=0,sticky='ew')
    status_label=tk.Label(frame8,text="V/S",anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5,)
    status_label.grid(row=1,column=0,columnspan=3,padx=0,pady=0,sticky='ew')  
    player_move_label=tk.Label(frame8,text="PLAYER",anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5,)
    player_move_label.grid(row=2,column=0,columnspan=3,padx=0,pady=0,sticky='ew')
  
  else:
    if frame8:
      frame8.destroy()
    frame9=tk.LabelFrame(frame2,border=0,text=None,padx=50,pady=50,width=50, height=50,bg=c4)
    frame9.grid_propagate(False)
    frame9.grid(row=0,column=1,sticky='news')
    for m in range(3):
      frame9.grid_rowconfigure(m,weight=1)
    frame9.grid_columnconfigure(0,weight=1)
    frame9.grid_columnconfigure(1,weight=2)

    cpu_move_label=tk.Label(frame9,text="CPU ",anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5)
    cpu_move_label.grid(row=0,column=0,padx=0,pady=0,sticky='ew')
    if cpumove=='ROCK':
        cpu_move_image=tk.Label(frame9,image=rockimg,bg=c4,borderwidth=0,padx=10,pady=10)
    elif cpumove=='PAPER':
        cpu_move_image=tk.Label(frame9,image=paperimg,bg=c4,borderwidth=0,padx=10,pady=10)
    elif cpumove=='SCISSOR':
        cpu_move_image=tk.Label(frame9,image=scissorimg,bg=c4,borderwidth=0,padx=10,pady=10)
    cpu_move_image.grid(row=0,column=1,padx=0,sticky='ew')

    status_label=tk.Label(frame9,text=result,anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5,)
    status_label.grid(row=1,column=0,columnspan=3,padx=0,pady=0,sticky='ew')  

    player_move_label=tk.Label(frame9,text="YOU ",anchor="center",font=(font2,30,'bold'),bg=c4,fg=c5,)
    player_move_label.grid(row=2,column=0,padx=0,pady=0,sticky='ew')
    if yourmove=='ROCK':
        your_move_image=tk.Label(frame9,image=rockimg,bg=c4,borderwidth=0,padx=10,pady=10)
    elif yourmove=='PAPER':
        your_move_image=tk.Label(frame9,image=paperimg,bg=c4,borderwidth=0,padx=10,pady=10)
    elif yourmove=='SCISSOR':
        your_move_image=tk.Label(frame9,image=scissorimg,bg=c4,borderwidth=0,padx=10,pady=10)
    your_move_image.grid(row=2,column=1,padx=0,sticky='ew')

  if player_score==max_score or cpu_score==max_score:
    if player_score==max_score:
      messagebox.showinfo("ROCK PAPER SCISSORS","CONGRATS , YOU WON THE GAME")

    else:
      messagebox.showinfo("ROCK PAPER SCISSORS","SORRY , CPU WON THE GAME")
    
    new_game()
    

def player_move(move):
  global player_move_label,cpu_move_label,status_label,yourmove,cpumove,cpu_score,player_score,result

  player_move_label.destroy()
  status_label.destroy()
  cpu_move_label.destroy()
  score_board.destroy()
  cpu_move_image,your_move_image=None,None
  if cpu_move_image and your_move_image:
    cpu_move_image.destroy()
    your_move_image.destroy()

  yourmove=move
  num=random.random()
  
  if num>0 and num<1/3:
    cpumove='ROCK'
  elif num>1/3 and num<2/3:
    cpumove='PAPER'
  else:
    cpumove='SCISSOR'

  if yourmove=='ROCK':
    if cpumove=='ROCK':
      result='Tie'
    elif cpumove=='PAPER':
      result='Cpu won'
      cpu_score=cpu_score+1
    else:
      result='You won'
      player_score=player_score+1

  elif yourmove=='PAPER':
    if cpumove=='PAPER':
      result='Tie'
    elif cpumove=='SCISSOR':
      result='Cpu won'
      cpu_score=cpu_score+1
    else:
      result='You won'
      player_score=player_score+1

  else:
    if cpumove=='SCISSOR':
      result='Tie'
    elif cpumove=='ROCK':
      result='Cpu won'
      cpu_score=cpu_score+1
    else:
      result='You won'
      player_score=player_score+1

  game_play()

def new_game():
  global rockimg, paperimg, scissorimg, frame2, frame4, frame5, rockbutton1, paperbutton1, scissorbutton1, frame6, score_board, frame8, frame9, cpu_move_label, status_label, player_move_label, cpu_move_image, your_move_image, frame8_available,score_label

  globals_to_destroy = {
        'frame2': frame2,
        'frame4': frame4,
        'frame5': frame5,
        'frame6': frame6,
        'score_board': score_board,
        'frame8': frame8,
        'frame9': frame9,
        'cpu_move_label': cpu_move_label,
        'status_label': status_label,
        'player_move_label': player_move_label,
        'rockbutton1': rockbutton1,
        'paperbutton1': paperbutton1,
        'scissorbutton1': scissorbutton1,


    }

  globals_to_none={
      'rockimg': rockimg,
      'paperimg': paperimg,
      'scissorimg': scissorimg,
      'cpu_move_image': cpu_move_image,
      'your_move_image': your_move_image,
      'frame8_available': frame8_available,
      'score_label':score_label,
    }


  for var_name in globals_to_destroy.keys():
        globals()[var_name].destroy()
  for var_name in globals_to_none.keys():
        globals()[var_name]=None

  frame2copy=tk.LabelFrame(root,text='frame2copy',border=0,bg=c4)
  frame2copy.grid(row=1,column=0,sticky='ew')
  frame2copy.grid_columnconfigure(0,weight=1)
  for l in range(4):
    frame2copy.grid_rowconfigure(l,weight=1)

  game_mode_choose_label=tk.Label(frame2copy,text="CHOOSE MODE",anchor="center",font=(font1,30,'bold'),bg=c4,fg=c1,)
  game_mode_choose_label.grid(row=0,column=0,columnspan=3,padx=0,pady=20,sticky='ew')
  game_mode_button1=tk.Button(frame2copy,text='5 POINTS',command=lambda:game_mode(5),bg=c1,fg=c5,font=(font1,13,'bold'),padx=37,relief='raised',activebackground=c5,activeforeground=c1)
  game_mode_button2=tk.Button(frame2copy,text='10 POINTS',command=lambda:game_mode(10),
  bg=c1,fg=c5,font=(font1,13,'bold'),padx=32,relief='raised',activebackground=c5,activeforeground=c1)
  game_mode_button3=tk.Button(frame2copy,text='UNTIL EXIT',command=lambda:game_mode('E'),bg=c1,fg=c5,font=(font1,13,'bold'),padx=28,relief='raised',activebackground=c5,activeforeground=c1)
  game_mode_button1.grid(row=1,column=0,columnspan=3,pady=20)
  game_mode_button2.grid(row=2,column=0,columnspan=3,pady=20)
  game_mode_button3.grid(row=3,column=0,columnspan=3,pady=20)


def exit_game():
  if gmode=='E':
    if player_score>cpu_score:
      messagebox.showinfo("ROCK PAPER SCISSORS","CONGRATS , YOU WON THE GAME")
    elif player_score<cpu_score:
      messagebox.showinfo("ROCK PAPER SCISSORS","SORRY , CPU WON THE GAME")
    else:
      messagebox.showinfo("ROCK PAPER SCISSORS","GAME TIE")
      
    root.quit()
  else:
    root.quit()
  

#upper layer
frame1=tk.LabelFrame(root,text=None,border=0,bg=c4,)#inside frame
frame1.grid(row=0,column=0,columnspan=3,sticky='ew',)#outside frame
frame1.grid_columnconfigure(0,weight=1)
heading=tk.Label(frame1,text="ROCK PAPER SCISSOR",padx=10,pady=10,font=(font1,55,'bold'),bg=c4,fg=c5)
heading.grid(row=0,padx=10,pady=10)

#middle layer
frame2copy=tk.LabelFrame(root,text='frame2copy',border=0,bg=c4)#inside frame
frame2copy.grid(row=1,column=0,sticky='ew')#outside frame
frame2copy.grid_columnconfigure(0,weight=1)
for l in range(4):
  frame2copy.grid_rowconfigure(l,weight=1)

game_mode_choose_label=tk.Label(frame2copy,text="CHOOSE MODE",anchor="center",font=(font1,30,'bold'),bg=c4,fg=c1,)
game_mode_choose_label.grid(row=0,column=0,columnspan=3,padx=0,pady=20,sticky='ew')
game_mode_button1=tk.Button(frame2copy,text='5 POINTS',command=lambda:game_mode(5),bg=c1,fg=c5,font=(font1,13,'bold'),padx=37,relief='raised',activebackground=c5,activeforeground=c1)
game_mode_button2=tk.Button(frame2copy,text='10 POINTS',command=lambda:game_mode(10),
bg=c1,fg=c5,font=(font1,13,'bold'),padx=32,relief='raised',activebackground=c5,activeforeground=c1)
game_mode_button3=tk.Button(frame2copy,text='UNTIL EXIT',command=lambda:game_mode('E'),bg=c1,fg=c5,font=(font1,13,'bold'),padx=28,relief='raised',activebackground=c5,activeforeground=c1)
game_mode_button1.grid(row=1,column=0,columnspan=3,pady=20)
game_mode_button2.grid(row=2,column=0,columnspan=3,pady=20)
game_mode_button3.grid(row=3,column=0,columnspan=3,pady=20)

#bottom layer
frame3=tk.LabelFrame(root,text=None,border=0,bg=c4)#inside frame
frame3.grid(row=2,column=0,columnspan=3,sticky='ew')#outside frame
for k in range(3):
  frame3.grid_columnconfigure(k,weight=1)

newgame_button=tk.Button(frame3,text='NEW GAME',command=new_game,bg=c6,fg=c5,font=(font1,10,'bold'),padx=50,pady=5,activebackground=c5,activeforeground=c6)
newgame_button.grid(column=0,row=0,padx=10,pady=20,)
exit_button=tk.Button(frame3,text='EXIT',command=exit_game,bg=c7,fg=c5,font=(font1,10,'bold'),padx=80,pady=5,activebackground=c5,activeforeground=c7)
exit_button.grid(column=2,row=0,padx=10,pady=20,)

root.mainloop()


