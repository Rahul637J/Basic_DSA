'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to create set difference    
'''

def clear_set(set1):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
        
          return set1.clear()

def main():
    set1={1,2,3,4,5,6,10}
    print(clear_set(set1))
    
if __name__=="__main__":
    main()