'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to multiply all the items in a list    
'''

def sum_items(list1):
          '''
          Description: 
              The function to multiply all the items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              sum: int - The multiplication of all the items in the list 
          '''
          product=1
          for i in list1:
                product*=i
          return product

def main():
    list1=[1,2,3,4,5,6]
    print(sum_items(list1))
    
if __name__=="__main__":
    main()