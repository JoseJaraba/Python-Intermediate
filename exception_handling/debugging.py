def divisors(num):
    try:
        if num < 0:
            raise ValueError("Enter a positive number")
        divisors = [i for i in range(1, num+1) if num%i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        

def run():
    try: 
        num = int(input("Enter an integer number: "))
        print(divisors(num))
        print("End")
    except ValueError:
        print("You must enter an integer")
    

if __name__ == "__main__":
    run()