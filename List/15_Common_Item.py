'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to find common items from two lists    
'''

def common_items(list1,list2):
           '''
           Description: 
               The function finds and returns the common items between two lists.
           Parameters:
               list1: list - The first list of elements.
               list2: list - The second list of elements.
           Return:
               list: A list containing the common elements found in both list1 and list2.
           '''
           result=[]
           for item in list1:
                 if item in list2:
                     result.append(item)       
           return result           

def main():
    list1=[1,2,3,4,5]
    list2=[4,6,5,7,8]
    print(common_items(list1,list2))
    
if __name__=="__main__":
    main()