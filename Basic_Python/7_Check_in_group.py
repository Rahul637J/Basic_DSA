'''
@Author: Rahul 
@Date: 2024-08-01
@Last Modified by: Rahul 
@Last Modified time: 2024-08-01
@Title: Python program to check whether a specified value is contained in a group of values    
'''

def checkValue(group, value):
    '''
    Description:
        Checks whether the specified value is contained in the given group of values.
    Parameters:
        group (list): A list of values to search through.
        value (any): The value to check for in the group.
    Return:
        bool: True if the value is in the group, False otherwise.
    '''
    if value in group:
        return True
    else:
        return False

def main():
    group = [1, 2, 3, 4, 5]
    value = 2
    print(checkValue(group, value))

if __name__ == "__main__":
    main()
