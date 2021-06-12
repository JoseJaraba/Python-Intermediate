def run():
    """
    squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i*i)
    """
    squares = [i*i for i in range (1,101) if i%3 != 0]
    print(squares)
    
    exercise = [i for i in range (1, 10000) if i%36 == 0]
    print(exercise)

if __name__ == '__main__':
    run()