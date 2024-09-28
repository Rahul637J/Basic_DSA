'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Python program to iterate over dictionaries using for loops.    
'''
def iterate_Dict(dictionary):
          '''
          Description: 
              The function will iterate the dictionary
          Parameters:
              dictionary: dict: The input dictionary to iterate
          Return :
              None
          '''
          for key in dictionary:
                print(key,":",dictionary[key])
        
def main():
    dictionary={
          1: 10,
          2: 20,
          3: 30,
          4: 40,
          5: 50,
          6: 60
          }
    iterate_Dict(dictionary)
    
if __name__=="__main__":
    main()