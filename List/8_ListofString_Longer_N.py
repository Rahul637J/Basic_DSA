'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to find the list of words that are longer than n from a
        given list of words.    
'''

def calculate(list1,num):
        '''
        Description: 
            The function returns a list of words that are longer than a specified length.
        Parameters:
           list1: list - The list of words.
           num: int - The length threshold to compare the words against.
        Return:
        list: list - A list of words from the input list that are longer than the specified length.
        '''
        list2=list()
        for item in list1:
              if len(item)> num:
                    list2.append(item)
        return list2

def main():
    list1=['abc', 'xyz', 'aba', '1221']
    num=2
    print(calculate(list1,num))
    
if __name__=="__main__":
    main()