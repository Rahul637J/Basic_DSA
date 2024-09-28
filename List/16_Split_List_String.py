'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to split a list based on first character of word    
'''

def split_list_by_first_char(words):
           '''
           Description: 
               The function splits a list of words into a dictionary where the keys are the first characters of the words and the values are lists of words that start with that character.
           Parameters:
               words: list - A list of words to be split.
           Return:
               dict: A dictionary where each key is a first character of the words, and the value is a list of words that start with that character.
           '''
           result=dict()
           for items in words:
                 if items[0] not in result:
                       result[items[0]]=[]
                       result[items[0]].append(items)
                 else:
                       result[items[0]].append(items)      
           return result           

def main():
    words = ["apple", "apricot", "banana", "blueberry", "cherry", "cranberry", "date"]
    print(split_list_by_first_char(words))
    
if __name__=="__main__":
    main()