'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to create set difference    
'''

def clone_tuple(original_tuple):
          '''
          Description: 
              The function will clone the tuple   
          Parameters:
              original_tuple (tuple): The original tuple   
          Return :
              copy_tuple(tuple): The cloned tuple
          '''
          copy_tuple=tuple(original_tuple)
          return copy_tuple

def main():
    original_tuple=(1,2,3,4,5,6)
    print(type(clone_tuple(original_tuple)))
    
if __name__=="__main__":
    main()