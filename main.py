# idk
from pyscript import display, document


def create(e):
    document.getElementById('result').innerHTML = ' '

    password = document.getElementById('input1').value

    if not password.isdigit():                      
         if password.isalpha():
             display(f'Your password needs to contain atleast one number', target='result')
         else:
             display(f'Thank you for signing up!', target='result')
    
    else:
        display(f'Your password needs to contain atleast one letter', target='result')
    
  

         