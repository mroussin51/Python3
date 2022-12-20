#This is a random number generator aimed a selecting the winning lotery ticket. The problem is that it is picks matching numbers. 
import random
number1 = random.randint(1, 5)
print(number1)
number2 = random.randint(1, 5)
if number2 != number1 and number2 == number1:
    print(number2)
#if number2 == number1:
#    number2 = random.randint(1, 5)
#   number2 = random.randint(1, 5)
#print(number2) 

#number3 = random.randint(1, 5)
#if number3 != number1 and number2:
#    print(number3)
#     else number3 = random.randint(1, 5)
#number3 = random.randint(1, 5)
# print(number3)
#if number3 != number1 or number2:
#   number3 = random.randint(1, 5)
#print(number3)
# print(number3)
#number4 = random.randint(1, 5)
#if number4 == number1 == number2 == number3:
#	print(random.randint(1, 5))
# print(number4)
#number5 = random.randint(1, 5)
#if number5 == number1 == number2 == number3 == number4:
#    print(random.randint(1, 5))
