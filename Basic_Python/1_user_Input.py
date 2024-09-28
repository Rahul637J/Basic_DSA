'''
@Author: Rahul 
@Date: 2024-08-01
@Last Modified by: Rahul 
@Last Modified time: 2024-08-01
@Title: Print the user's first and last name in reverse order with a space between them     
'''

def main():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    print(last_name[::-1]+" "+first_name[::-1])
    
if __name__=="__main__":
    main()