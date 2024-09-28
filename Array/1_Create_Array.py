'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Python program to create an array of 5 integers and display the array items    
'''
import array as arr
def create_Array():
          '''
          Description: 
            The function to create an array
          Parameters:
              None 
          Return :
              None
          '''
          a=arr.array('i',[1,2,3,4,5])
          for i in range(len(a)):
                print(a[i],end=" ")
        
def main():
    create_Array()
    
    
if __name__=="__main__":
    main()