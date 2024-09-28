'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to find smallest items in a list    
'''

def smaller_items(list1):
          '''
          Description: 
              The function to find the smallest items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              min: int - The smallest item in the list 
          '''

          return min(list1)


def main():
    list1=[1,2,3,4,5,6]
    print(smaller_items(list1))
    
    
if __name__=="__main__":
    main()