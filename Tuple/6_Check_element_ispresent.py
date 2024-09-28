'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to check whether an element exists within a tuple    
'''

def isPresent(tuple_values,element):
          '''
          Description: 
              Description of function   
          Parameters:
              tuple_values(tuple): The tuple containing number
              element(any): To check it is present in tuple or not 
          Return :
              True if element is present in tuple, False otherwise
          '''
          if element in tuple_values:
                return True
        
          return False

def main():
    tuple_values=(1,2,3,5,4,6)
    element=1
    print(isPresent(tuple_values,element))
    
if __name__=="__main__":
    main()