# Day of the week calculator
# Using Zeller's congruence

from tkinter import *
from tkinter.ttk import *

##### Create root window, a frame in the window and a grid to place widegets #####
root = Tk()
root.title("Day of the Week Calculator")
root.geometry("800x300")
frame = Frame(root)
frame.grid()

##### Dictionaries #####
day_key={   0:"Saturday",
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",
            6:"Friday"}

month_value={   "January":13,
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

##### Get date (day,month,year) #####
def select_day(event):
    global q
    q = int(combo_day.get())

def select_month(event):
    global m
    m = int(month_value[combo_month.get()])

def select_year(event):
    global year_input
    year_input = int(entry_year.get()) 
    
##### Calibrate input #####
def calibrate_input():
    global year, k, j, leap
    if m in [13,14]:
        year=int(year_input-1)
    else:
        year=int(year_input)

    k = int(year%100)
    j = int(year//100)
    
    if (year_input%4) == 0:
        if (year_input%100) == 0:
            if (year_input%400) == 0:
                leap = True
            else: leap = False
        else:
            leap = True
    else:
        leap = False

##### Test input #####
def test_input():
    if m in (4,6,9,11) and q not in range(1,31):
        output_text=("This date is invalid. You can't have", q, "days in", combo_month.get())
        invalid_date = Label(frame, text=output_text).grid(row=3, column=2)
    elif leap == False and m == 14 and q not in range(1,29):
        invalid_date = Label(frame, text="This date is invalid. You can only have up to 28 days in February").grid(row=3, column=2)
    elif leap == True and m == 14 and q not in range(1,30):
        invalid_date = Label(frame, text="This date is invalid. Even though it's a leap year you can only have up to 29 days in February").grid(row=3, column=2)            
    elif year_input == 1752 and m == 9 and q in range(3,14):
        lbl_invalid_date_jul_greg = Label(frame, text="This date is invalid. When Britain, Ireland and the colonies switched from the Julian calendar to the Gregorian calendar they went to bed on the 3rd September 1752 and woke up on the 14th September!").grid(row=3, column=2)

##### Perform calculation #####
def calculation():
        if year_input <=1752 and m >= 9 and q <3:
            day = day_key[(q + 13*(m+1)//5 + k + k//4 + 5 - j) %7]
            print_result = Label(frame, text=day).grid(row=4, column=0)
        else: 
            day = day_key[(q + 13*(m+1)//5 + k + k//4 + j//4 - 2*j) %7]
            print_result = Label(frame, text=day).grid(row=4, column=0)

##### GUI #####
lbl_day = Label(frame, text="Day")
lbl_day.grid(row=1, column=0, padx=20)

lbl_month = Label(frame, text="Month")
lbl_month.grid(row=1, column=1, padx=20)

lbl_year = Label(frame, text="Year")
lbl_year.grid(row=1, column=2, padx=20)

combo_day = Combobox(frame)
combo_day['values'] = list (range(1,32))
combo_day.set("Choose a day")
combo_day.grid(row=2, column=0)
combo_day.bind("<<ComboboxSelected>>", select_day)

combo_month = Combobox(frame)
combo_month.grid(row=2, column=1)
combo_month['values'] = list (month_value.keys())
combo_month.set("Choose a month")
combo_month.bind("<<ComboboxSelected>>", select_month)

entry_year = Entry(frame)
entry_year.grid(row=2, column=2)
entry_year.insert(0,"Choose a year") 
entry_year.bind("<KeyRelease>", select_year) 

##### Provide result #####
but_process_data = Button(frame, text="Process data", command=lambda:[calibrate_input(), test_input(), calculation()]).grid(row=2, column=3, padx=20)

root.mainloop()

 