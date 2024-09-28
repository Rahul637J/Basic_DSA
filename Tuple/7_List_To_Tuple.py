'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to convert list to tuple   
'''

def toTuple(list1):
          '''
          Description: 
              The function to convert list to tuple   
          Parameters:
              list1 (list): The input list values 
          Return :
              list1 (tuple): The converted tuple from list
          '''
        
          return tuple(list1)

def main():
    list1=[1,2,3,4,5]
    print(toTuple(list1))
    
if __name__=="__main__":
    main()