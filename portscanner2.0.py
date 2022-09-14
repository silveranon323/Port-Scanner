#Developed By SilverAnon
import socket
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("PORT SCANNER")
root.configure( bg = 'black') 
def center_window( width =300 , height = 200):
     #get screen width and height
     screen_width= root.winfo_screenwidth()
     screen_height= root.winfo_screenheight()
     #calculating the position of x and y coordinate
     x = (screen_width/2) - (width/2)
     y = (screen_height/2) - (height/2)
     root.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window()
def port_scanner():   
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     global  a , b
     a = hostvalue.get()
     b = portvalue.get()
     
     if s.connect_ex((a,b)):
          
          messagebox.showerror(" ALERT!" ,  "PORT CLOSE")
     
     else:
          
          messagebox.showinfo(" ALERT!" , "PORT OPEN")
def clear():
     host_entry.delete(0,END)
     port_entry.delete(0, END)
def result():
     
     port_scanner()
     
def exit_func():
     response = messagebox.askokcancel("QUIT" , "Are you sure you want to quit ?")
     if response == 0 :
          pass
     elif response == 1 :
          root.destroy()
          
          
          

h =  Label(root,text= "PORT SCANNER ", font = "comicsanms 20 bold", fg = "red", bg = "black")
h.grid(column =1)
ho_st = Label(root,text= "TARGET", font = "comicsanms 10 bold" , fg = "lightgreen" , bg = "black" )
po_rt  = Label(root,text = "PORT", font = "comicsanms 10 bold" , fg = "lightgreen", bg = "black")
ho_st.grid(row = 1)
po_rt.grid(row = 2)

hostvalue = StringVar()
portvalue = IntVar()


host_entry =Entry(root, textvariable = hostvalue,fg = "black")
port_entry = Entry(root, textvariable = portvalue,fg = "black")
host_entry.config(highlightthickness = 2 , highlightbackground = "lime" , width = 30)
port_entry.config(highlightthickness = 2 , highlightbackground = "lime" , width = 30)
host_entry.grid(row =1 ,  column = 1)
port_entry.grid(row =2, column = 1)

Button(root ,text = "Submit Details ",font = "comicsanms 10 bold ", fg = "red",bg = "yellow",   command = result).grid(padx= 40,pady =10,column=1)
b1 = Button( root , text = "CLEAR " , font = "comicsanms 10 bold ", fg = "red",bg = "yellow", command = clear)
b1.grid(column = 1 , row = 4)
b2 = Button( root , text = "QUIT" , font = "comicsanms 10 bold ", fg = "red",bg = "yellow", command = exit_func)
b2.grid(column = 1 , row =5)
root.mainloop()

