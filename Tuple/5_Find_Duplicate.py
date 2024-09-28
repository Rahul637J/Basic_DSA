'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to find the repeated items of a tuple    
'''

def find_duplicate(tuple_numbers):
          '''
          Description: 
              The function to find duplicate in tuple   
          Parameters:
               tuple_numbers(tuple): The input tuple
          Return :
              duplicate(tuple): The repeated item in the tuple_numbers
          '''
          duplicate=[]
          original=[]

          for item in tuple_numbers:
                  if item not in original:
                         original.append(item)
                  else:
                         duplicate.append(item)     
        
          return tuple(duplicate)

def main():
    tuple_numbers=(1,1,5,6,2,2,3,4,4,10,11,12,7,7)
    print(find_duplicate(tuple_numbers))
    
if __name__=="__main__":
    main()