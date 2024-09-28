'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to remove element from tuple
'''

def remove_element(tuple_value,element):
          '''
          Description: 
              The function to remove the tuple element   
          Parameters:
              tuple_value (tuple): The input tuple value
              element (any): The element to remove the from tuple 
          Return :
              list1 (tuple) : The updated tuple 
          '''
          list1=list(tuple_value)
          list1.remove(element)
          return tuple(list1)

def main():
    tuple_value=(1,2,3,4,5)
    element=5
    print(remove_element(tuple_value,element))
    
if __name__=="__main__":
    main()