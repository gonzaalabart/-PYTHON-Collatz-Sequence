'''Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. '''

def collatz():
    try:
      number = int(input('Insert an int value: '))
      while number!= 1:
        if number % 2 == 0:
          number = number // 2
          print(number)
        else:
          number = 3 * number + 1
          print(number)
      return number
    except:
      print('Thats not a valid number')

collatz()

