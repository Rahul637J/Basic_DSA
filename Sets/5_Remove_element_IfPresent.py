'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to remove an item from a set if it is present in the set    
'''
from _4_Remove_member  import remove_Element
def remove_Value(set_values,value):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          if value in set_values:
            remove_Element(set_values,value)
          
          return set_values  
                
def main():
    set_values={1,2,3,4,5,6}
    value=4
    print(remove_Element(set_values,value))
    
if __name__=="__main__":
    main()