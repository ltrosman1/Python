import sys

if len(sys.argv) < 2: #1 arg is script name
    print("Missing argument. Usage: python prime_numbers <number>")
    quit()

firstarg=sys.argv[1]


try:
    num = int(firstarg)
except:
    print("Invalid or missing argument. Usage: python prime_numbers < number>")
    quit()


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(str(count_primes(num)) + " prime_numbers up to number: {}".format(num))