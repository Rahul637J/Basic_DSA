'''
@Author: Rahul 
@Date: 2024-08-06
@Last Modified by: Rahul 
@Last Modified time: 2024-08-06
@Title: Python program to unpack the tuple in sevaral variables     
'''

def unpack_tuple(data):
          '''
          Description: 
              The function to unpaking the tuple   
          Parameters:
              data (tuple): The tuple of data to unpack   
          Return :
              None
          '''
          
          college,degree,cgpa=data
          print("College :",college)
          print("Degree :",degree)
          print("CGPA :",cgpa)

def main():
    data=("Anna Unviversity","MCT",8.43)
    unpack_tuple(data)
    
if __name__=="__main__":
    main()