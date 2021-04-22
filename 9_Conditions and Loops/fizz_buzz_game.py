
def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz!')
    elif n % 3 == 0:
        print('Fizz!')
    elif n % 5 == 0:
        print('Buzz!')
    else:
        print(n)

n=int(input("Enter number from 1 to 100:\n"))

fizzbuzz(n)