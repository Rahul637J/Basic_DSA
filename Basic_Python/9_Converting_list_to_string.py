'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Finding the day by the date    
'''

def listToString(numbers):
    '''
    Description:
        Converts a list of numbers into a single string by concatenating their string representations.
    Parameters:
        numbers (list of int): A list of integers to be converted into a string.
    Return:
        str: A single string formed by concatenating the string representations of the integers in the list.
    '''
    return ''.join(map(str, numbers))

def main():
    numbers = [1, 2, 3, 6, 5, 4, 7]
    res = listToString(numbers)
    print(res)

if __name__ == "__main__":
    main()
