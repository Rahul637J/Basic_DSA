'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to reverse the tuple    
'''

def reverse_tuple(tuples):
          '''
          Description: 
              The function to reverse the tuple   
          Parameters:
              tuples (tuple): The tuple value to reverse
          Return :
              The revesed tuple
          '''
        
          return tuples[::-1]

def main():
    tuples=(10,9,8,7,6)
    print("Before reverse:",tuples)
    print("After reverse",reverse_tuple(tuples))
    
if __name__=="__main__":
    main()