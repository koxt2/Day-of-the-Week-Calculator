# Day of the week calculator

# Using Zeller's congruence...

from tkinter import *
from tkinter.ttk import *

#Create root window and a frame in the window
root = Tk()
root.title("Day of the Week Calculator")
root.geometry("600x300")
frame = Frame(root)
frame.grid()

#Create labels
lbl_question = Label(frame, text="Please enter the date in the boxes below...")
lbl_question.grid(row=0, column=0, padx=10, pady=10)

lbl_day = Label(frame, text="Day", width=10)
lbl_day.grid(row=1, column=0)

lbl_month = Label(frame, text="Month", width=10)
lbl_month.grid(row=1, column=1)

lbl_year = Label(frame, text="Year", width=10)
lbl_year.grid(row=1, column=2)

#Get day
def selected_day(event):
    global q
    q = int(combo_day.get())

combo_day = Combobox(frame)
combo_day['values'] = list (range(1,32))
combo_day.set("Choose a day")
combo_day.grid(row=2, column=0)
combo_day.bind("<<ComboboxSelected>>", selected_day)

#Get month and determine month code
month_code={"January":13,
            "February":14,
            "March":3,
            "April":4,
            "May":5,
            "June":6,
            "July":7,
            "August":8,
            "September":9,
            "October":10,
            "November:":11,
            "December":12}

def selected_month(event):
    global m
    m = int(month_code[combo_month.get()])
    return m
    
combo_month = Combobox(frame)
combo_month.grid(row=2, column=1)
combo_month['values'] = list (month_code.keys())
combo_month.set("Choose a month")
combo_month.bind("<<ComboboxSelected>>", selected_month)

#Get year
def selected_year(event):
    global year_input
    year_input = int(entry_year.get())


entry_year = Entry(frame)
entry_year.grid(row=2, column=2)
entry_year.insert(0,"Choose a year") 
entry_year.bind("<KeyRelease>", selected_year) 

#Calibrate inputs
def calibrate_inputs():
    global year
    global k
    global j
    if m in [13,14]:
        year=int(year_input-1)
    else:
        year=int(year_input)
    k = int(year%100)
    j = int(year//100)

#Print inputs
def print_day():
    lbl_day = Label(frame, text=q).grid(row=4, column=0)

def print_month():
    lbl_month = Label(frame, text=m).grid(row=4, column=1)

def print_year():
    lbl_year = Label(frame, text=year_input).grid(row=4, column=2)

def print_calibraton():
    lbl_calibrated = Label(frame, text=year).grid(row=4, column=3)

but_day = Button(frame, text="Show day", command=print_day).grid(row=3, column=0)
but_month = Button(frame, text="Show month", command=print_month).grid(row=3, column=1)
but_year = Button(frame, text="Show year", command=print_year).grid(row=3, column=2)
but_calibrated = Button(frame, text="Show calibrated year", command=calibrate_inputs).grid(row=3, column=3)

#Validity of date
    #Leap year?
#if (year_input%4) == 0:
 #   if (year_input%100) == 0:
  #      if (year_input%400) == 0:
   #         year_leap = True
    #    else: year_leap = False
    #else:
     #   year_leap = True
#else:
 #   year_leap = False

    #Does the date lie within the missing dates of the Julian-Gregorian transition?
#def jul_greg_missing_date():
 #   jul_greg_missing_date = Label(frame, text="This date is invalid. When Britain, Ireland and the colonies switched from the Julian calendar to the Gregorian calendar they went to bed on the 3rd September 1752 and woke up on the 14th September!")
  #  jul_greg_missing_date.grid(row=5, column=0)

#if year_input == 1752 and m == 9 and q in range(3,14):
 #   command=jul_greg_missing_date

root.mainloop()
"""
#Day and month codes 
day_code={  0:"Saturday",
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",
            6:"Friday"}










    #Does the date lie within the given month?
if m in (4,6,9,11) and q not in range(1,31):
    print("This date is invalid. You can't have", q, "days in", m)
elif m in (3,5,7,8,10,12,13) and q not in range(1,32):
    print("This date is invalid. You can't have", q, "days in", m)
elif year_leap == False and m == 14 and q not in range(1,29):
    print("This date is invalid. You can only have up to 28 days in February")
elif year_leap == True and m == 14 and q not in range(1,30):
    print("This date is invalid. Even though", year_input, "is a leap year you can only have up to 29 days in February")            




#Final calculation
else:
    if year_input == 1752 and m == 9 and q <3:
        day = day_code[(q + 13*(m+1)//5 + k + k//4 + 5 - j) %7]
        print("The day on", str(q) + "/" + str(m) + "/" + str(year_input), "is a", day)
    else: 
        day = day_code[(q + 13*(m+1)//5 + k + k//4 + j//4 - 2*j) %7]
        print("The day on", str(q) + "/" + str(m) + "/" + str(year_input), "is a", day)
 
"""

