'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to get a string from a given string where all occurrences of its
        first char have been changed to '$'    
'''

def replace_Character(input_String):
          '''
          Description: 
              This function will replace the 2nd occurence of the 1st character with '$'   
          Parameters:
              input_String: str: The input string 
          Return :
              output_String: str: The updated string  
          '''

          character=input_String[0]
          input_String=input_String.replace(character,"$")
          output_String=character+input_String[1:] 
          return output_String

def main():
    input_String="restart"
    print(replace_Character(input_String))
    
if __name__=="__main__":
    main()