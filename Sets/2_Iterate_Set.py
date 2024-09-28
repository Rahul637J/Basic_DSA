'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to iteration over set   
'''
def iterate_set(set_values):
          '''
          Description: 
              Description of function   
          Parameters:
              None 
          Return :
              None
          '''
          for i in set_values:
                print(i,end=" ")

def main():
    set_values={1,2,3,4,5}
    iterate_set(set_values)

    
if __name__=="__main__":
    main()