'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Python program to list all files in a directory in Python   
'''
import os
def list_files():
         '''
         Description:
             Lists all files and directories in the specified directory.
         Parameters:
             None:
         Return:
             list: A list of file and directory names in the specified directory.
         '''
         return os.listdir()
        
def main():
    print("Files list:",list_files())
    
if __name__=="__main__":
    main()