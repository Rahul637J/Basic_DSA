'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to remove duplicates from a list of lists   
'''

def remove_duplicate_list_of_list(list1):
          '''
          Description: 
              The function removes duplicate lists from a list of lists.
          Parameters:
              list1: list - A list containing other lists, potentially with duplicates.
          Return:
              list: A list of lists with duplicates removed.
          '''
          result=set()
          for item in list1:
                result.add(tuple(item))
          return [list(item) for item in result]           

def main():
    list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(remove_duplicate_list_of_list(list1))
    
if __name__=="__main__":
    main()