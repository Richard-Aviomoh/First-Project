import tkinter 
from tkinter.constants import END, FALSE, LEFT, SOLID, SUNKEN
from typing import Text
import backup2
from tkinter import Grid, StringVar, messagebox as msg
from functools import partial
import datetime
from tkinter import *
from PIL import ImageTk,Image
from sqlite3.dbapi2 import SQLITE_UPDATE
import sqlite3

def edit_item():
    
    conn3 = sqlite3.connect(dbs)
    cur3 = conn3.cursor()
    try:
        table_view = cur3.execute(
            'SELECT * FROM Teams WHERE Twon = ?', Team_name.get())
        for each in table_view:
            
            name_var.set(each[0])
            amount_var.set(each[1])
            quantity_var.set(each[2])
            costprice_var.set(each[3])
            salesprice_var.set(each[4])
            descriptionV.set(each[5])

            
    except sqlite3.Error:
        msg.showinfo("Error", "Error fetching the selected item for editing!")
    finally:
        cur3.close()

def fixtures():
    frame11.place_forget()
    frame7B.place_forget()
    frame4.place_forget()
    modal.place_forget()
    frame7.place_forget()
    Frame201.place_forget()
    frame7A.place(x = 163, y = 88)
    
    
    
def Results():
    frame7B.place(x = 163, y = 88)
    frame7A.place_forget()
    frame4.place_forget()
    frame11.place_forget()
    modal.place_forget()
    frame7.place_forget()
    Frame201.place_forget()
    
    
    

    
def Bettings():
    frame11.place_forget()
    frame7B.place_forget()
    frame7A.place_forget()
    modal.place_forget()
    frame7.place_forget()
    Frame201.place_forget()
    frame4.place(x = 163, y = 88)
    
def alert(): 
    Frame201.place_forget()
    
def SearchBar():
    frame11.place_forget()
    frame7B.place_forget()
    frame7A.place_forget()
    frame4.place_forget()
    frame7.place_forget()
    Frame201.place_forget()
    modal.place(x = 163, y = 88) 
    
def Standings():
    frame11.place_forget()
    frame7A.place_forget()
    frame4.place_forget()
    frame7B.place_forget()
    frameE.place_forget()
    frameD.place_forget()
    frame1A.place_forget()
    frame1B.place_forget()
    modal.place_forget()
    Frame201.place_forget()
    frame7.place(x = 163, y = 88) 
              

def TopScorers():
    frameD.place(x = 45, y = 50)
    frame1A.place(x = 45, y = 25)
    
    
def TopAssists():
    frameE.place(x = 815, y = 50)
    frame1B.place(x = 815, y = 25)
    
def verify():
    try:
        try:
            
            age = int(entry8.get())
        except ValueError:
            msg.showinfo("Information","PLEASE INPUT A VALID AGE ODE!!")
        except UnboundLocalError:
            pass
        if age <= 17:
           msg.showerror("ERROR", "YOU ARE NOT OLD ENOUGH TO BET")
        elif age >= 100:
             msg.showinfo("Information","OMO YOU DON OLD NOW??")
        else: Frame201.place(x = 250, y = 140) #msg.showinfo("Information", "AGE VERIFICATION SUCCESSFUL. UNFORTUNATELY, THE BETTING PAGE IS CURENTLY UNDER MANTAINANCE")
    except UnboundLocalError:
            pass

