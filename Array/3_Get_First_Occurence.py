'''
@Author: Rahul 
@Date: 2024-08-02
@Last Modified by: Rahul 
@Last Modified time: 2024-08-02
@Title: Finding the day by the date    
'''
import array as arr
def getOccurence(data,target):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          occurence=0
          for i in range(len(data)):
                if data[i] == target:
                      occurence=i
                      break
          return occurence

def main():
    data=arr.array('i',[1,2,3,5,4,5])
    target=2
    occurence=getOccurence(data,target)
    print(occurence)
    
if __name__=="__main__":
    main()