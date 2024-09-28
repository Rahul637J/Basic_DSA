'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to add member(s) in a set    
'''
def add_member(set_values,value):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          set_values.add(value)
          return set_values

def main():
    set_value={1,2,3,4,5}
    value=6
    print(add_member(set_value,value),end=" ")
    
    
if __name__=="__main__":
    main()