'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program to call an external command in Python
'''

import os

def external_Command():
    '''
    Description:
        Executes an external command to get the current working directory and prints it.
    Parameters:
        None
    Return:
        None
    '''
    result = os.getcwd()
    print(result)

def main():
    external_Command()

if __name__ == "__main__":
    main()
