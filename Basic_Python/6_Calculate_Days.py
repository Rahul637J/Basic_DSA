'''
@Author: Rahul 
@Date: 2024-08-01
@Last Modified by: Rahul 
@Last Modified time: 2024-08-01
@Title: Python program to calculate the number of days between two dates    
'''

import datetime

def calculateDays(day1, day2):
    '''
    Description:
        Calculates and prints the number of days between two dates.
    Parameters:
        day1 (list of int): A list containing the year, month, and day for the first date in the format [year, month, day].
        day2 (list of int): A list containing the year, month, and day for the second date in the format [year, month, day].
    Return:
        None
    '''
    date1 = datetime.datetime(day1[0], day1[1], day1[2])
    date2 = datetime.datetime(day2[0], day2[1], day2[2])
    tot_days = (date2 - date1).days
    print(tot_days, "days")

def main():
    date1 = [int(i) for i in input("Enter the first date in [yyyy,mm,dd] format separated by commas: ").split(",")]
    date2 = [int(i) for i in input("Enter the second date in [yyyy,mm,dd] format separated by commas: ").split(",")]
    calculateDays(date1, date2)

if __name__ == "__main__":
    main()
