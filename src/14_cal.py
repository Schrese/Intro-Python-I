"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# receive user input as argument input (we're not going to be using the 'input' function, because we're not waiting on the users' input, since the input comes in when running the file)
# sys.argv is a list of args that the user provides at the start of the program

# print(sys.argv) ---> Checking to make sure that it's working. this logs the file, and any arguments you enter in the console "python3 14_cal.py 4 2015" will print out a list of those arguments

# num_args = len(sys.argv)
# # print(sys.argv[1])
# cal = calendar.TextCalendar()

# month = datetime.now().month
# year = datetime.now().year

# # opone = (month, year)
# # optwo = (sys.argv[1], year)
# # opthree = (sys.argv[1], sys.argv[2])

# if num_args == 1:
#   month = datetime.now().month
#   year = datetime.now().year
#   cal.prmonth(month, year)

# def getDate(onlyone, only2=optwo, only3=opthree):
#   result = opone
#     result = cal.prmonth()





num_args = len(sys.argv)

# init an instance of the text calendar class
cal = calendar.TextCalendar()


# if user specified no args: 
if num_args == 1:
  # print current month and year
  month = datetime.now().month
  year = datetime.now().year
  # print(month, year) - that's not formatted
  # we want to print out the month with the calendar
  cal.prmonth(year, month)
# if user specified one arg:
elif num_args == 2:
  # assume that args is the month
  month = int(sys.argv[1])
  year = datetime.now().year
  # print that month of the current year
  cal.prmonth(year, month)
# If user specified 2 args:
elif num_args == 3:
  month = int(sys.argv[1])
  year = int(sys.argv[2])
  # print that month of that year
  cal.prmonth(year, month)
# otherwise
else:
  # print a message 
  print("usage: cal.py [month] [year]")
  # exit the program - Not needed, but this is nice. The "1" is just an arbitrary stataus code number that's been standardized to mean "we're exiting not because the program broke, but for some other reason"
  sys.exit(1) # this is good for if the user input something other than what we have accounted for

# we need to print out a formatted calendar
# cal.prmonth(year, month) # we did this to clean up the if/else's


# TO CLEAN IT UP
# cal = calendar.TextCalendar()

# month = datetime.now().month
# year = datetime.now().year