'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to use of frozensets    
'''

def to_frozenSet(set1):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
        
          return frozenset(set1)

def main():
    set1={1,2,3,4,5,6,10}
    print(type(to_frozenSet(set1)))
    
if __name__=="__main__":
    main()