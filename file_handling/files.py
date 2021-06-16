def read():
    numbers = list()
    with open("./db/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)
            
            
def write():
    names = ["Facundo", "Miguel", "José", "Chris"]
    with open("./db/names.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")

def run():
    write()

if __name__ == "__main__":
    run()