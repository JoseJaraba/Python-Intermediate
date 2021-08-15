def my_gen():
    for i in range(1, 101):
        if i % 2 == 0:
            yield i

def run():
    my_first_gen = my_gen()
    while True:
        try:
            print(next(my_first_gen))
        except StopIteration:
            print('End of the iteration')
            break

if __name__ == '__main__':
    run()
    