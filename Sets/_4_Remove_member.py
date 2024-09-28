'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to remove item(s) from set    
'''
def remove_Element(set_values,value):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          set_values.remove(value)
          return set_values

def main():
    set_value={1,2,3,4,5,6}
    value=3
    print(remove_Element(set_value,value))
    
if __name__=="__main__":
    main()