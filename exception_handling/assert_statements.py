def divisors(num):
    divisors = [i for i in range(1, num+1) if num%i == 0]
    return divisors
        

def run():
    num = input("Enter an integer number: ")
    assert num.isnumeric() and int(num) > 0, "You must enter a positive integer number"
    print(divisors(int(num)))
    print("End")
    

if __name__ == "__main__":
    run()