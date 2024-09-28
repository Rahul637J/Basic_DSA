'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Finding the day by the date    
'''
import array as arr
def removeElement(data,target):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          for i in range(len(data)):
                if data[i] == target:
                      data.pop(i)
                      break
          return data

def main():
    data=arr.array('i',[1,2,3,5,4,5])
    target=1
    result_data=removeElement(data,target)
    for i in range(len(result_data)):
          print(data[i],end=" ")
    
if __name__=="__main__":
    main()