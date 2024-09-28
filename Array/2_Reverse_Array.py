'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Finding the day by the date    
'''
import array as arr
def reverse_Array(data):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          return data[::-1]
        
def main():
    data=arr.array('i',[1,2,3,4,5])
    rev_arr=reverse_Array(data)
    for i in range(len(rev_arr)):
          print(rev_arr[i],end=" ")
    
if __name__=="__main__":
    main()