'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to reverse a string    
'''

def reverse_String(scentence):
          '''
          Description: 
              This function takes a string as input and returns the string in reverse order.
          Parameters:
              scentence: str: The input to reverse string 
          Return :
              scentence: str: The reverse formatted string
          '''
        
          return scentence[::-1]

def main():
    scentence="Hello World"
    print("Before reverse :",scentence)
    print("After reverse :",reverse_String(scentence))

    
if __name__=="__main__":
    main()