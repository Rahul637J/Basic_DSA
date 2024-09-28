'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to count the number of characters (character frequency) in a
        string.    
'''

def character_Frequency(word):
          '''
          Description: 
              The function to count the frequency of the character in string    
          Parameters:
              word: String: The input word for finding frequency 
          Return :
              frequency: dict: The dictionary contains the frequency of the character  
          '''
          frequency=dict()
          for i in word:
                if i not in frequency:
                      frequency[i]=1
                else:
                      frequency[i]+=1
        
          return frequency

def main():
    scentence="Hello World"
    print(character_Frequency(scentence))
    
if __name__=="__main__":
    main()