'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Python program to find out the number of CPUs being used.  
'''

import os

def cpu_using():
    '''
    Description:
        Returns the number of CPUs available on the current machine.
    Parameters:
        None
    Return:
        int: The number of CPUs available. Returns None if the count cannot be determined.
    '''
    return os.cpu_count()

def main():
    print("The CPU count:", cpu_using())

if __name__ == "__main__":
    main()