dbs = 'Teamx.db'
conn = sqlite3.connect(dbs)
cur = conn.cursor()

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Teams(
    Club VARCHAR(255) ,
    SName VARCHAR(255),
    SCapacity VARCHAR(255),
    CCaptain VARCHAR(255),    
    TWon VARCHAR(255),
    BOdds VARCHAR(255)
    )''')
except sqlite3.OperationalError:
    pass
finally:
    conn.close()
    


window=tkinter.Tk()
window.title("Inventory")
window.config(background="powder blue") 
    
#....................................................................................................................................

frame1 = tkinter.Frame(width=1000, height=2, highlightbackground= "black", highlightthickness=2)

label = tkinter.Label(frame1, width=800, height=2, text = "               UEFA CHAMPIONS LEAGUE", foreground = "white", background = "dark blue", font="times 20",bd=10 )
label.pack()

frame1.pack(side="top")

#...................................................................................................................................
frame2 = tkinter.Frame(width=120, height=700,background = "black")

btn1=tkinter.Button(frame2,text="FIXTURES",padx=17,pady=16,fg="black",font="times 9",bd=5,relief="raised", width=10, command = lambda: fixtures())
btn1.place(x=20, y=50)

btn1=tkinter.Button(frame2,text="RESULTS",padx=17,pady=16,fg="black",font="times 9",bd=5,relief="raised", width=10, command = lambda: Results())
btn1.place(x=20, y=150)

btn1=tkinter.Button(frame2,text="STANDINGS",padx=17,pady=16,fg="black",font="times 9",bd=5,relief="raised", width=10, command = lambda:Standings())
btn1.place(x=20, y=250)

btn1=tkinter.Button(frame2,text="SEARCH BAR",padx=17,pady=16,fg="black",font="times 9",bd=5,relief="raised", width=10, command = lambda:SearchBar())
btn1.place(x=20, y=350)

btn1=tkinter.Button(frame2,text="BETTING",padx=17,pady=16,fg="black",font="times 9",bd=5,relief="raised", width=10, command = lambda:Bettings())
btn1.place(x=20, y=450)



frame2.pack(side="left",padx = 0, pady= 0, ipadx = 20, ipady=20)


#...................................................................................................................................

frame6 = tkinter.Frame(width=3, height = 700, background = "powder blue", highlightbackground= "black", highlightthickness=10)
frame6.pack(side="left")


frame7 = tkinter.Frame(width=1265, height = 700, background = "black" )
frame7A = tkinter.Frame(width=1265, height = 700, background = "black" )
frame7B = tkinter.Frame(width=1265, height = 700, background = "black" )
frameD = tkinter.Frame(width=1000, height = 700, background = "black" )
frameE = tkinter.Frame(width=1000, height = 700, background = "black" )


frame7 = tkinter.Frame(width=1265, height = 700, background = "black" )
my_image = ImageTk.PhotoImage(Image.open("pic5.JPG"))
tity = tkinter.Label(master = frame7, image = my_image, anchor = NW, height = 800, width = 1200, bg= "black" )
tity.place(x=0, y=0, relwidth = 10, relheight = 10)
frame7.place(x=163, y = 88,width= 1265, height = 800 )


#Standings
frameA = tkinter.Frame(frame7)

Label0 = tkinter.Label(master = frame7, text = "     GROUP A    ", height=1, width = 30, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").place(x=435, y = 25)

Label0 = tkinter.Label(master = frameA, text = "Club",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 0, column=0); Label0Q = tkinter.Label(master = frameA, text = "GP",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=1);Label0W = tkinter.Label(master = frameA, text = "Won",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=2);Label0E = tkinter.Label(master = frameA, text = "Drawn",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=3);Label0 = tkinter.Label(master = frameA, text = "Lost",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=4);Label0 = tkinter.Label(master = frameA, text = "Points",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=5)

Label0 = tkinter.Label(master = frameA, text = "Barcelona",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 1, column=0)
Label0Q = tkinter.Label(master = frameA, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=1)
Label0W = tkinter.Label(master = frameA, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=2)
Label0E = tkinter.Label(master = frameA, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=3)
Label0 = tkinter.Label(master = frameA, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=4)
Label0 = tkinter.Label(master = frameA, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=5)

Label0 = tkinter.Label(master = frameA, text = "Arsenal",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 2, column=0)
Label0Q = tkinter.Label(master = frameA, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=1)
Label0W = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=2)
Label0E = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=3)
Label0 = tkinter.Label(master = frameA, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=4)
Label0 = tkinter.Label(master = frameA, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=5)

Label0 = tkinter.Label(master = frameA, text = "Monaco",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 3, column=0)
Label0Q = tkinter.Label(master = frameA, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=1)
Label0W = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=2)
Label0E = tkinter.Label(master = frameA, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=3)
Label0 = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=4)
Label0 = tkinter.Label(master = frameA, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=5)

Label0 = tkinter.Label(master = frameA, text = "AC Milan",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 4, column=0)
Label0Q = tkinter.Label(master = frameA, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=1)
Label0W = tkinter.Label(master = frameA, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=2)
Label0E = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=3)
Label0 = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=4)
Label0 = tkinter.Label(master = frameA, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=5)

frameA.place(x = 360, y = 50)

frameB = tkinter.Frame(frame7)


Label0 = tkinter.Label(master = frame7, text = "     GROUP B    ", height=1, width = 30, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").place(x=425, y = 206)

Label0 = tkinter.Label(master = frameB, text = "Club",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 0, column=0); Label0Q = tkinter.Label(master = frameB, text = "GP",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=1);Label0W = tkinter.Label(master = frameB, text = "Won",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=2);Label0E = tkinter.Label(master = frameB, text = "Drawn",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=3);Label0 = tkinter.Label(master = frameB, text = "Lost",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=4);Label0 = tkinter.Label(master = frameB, text = "Points",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=5)

Label0 = tkinter.Label(master = frameB, text = "Atletico Madrid",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 1, column=0)
Label0Q = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=1)
Label0W = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=2)
Label0E = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=3)
Label0 = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=4)
Label0 = tkinter.Label(master = frameB, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=5)

Label0 = tkinter.Label(master = frameB, text = "Man United",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 2, column=0)
Label0Q = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=1)
Label0W = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=2)
Label0E = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=3)
Label0 = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=4)
Label0 = tkinter.Label(master = frameB, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=5)

Label0 = tkinter.Label(master = frameB, text = "PSG",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 3, column=0)
Label0Q = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=1)
Label0W = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=2)
Label0E = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=3)
Label0 = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=4)
Label0 = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=5)

Label0 = tkinter.Label(master = frameB, text = "PSV",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 4, column=0)
Label0Q = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=1)
Label0W = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=2)
Label0E = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=3)
Label0 = tkinter.Label(master = frameB, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=4)
Label0 = tkinter.Label(master = frameB, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=5)

frameB.place(x = 360, y = 230)

frameC = tkinter.Frame(frame7)

Label0 = tkinter.Label(master = frame7, text = "     GROUP C    ", height=1, width = 30, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").place(x=435, y = 396)

Label0 = tkinter.Label(master = frameC, text = "Club",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 0, column=0); Label0Q = tkinter.Label(master = frameC, text = "GP",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=1);Label0W = tkinter.Label(master = frameC, text = "Won",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=2);Label0E = tkinter.Label(master = frameC, text = "Drawn",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=3);Label0 = tkinter.Label(master = frameC, text = "Lost",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=4);Label0 = tkinter.Label(master = frameC, text = "Points",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=5)

Label0 = tkinter.Label(master = frameC, text = "Chelsea",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 1, column=0)
Label0Q = tkinter.Label(master = frameC, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=1)
Label0W = tkinter.Label(master = frameC, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=2)
Label0E = tkinter.Label(master = frameC, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=3)
Label0 = tkinter.Label(master = frameC, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=4)
Label0 = tkinter.Label(master = frameC, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=5)

Label0 = tkinter.Label(master = frameC, text = "Real Madrid",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 2, column=0)
Label0Q = tkinter.Label(master = frameC, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=1)
Label0W = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=2)
Label0E = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=3)
Label0 = tkinter.Label(master = frameC, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=4)
Label0 = tkinter.Label(master = frameC, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=5)

Label0 = tkinter.Label(master = frameC, text = "Intermilan",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 3, column=0)
Label0Q = tkinter.Label(master = frameC, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=1)
Label0W = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=2)
Label0E = tkinter.Label(master = frameC, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=3)
Label0 = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=4)
Label0 = tkinter.Label(master = frameC, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=5)

Label0 = tkinter.Label(master = frameC, text = "Bayern",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 4, column=0)
Label0Q = tkinter.Label(master = frameC, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=1)
Label0W = tkinter.Label(master = frameC, text = "0",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=2)
Label0E = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=3)
Label0 = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=4)
Label0 = tkinter.Label(master = frameC, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=5)

frameC.place(x = 360, y = 420)


#top goal scorers

frameD = tkinter.Frame(frame7)
frame1A = tkinter.Frame(frame7)
Label0c = tkinter.Label(master = frame1A, text = "     TOP SCORERS    ", height=1, width = 29, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid")
Label0c.pack()
frame1A.place(x = 45, y =25)
Label0 = tkinter.Label(master = frameD, text = "S/N",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 0, column=0); Label0Q = tkinter.Label(master = frameD, text = "Player",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=1);Label0W = tkinter.Label(master = frameD, text = "Games",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=2);Label0E = tkinter.Label(master = frameD, text = "Goals",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=3)

Label0 = tkinter.Label(master = frameD, text = "1",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 1, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Lionel Messi",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=2)
Label0E = tkinter.Label(master = frameD, text = "7",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=3)

Label0 = tkinter.Label(master = frameD, text = "2",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 2, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Cristiano Ronaldo",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=2)
Label0E = tkinter.Label(master = frameD, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=3)

Label0 = tkinter.Label(master = frameD, text = "3",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 3, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Romelu Lukaku",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=2)
Label0E = tkinter.Label(master = frameD, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=3)

Label0 = tkinter.Label(master = frameD, text = "4",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 4, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Neymar JR",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=2)
Label0E = tkinter.Label(master = frameD, text = "5",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=3)

Label0 = tkinter.Label(master = frameD, text = "5",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 5, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Harry Kane",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=2)
Label0E = tkinter.Label(master = frameD, text = "5",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=3)

Label0 = tkinter.Label(master = frameD, text = "6",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 6, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Antonio Griezman",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=2)
Label0E = tkinter.Label(master = frameD, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=3)

Label0 = tkinter.Label(master = frameD, text = "7",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 7, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Sergio Aguero",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=2)
Label0E = tkinter.Label(master = frameD, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=3)

Label0 = tkinter.Label(master = frameD, text = "8",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 8, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Heung-min Son",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=2)
Label0E = tkinter.Label(master = frameD, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=3)

Label0 = tkinter.Label(master = frameD, text = "9",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 9, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Raheem Sterling",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=2)
Label0E = tkinter.Label(master = frameD, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=3)

Label0 = tkinter.Label(master = frameD, text = "10",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 10, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Ngolo Kante",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=2)
Label0E = tkinter.Label(master = frameD, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=3)

Label0 = tkinter.Label(master = frameD, text = "11",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 11, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Karim Benzema",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=2)
Label0E = tkinter.Label(master = frameD, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=3)

Label0 = tkinter.Label(master = frameD, text = "12",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 12, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Eden Hazard",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=2)
Label0E = tkinter.Label(master = frameD, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=3)

Label0 = tkinter.Label(master = frameD, text = "13",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 13, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Edison Cavani",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=2)
Label0E = tkinter.Label(master = frameD, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=3)

Label0 = tkinter.Label(master = frameD, text = "14",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 14, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Gabriel Jesus",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=2)
Label0E = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=3)

Label0 = tkinter.Label(master = frameD, text = "15",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 15, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Jack Graelish",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=2)
Label0E = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=3)

Label0 = tkinter.Label(master = frameD, text = "16",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 16, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Di Maria",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=1)
Label0W = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=2)
Label0E = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=3)

Label0 = tkinter.Label(master = frameD, text = "17",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 17, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Sadio Mane",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=2)
Label0E = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=3)

Label0 = tkinter.Label(master = frameD, text = "18",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 18, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Roberto Firminho",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=2)
Label0E = tkinter.Label(master = frameD, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=3)

Label0 = tkinter.Label(master = frameD, text = "19",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 19, column=0)
Label0Q = tkinter.Label(master = frameD, text = "Mohammed Salah",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=2)
Label0E = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=3)

Label0 = tkinter.Label(master = frameD, text = "20",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 20, column=0)
Label0Q = tkinter.Label(master = frameD, text = "J Jota",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=1)
Label0W = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=2)
Label0E = tkinter.Label(master = frameD, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=3)

frameD.place(x = 45, y = 50)


#top assists

frameE = tkinter.Frame(frame7)
frame1B = tkinter.Frame(frame7)
Label0 = tkinter.Label(master = frame1B, text = "     TOP ASSITS    ", height=1, width = 29, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").pack()
frame1B.place(x = 815,y = 25)
Label0 = tkinter.Label(master = frameE, text = "S/N",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 0, column=0); Label0Q = tkinter.Label(master = frameE, text = "Player",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=1);Label0W = tkinter.Label(master = frameE, text = "Games",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=2);Label0E = tkinter.Label(master = frameE, text = "Goals",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 0, column=3)

Label0 = tkinter.Label(master = frameE, text = "1",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 1, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Lionel Messi",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=2)
Label0E = tkinter.Label(master = frameE, text = "7",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 1, column=3)

Label0 = tkinter.Label(master = frameE, text = "2",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 2, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Cristiano Ronaldo",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=2)
Label0E = tkinter.Label(master = frameE, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 2, column=3)

Label0 = tkinter.Label(master = frameE, text = "3",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 3, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Romelu Lukaku",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=2)
Label0E = tkinter.Label(master = frameE, text = "6",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 3, column=3)

Label0 = tkinter.Label(master = frameE, text = "4",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 4, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Neymar JR",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=2)
Label0E = tkinter.Label(master = frameE, text = "5",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 4, column=3)

Label0 = tkinter.Label(master = frameE, text = "5",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 5, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Harry Kane",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=2)
Label0E = tkinter.Label(master = frameE, text = "5",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 5, column=3)

Label0 = tkinter.Label(master = frameE, text = "6",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 6, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Antonio Griezman",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=2)
Label0E = tkinter.Label(master = frameE, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 6, column=3)

Label0 = tkinter.Label(master = frameE, text = "7",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 7, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Sergio Aguero",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=2)
Label0E = tkinter.Label(master = frameE, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 7, column=3)

Label0 = tkinter.Label(master = frameE, text = "8",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 8, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Heung-min Son",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=2)
Label0E = tkinter.Label(master = frameE, text = "4",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 8, column=3)

Label0 = tkinter.Label(master = frameE, text = "9",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 9, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Raheem Sterling",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=2)
Label0E = tkinter.Label(master = frameE, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 9, column=3)

Label0 = tkinter.Label(master = frameE, text = "10",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 10, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Ngolo Kante",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=2)
Label0E = tkinter.Label(master = frameE, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 10, column=3)

Label0 = tkinter.Label(master = frameE, text = "11",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 11, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Karim Benzema",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=2)
Label0E = tkinter.Label(master = frameE, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 11, column=3)

Label0 = tkinter.Label(master = frameE, text = "12",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 12, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Eden Hazard",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=2)
Label0E = tkinter.Label(master = frameE, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 12, column=3)

Label0 = tkinter.Label(master = frameE, text = "13",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 13, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Edison Cavani",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=2)
Label0E = tkinter.Label(master = frameE, text = "3",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 13, column=3)

Label0 = tkinter.Label(master = frameE, text = "14",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 14, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Gabriel Jesus",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=2)
Label0E = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 14, column=3)

Label0 = tkinter.Label(master = frameE, text = "15",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 15, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Jack Graelish",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=2)
Label0E = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 15, column=3)

Label0 = tkinter.Label(master = frameE, text = "16",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 16, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Di Maria",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=1)
Label0W = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=2)
Label0E = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 16, column=3)

Label0 = tkinter.Label(master = frameE, text = "17",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 17, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Sadio Mane",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=2)
Label0E = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 17, column=3)

Label0 = tkinter.Label(master = frameE, text = "18",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 18, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Roberto Firminho",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=2)
Label0E = tkinter.Label(master = frameE, text = "2",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 18, column=3)

Label0 = tkinter.Label(master = frameE, text = "19",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 19, column=0)
Label0Q = tkinter.Label(master = frameE, text = "Mohammed Salah",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=2)
Label0E = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 19, column=3)

Label0 = tkinter.Label(master = frameE, text = "20",  width = 4, height=1, foreground = "white",background= "black",font="times 12",bd=1, borderwidth=1, relief = "solid").grid(row = 20, column=0)
Label0Q = tkinter.Label(master = frameE, text = "J Jota",  width = 12, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=1)
Label0W = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=2)
Label0E = tkinter.Label(master = frameE, text = "1",  width = 6, height=1, foreground = "white",background= "black",font="times 12",bd=5, borderwidth=1.4, relief = "solid").grid(row = 20, column=3)

frameE.place(x = 815, y = 50)


btn1=tkinter.Button(frame7,text="TOP SCORERS",padx=0,pady=0,fg="white",bg = "black", font="times 11",bd=5,relief="raised", width=12, command = lambda:TopScorers())
btn1.place(x=455, y=565)
btn1A=tkinter.Button(frame7,text="TOP ASSITS",padx=0,pady=0,fg="white",bg = "black", font="times 11",bd=5,relief="raised", width=12, command = lambda: TopAssists())
btn1A.place(x=569, y=565)






#searchb bar
modal = tkinter.Frame(width=1265, height = 700, background = "powder blue")
modal.place(x=163, y=88, width =1265, height =800 )


my_imagee = ImageTk.PhotoImage(Image.open("pic8.JPG"))
pity = tkinter.Label(master = modal, image = my_imagee, anchor = NW, height = 800, width = 1200, bg= "black" )
pity.place(x=0, y=0, relwidth = 10, relheight = 10)

frame2a = tkinter.Frame(modal, width=220, height=700,background = "black")
frame2a.place(x = 1025, y = 0)


Team = StringVar()
Team_name = tkinter.Entry(modal, width = 10, textvariable=Team, bd=5, font = "times 9")
Team_name.place(x = 1040, y = 0)

btn1=tkinter.Button(modal,text="FIND ID",padx=0,pady=0,fg="white",bg = "dark blue", font="times 9",bd=5,relief="raised", width=9, command = lambda: edit_item())
btn1.place(x=1110, y=0)  

l_name = tkinter.Label(modal, text="CLUB",bd=5, foreground = "white", background= "dark blue", font="times 9")
l_name.place(x = 1100, y= 40)
name_var = StringVar() 
name = tkinter.Entry(modal, textvariable=name_var, bd=5)
name.place(x= 1055, y = 69)

l_amount = tkinter.Label(modal, text="STADIUM", bd=5, foreground = "white", background= "dark blue", font="times 9")
l_amount.place(x = 1085, y= 130)
amount_var = StringVar()
amount = tkinter.Entry(modal, textvariable=amount_var, bd=5)
amount.place(x = 1055, y= 159)

l_quantity = tkinter.Label(modal, text="CAPACITY", bd=5, foreground = "white", background= "dark blue", font="times 9")
l_quantity.place(x = 1087, y= 230)
quantity_var = StringVar()
quantity = tkinter.Entry(modal, textvariable=quantity_var, bd=5)
quantity.place(x = 1055, y= 259)

l_costprice = tkinter.Label(modal, text="CLUB CAPTAIN", bg = "blue", bd=5, foreground = "white", background= "dark blue", font="times 9")
l_costprice.place(x = 1072, y= 330)
costprice_var = StringVar()
costprice = tkinter.Entry(modal, textvariable=costprice_var, bd=5)
costprice.place(x = 1055, y= 359)

l_salesprice = tkinter.Label(modal, text="TITLES WON", bd=5, foreground = "white", background= "dark blue", font="times 9")
l_salesprice.place(x = 1080, y= 430)
salesprice_var = StringVar()
salesprice = tkinter.Entry(modal, textvariable=salesprice_var, bd=5)
salesprice.place(x = 1055, y= 459)
            
l_description = tkinter.Label(modal, text="BETTING ODDS", bd=5, foreground = "white", background= "dark blue", font="times 9")
l_description.place(x = 1070, y= 530)
descriptionV = StringVar()
description = tkinter.Entry(modal, textvariable = descriptionV, bd=5 )
description.place(x = 1055, y= 559)
frame4 = tkinter.Frame(width=1265, height = 700, background = "powder blue")
my_image9 = ImageTk.PhotoImage(Image.open("pic9.JPG"))
tityy9 = tkinter.Label(master = frame4, image = my_image9, anchor = NW, height = 800, width = 1200, bg= "black" )
tityy9.place(x=0, y=0, relwidth = 10, relheight = 10)

        
   

Label0v = tkinter.Label(master = frame4, text = "PLEASE  TYPE  YOUR  AGE  IN  THE  TEXT  BOX  FOR  AGE  VERIFICATION", height=1, width = 65, foreground = "white",background= "dark blue",font="times 13",bd=5, borderwidth=1.4, relief = "solid").place(x=200, y = 1)
entry8 = tkinter.Entry(master = frame4, textvariable= int, foreground = "black", background = "white", width =10,font="times 9",bd=5)
entry8.place(x = 790, y = 0)
btn1x=tkinter.Button(frame4,text="ENTER",padx=0,pady=0,fg="white",bg = "black", font="times 9",bd=5,relief="raised", width=12, command = lambda: verify())
btn1x.place(x=862, y=0)

Frame201 = tkinter.Frame(width=1530, background = "dark blue",height=5, highlightbackground= "black", highlightthickness=2)
Label1 = tkinter.Label(master = Frame201,text = "YOUR AGE WAS SUCCESSFULLY VERFIED. HOWEVER, THE BETTING PAGE IS CURRNTLY UNDER MAINTENANCE", font="times 15", foreground = "white", background = "black")
Label1.pack()
Btn999 = tkinter.Button(Frame201,text="OK",fg="black",font="times 9",bd=5,relief="solid", width=9, height= 2, borderwidth=1.1, command = lambda: alert())
Btn999.pack(padx=17,pady=60)
Frame201.place(x=300, y = 100)


frame4.place(x=163, y = 88,width= 1265, height = 800 )


#frame7 = tkinter.Frame(width=1000, height = 700, background = "black" )
#my_image = ImageTk.PhotoImage(Image.open("pic5.JPG"))
#tity = tkinter.Label(master = frame7, image = my_image, anchor = NW, height = 800, width = 1200, bg= "black" )
#tity.place(x=0, y=0, relwidth = 10, relheight = 10)
#frame7.place(x=163, y = 88,width= 1265, height = 800 )


#results

my_imageee2 = ImageTk.PhotoImage(Image.open("pic5.JPG"))
tityy2 = tkinter.Label(master = frame7B, image = my_imageee2, anchor = NW, height = 800, width = 1200, bg= "black" )
tityy2.place(x=0, y=0, relwidth = 10, relheight = 10)
frame7B.place(x=163, y = 88 )
Label0 = tkinter.Label(master = frame7B, text = "     TUESDAY, SEPTEMBER 08. 2021    ", height=1, width = 30, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=425, y = 25)


Label0 = tkinter.Label(master = frame7B, text = "                  Barcelona                     4  :  1               Chelsea                    ", height=1,width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 50)
Label1 = tkinter.Label(master = frame7B, text = "                  Realmadrid                   3  :  2                Bayern                    ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 75)
Label2 = tkinter.Label(master = frame7B, text = "                  Manchester United        0  :  0                 Ajax                      ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 100)
Label3 = tkinter.Label(master = frame7B, text = "                  Liverpool                     2  :  4                 PSG                     ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 125)
Label4 = tkinter.Label(master = frame7B, text = "                    Porto                           2  :  2                Sevilla                      ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 150)
Label5 = tkinter.Label(master = frame7B, text = "                   Dortmond                    3  :  1              Atletico                     ", height=1,width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 175)
Label35 = tkinter.Label(master = frame7B, text = "                  Napoli                         1  :  0                 Inter                     ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 195)
Label46 = tkinter.Label(master = frame7B, text = "                  Mainz                          2  :  0              Arsenal                    ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 220)


Label01 = tkinter.Label(master = frame7B, text = "     WEDNESDAY, SEPTEMBER 09. 2021    ", height=1, width = 30, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=425, y = 290)
Label02 = tkinter.Label(master = frame7B, text = "                 Benfica                        4  :  5                  PSV                      ", height=1,width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 315)
Label13 = tkinter.Label(master = frame7B, text = "                 Monaco                       0  :  3                Everton                   ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 340)
Label24 = tkinter.Label(master = frame7B, text = "                 Valencia                       2  :  2               AC Milan                 ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 365)
Label35 = tkinter.Label(master = frame7B, text = "                  Napoli                         2  :  1                 Inter                       ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 390)
Label46 = tkinter.Label(master = frame7B, text = "                 Mainz                          0  :  2                Arsenal                   ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 415)
Label57 = tkinter.Label(master = frame7B, text = "                 Juventus                      3  :  3                FC Koln                 ", height=1,width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 440)
Label4 = tkinter.Label(master = frame7B, text = "                 Porto                           4  :  2                Sevilla                    ", height=1, width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 465)
Label5 = tkinter.Label(master = frame7B, text = "                 Dortmond                    5  :  1               Atletico                   ", height=1,width = 45, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=350, y = 490)


#fixtures
my_imageee1 = ImageTk.PhotoImage(Image.open("pic5.JPG"))
tityy1 = tkinter.Label(master = frame7A, image = my_imageee1, anchor = NW, height = 800, width = 1200, bg= "black" )
tityy1.place(x=0, y=0, relwidth = 10, relheight = 10)
Label0 = tkinter.Label(master = frame7A, text = "     TUESDAY, SEPTEMBER 15. 2021    ", height=1, width = 30, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=425, y = 25)


Label0 = tkinter.Label(master = frame7A, text = "   Barcelona                       Vs           Chelsea               8:45PM     ", height=1,width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 50)
Label1 = tkinter.Label(master = frame7A, text = "   Realmadrid                     Vs            Bayern               8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 75)
Label2 = tkinter.Label(master = frame7A, text = "   Manchester United          Vs             Ajax                  8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 100)
Label3 = tkinter.Label(master = frame7A, text = "   Liverpool                        Vs             PSG                 8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 125)
Label4 = tkinter.Label(master = frame7A, text = "   Porto                              Vs           Sevilla                 8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 150)
Label5 = tkinter.Label(master = frame7A, text = "   Dortmond                       Vs          Atletico                8:45PM     ", height=1,width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 175)
Label35 = tkinter.Label(master = frame7A, text = "  Napoli                             Vs              Inter                8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 195)
Label46 = tkinter.Label(master = frame7A, text = "  Mainz                              Vs           Arsenal               8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 220)


Label01 = tkinter.Label(master = frame7A, text = "     WEDNESDAY, SEPTEMBER 16. 2021    ", height=1, width = 30, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=425, y = 290)
Label02 = tkinter.Label(master = frame7A, text = "  Benfica                           Vs              PSV                 8:45PM     ", height=1,width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 315)
Label13 = tkinter.Label(master = frame7A, text = "  Monaco                          Vs            Everton              8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 340)
Label24 = tkinter.Label(master = frame7A, text = "  Valencia                          Vs           AC Milan            8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 365)
Label35 = tkinter.Label(master = frame7A, text = "  Napoli                             Vs              Inter                8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 390)
Label46 = tkinter.Label(master = frame7A, text = "  Mainz                              Vs            Arsenal              8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 415)
Label57 = tkinter.Label(master = frame7A, text = "  Juventus                          Vs            FC Koln            8:45PM     ", height=1,width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 440)
Label4 = tkinter.Label(master = frame7A, text = "  Porto                               Vs            Sevilla               8:45PM     ", height=1, width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 465)
Label5 = tkinter.Label(master = frame7A, text = "  Dortmond                        Vs           Atletico              8:45PM     ", height=1,width = 50, foreground = "white",background= "black",font="times 14",bd=5, borderwidth=1.4, relief = "solid").place(x=320, y = 490)

frame7A.place(x=163, y = 88 )





frame11 = tkinter.Frame( background = "powder blue")
my_imageee = ImageTk.PhotoImage(Image.open("pic5.JPG"))
tityy = tkinter.Label(master = frame11, image = my_imageee, anchor = NW, height = 800, width = 1200, bg= "black" )
tityy.place(x=0, y=0, relwidth = 10, relheight = 10)
frame11.place(x=163, y = 88,width= 1265, height = 800 )


window.mainloop()