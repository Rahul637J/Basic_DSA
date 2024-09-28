'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to append a list to the second list.   
'''

def append_List(list1,list2):
        '''
        Description: 
            The function appends the elements of the second list to the first list.
        Parameters:
            list1: list - The first list of elements.
            list2: list - The second list of elements to append to the first list.
        Return:
            list: A new list containing elements from both list1 and list2.
        '''
        return list1+list2

def main():
    list1=[1,2,3,4,5]
    list2=[6,7,8,9,10]
    print(append_List(list1,list2))
    
if __name__=="__main__":
    main()