'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python function that takes two lists and returns True if they have at
        least one common member    
'''

def ifPresent(list1,list2):
          '''
          Description: 
              The function checks whether the two input lists have at least one common member.
          Parameters:
              list1: list - The first list of elements.
              list2: list - The second list of elements.
          Return:
              bool: True if there is at least one common member in both lists, otherwise False.
          '''
          
          for item in list1:
                if item in list2:
                      return True
          return False

def main():
    list1=[1,2,3,4,5,6]
    list2=[4,10,7,5,8]
    print(ifPresent(list1,list2))
    
if __name__=="__main__":
    main()