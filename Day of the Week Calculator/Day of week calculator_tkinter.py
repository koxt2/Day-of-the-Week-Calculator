# Day of the week calculator
# Using Zeller's congruence...

from tkinter import *
from tkinter.ttk import *




##### Create root window and a frame in the window #####
root = Tk()
root.title("Day of the Week Calculator")
root.geometry("800x300")
frame = Frame(root)
frame.grid()




##### Create labels #####
lbl_question = Label(frame, text="Please enter the date in the boxes below...")
lbl_question.grid(row=0, column=0, padx=10, pady=10)

lbl_day = Label(frame, text="Day", width=10)
lbl_day.grid(row=1, column=0)

lbl_month = Label(frame, text="Month", width=10)
lbl_month.grid(row=1, column=1)

lbl_year = Label(frame, text="Year", width=10)
lbl_year.grid(row=1, column=2)



##### Get date (day,month,year) #####
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



##### Process inputs #####
#Leap year?
def leap_year():
    global leap
    if (year_input%4) == 0:
        if (year_input%100) == 0:
            if (year_input%400) == 0:
                leap = True
            else: leap = False
        else:
            leap = True
    else:
        leap = False


#Calibrate year
def calibrate_year():
    global year
    global k
    global j 
    if m in [13,14]:
        year=int(year_input-1)
    else:
        year=int(year_input)
    k = int(year%100)
    j = int(year//100)

#Is it a valid date?
#Does the date lie within the missing dates of the Julian-Gregorian transition?
def jul_greg_missing_date():
    global invalid_date_jul_greg
    if year_input == 1752 and m == 9 and q in range(3,14):
        invalid_date_jul_greg = True
    else:
       invalid_date_jul_greg = False

#Does the date lie within the given month?
def valid_date():
    if m in (4,6,9,11) and q not in range(1,31):
        invalid_date = Label(frame, text="This date is invalid. You can't have days in april").grid(row=6, column=0)
    elif m in (3,5,7,8,10,12,13) and q not in range(1,32):
        invalid_date = Label(frame, text="This date is invalid. You can't have days in march").grid(row=6,column=0)
    elif leap == False and m == 14 and q not in range(1,29):
        invalid_date = Label(frame, text="This date is invalid. You can only have up to 28 days in February").grid(row=6, column=0)
    elif leap == True and m == 14 and q not in range(1,30):
        invalid_date = Label(frame, text="This date is invalid. Even though it's a leap year you can only have up to 29 days in February").grid(row=6, column=0)            

#Final calculation

def result():
    day_code={  0:"Saturday",
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",
            6:"Friday"}
    if year_input == 1752 and m == 9 and q <3:
        day = day_code[(q + 13*(m+1)//5 + k + k//4 + 5 - j) %7]
        #print("The day on", str(q) + "/" + str(m) + "/" + str(year_input), "is a", day)
        print_result = Label(frame, text=day).grid(row=6, column=0)
    else: 
        day = day_code[(q + 13*(m+1)//5 + k + k//4 + j//4 - 2*j) %7]
        print_result = Label(frame, text=day).grid(row=6, column=0)



#Print inputs
def print_day():
    lbl_day = Label(frame, text=q).grid(row=3, column=0)

def print_month():
    lbl_month = Label(frame, text=m).grid(row=3, column=1)

def print_year():
    lbl_year = Label(frame, text=year_input).grid(row=3, column=2)

def print_leap():
    if leap == True:
        lbl_leap = Label(frame, text="Leap year!").grid(row=3, column=3)
    else:
        lbl_not_leap = Label(frame, text="Not a Leap!").grid(row=3, column=3)

def print_calibrated_year():
    lbl_calibrated_year = Label(frame, text=year).grid(row=3, column=4)
    lbl_calibrated_year = Label(frame, text=j).grid(row=4, column=4)
    lbl_calibrated_year = Label(frame, text=k).grid(row=5, column=4)

def print_invalid_date_jul_greg():
    if invalid_date_jul_greg == True:
        lbl_invalid_date_jul_greg = Label(frame, text="This date is invalid. When Britain, Ireland and the colonies switched from the Julian calendar to the Gregorian calendar they went to bed on the 3rd September 1752 and woke up on the 14th September!").grid(row=3, column=5)

but_process_data = Button(frame, text="Process data", command=lambda:[calibrate_year(), leap_year(), jul_greg_missing_date(), valid_date(), result()]).grid(row=4, column=0)
but_print_data = Button(frame, text="How inputted data", command=lambda:[print_day(), print_month(), print_year(), print_leap(), print_calibrated_year(), print_invalid_date_jul_greg()]).grid(row=5, column=0)





root.mainloop()

 