'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to get the difference between the two list   
'''

def ifPresent(list1,list2):
          '''
          Description: 
              The function returns the difference between two lists, specifically the elements present in the first list but not in the second list.
          Parameters:
              list1: list - The first list of elements.
              list2: list - The second list of elements to compare against.
          Return:
              list: A list containing elements that are in list1 but not in list2.
          '''
          result=[]
          for item in list1:
                if item not in list2:
                      result.append(item)
          return result

def main():
    list1=[1,2,3,4,5,6]
    list2=[4,10,7,5,8]
    print(ifPresent(list1,list2))
    
if __name__=="__main__":
    main()