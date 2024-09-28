'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: python program to access environment variables    
'''
import os
def access_environment_variables():
           '''
           Description:
               Retrieves the value of the 'PYTHON_HOME' environment variable.
           Parameters:
               None
           Return:
               str: The value of the 'PYTHON_HOME' environment variable, or None if the variable is not set.
           '''
           return os.getenv('PYTHON_HOME')
        
def main():
    print(access_environment_variables())
    
if __name__=="__main__":
    main()