# write a function that checks whether if the number passed into it is a prime number or not

def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number.")
    e       
            
    
        

n = int(input("Check this number:  "))
prime_checker(number=n)