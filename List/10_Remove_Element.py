'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to print a specified list after removing the 0th, 4th and
        5th elements.    
'''

def removeELement(list1,positions):
          '''
          Description: 
              The function removes the elements at the specified positions from the input list.
          Parameters:
              list1: list - The list of elements.
              positions: list - A list of positions (indices) of the elements to be removed.
          Return:
              list: The modified list after removing the specified elements.
          '''
          
          for position in sorted(positions,reverse=True):
                del list1[position]

          return list1

def main():
    list1=[1,2,3,4,5,6]
    positions=[0,4]
    print(removeELement(list1,positions))
    # print(list1[4])
    
if __name__=="__main__":
    main()