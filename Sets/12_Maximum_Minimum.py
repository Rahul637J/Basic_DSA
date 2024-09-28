'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to create set difference    
'''

def maximum_minimum(set1):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          maximum=max(set1)
          minimum=min(set1)

          return maximum,minimum

def main():
    set1={1,2,3,4,5,6,10}
    maximum,minimum=maximum_minimum(set1)
    print("Maximum",maximum)
    print("Minimum",minimum)
    
if __name__=="__main__":
    main()