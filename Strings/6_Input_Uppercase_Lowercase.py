'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python script that takes input from the user and displays that input back in
        upper and lower cases.    
'''

def changeCase(inputString):
          '''
          Description: 
              This function will convert the input string to uppercase and lowercase   
          Parameters:
              inputString: str: The user input 
          Return :
              It will return the inputString in uppercase and lowercase
          '''

          return inputString.upper(),inputString.lower() 

def main():
    inputString=input("Enter the word or scentence : ")
    upperCase,lowerCase=changeCase(inputString)
    print("UpperCase :",upperCase,"\n","LowerCase :",lowerCase)

    
if __name__=="__main__":
    main()