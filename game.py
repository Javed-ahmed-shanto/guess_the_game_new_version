import random
print('please give the minimum range number')
abra = int(input())
print('please give the maximum range number')
dabra = int(input())
print('Please Guess the Number')
your_number = int(input())
number = random.randint(abra,dabra)
if your_number == number:
    print('Congrats! You Have Guess The Correct Number In Your First Guess')
else:
    print('Sorry. Please Try Again')
    your_number = int(input())
    if your_number == number:
        print('Congrats! You Have Guess The Correct Number In this time')
    else:
        print("It's your last time buddy")
        your_number = int(input())
    if your_number == number:
        print('Congrats! You Have Guess The Correct Number In last time')
    else:
        print('Sorry brother! No luck')
