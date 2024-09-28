'''

@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to count the number of strings with specific conditions

'''

def countStringItems(list1):
    '''
    Description: 
        The function counts the number of strings in the list where the length of the string is 2 or more 
        and the first and last character of the string are the same.
    Parameters:
        list1: list - The list of strings to be evaluated
    Return:
        int - The count of strings that satisfy the conditions
    '''
    count = 0
    for item in list1:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count


def main():
    list1 = ['abc', 'xyz', 'aba', '1221']
    print(countStringItems(list1))
    
if __name__ == "__main__":
    main()
