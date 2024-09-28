'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program to check whether a file exists    
'''

def main():
    try:
        file=open("ML/Dem.txt")
        
    except IOError:
          print("File not found!!!")  
          file.close()  

if __name__=="__main__":
    main()