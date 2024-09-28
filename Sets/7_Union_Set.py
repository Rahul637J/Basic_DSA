'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to create a union of sets    
'''

def union_set(set1,set2):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
        
          return set1|set2

def main():
    set1={1,2,3,4,5}
    set2={6,7,8,9,10}
    print(union_set(set1,set2))
    
if __name__=="__main__":
    main()