'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to add 'ing' at the end of a given string    
'''

def add_Stirng(input_String):
          '''
          Description: 
                 
          Parameters:
              None 
          Return :
              None
          '''
          if len(input_String)<3:
                return input_String
          elif input_String[len(input_String)-3:] != "ing":
                return input_String+"ing"
          else:
                return input_String+"ly"
          
def main():
    input_String="String"
    print("Output String :",add_Stirng(input_String))
    
    
if __name__=="__main__":
    main()