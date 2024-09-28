'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to sum all the items in a list    
'''

def sum_items(list1):
          '''
          Description: 
              The function to sum all the items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              sum: int - The sum of all the items in the list 
          '''
          sum=0
          for i in list1:
                sum+=i
          return sum

def main():
    list1=[1,2,3,4,5,6]
    print(sum_items(list1))
    
if __name__=="__main__":
    main()