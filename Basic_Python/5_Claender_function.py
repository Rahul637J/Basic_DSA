'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program to print the calendar of a given month and year    
'''

import calendar

def printMonth(year, month):
    '''
    Description:
        Prints the calendar for a specified month and year.
    Parameters:
        year (int): The year for which the calendar is to be printed.
        month (int): The month for which the calendar is to be printed.
    Return:
        None
    '''
    print(calendar.month(year, month))

def main():
    year, month = 2024, 8
    printMonth(year, month)

if __name__ == "__main__":
    main()
