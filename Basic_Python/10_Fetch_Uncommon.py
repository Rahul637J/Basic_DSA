'''
@Author: Rahul 
@Date: 2024-08-01
@Last Modified by: Rahul 
@Last Modified time: 2024-08-01
@Title: Python program to print out a set containing all the colors from color    
'''
        
def main():
    colours1=("Red","Green","Blue","Black")
    colours2=("Green","Blue")
    uniqueColour=set()
    for colour in colours1:
          if colour not in colours2:
                uniqueColour.add(colour)

    print(uniqueColour)            

if __name__=="__main__":
    main()