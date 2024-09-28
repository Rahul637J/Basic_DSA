'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Finding the day by the date    
'''
def add_in_range(n):
          '''
          Description: 
              The will add the object to dictionary in the given length   
          Parameters:
              n: int: The length for the dicitionary
          Return :
              None
          '''
          dictionary={}
          for i in range(1,n+1):
                dictionary[i]=i*i
          print(dictionary)
        
def main():
    n=5
    add_in_range(n)
    
    
if __name__=="__main__":
    main()