'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: python program to check whether two lists are circularly identical    
'''

def is_Circular(list1,list2):
          '''
          Description: 
              The function checks whether two lists are circularly identical, meaning one list can be rotated to match the other.
          Parameters:
              list1: list - The first list of elements.
              list2: list - The second list of elements.
          Return:
              bool: True if the two lists are circularly identical, otherwise False.
          '''
          if len(list1)!=len(list2):
                return False
          for item in list1:
                if list1[item:]+list1[:item]==list2:
                      return True
          return False     

def main():
    list1=[1,2,3,4]
    list2=[3,4,1,2]
    print(is_Circular(list1,list2))
    
if __name__=="__main__":
    main()