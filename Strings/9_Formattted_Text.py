'''
@Author: Rahul 
@Date: 2024-08-05
@Last Modified by: Rahul 
@Last Modified time: 2024-08-05
@Title: Python program to display formatted text (width=50) as output    
'''
import textwrap
def formatText(text,width):
          '''
          Description: 
              The function to wrap the text with given width using 'textwrap madule'   
          Parameters:
              text: string: The input paragraph   
              width: int: The width for the wrap
          Return :
              text: The text in the wraped format 
          '''
          return textwrap.fill(text,width=width)

def main():
       text='''For example, consider a class shapes that have many objects like circle, square, triangle, etc. having its own attributes and methods. An instance attribute refers to the properties of that particular object like edge of the triangle being 3, while the edge of the square can be 4'''
       width=100
       print(formatText(text,width))
    
if __name__=="__main__":
    main()