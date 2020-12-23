import sys

evenNumbers = [number for number in range(4400) if(number % 2 == 0)]

evenNumberGenerator = (number for number in range(440) if(number % 2 == 0))

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumberGenerator))
print('suma', sum(evenNumberGenerator))