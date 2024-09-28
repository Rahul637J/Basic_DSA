'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to remove duplicates from a list    
'''

def removeDuplicate(list1):
           '''
            Description: 
                The function removes duplicate elements from the list and returns a list of unique elements.
            Parameters:
                list1: list - The list of elements (could be numbers or other hashable types)
            Return:
                list - A list containing only the unique elements from the input list
            '''
           
           unique=set()
           for i in list1:
                 unique.add(i)
           return list(unique)

def main():
    list1=[1,2,3,4,4,5,1,6]
    print(removeDuplicate(list1))
    
if __name__=="__main__":
    main()