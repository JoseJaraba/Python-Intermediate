from functools import reduce

def run():
    #-- Filter Function --#
    my_list = [1,4,5,6,9,13,19,21]
    # odd_nums = [i for i in my_list if i%2 != 0] list comprehension
    odd_nums = list(filter(lambda x: x%2 != 0, my_list))
    
    print(odd_nums)
    
    #-- Map Funciton --#
    my_list = [1,2,3,4,5]
    # squares = [i*i for i in my_list] list comprehension
    squares = list(map(lambda x: x*x, my_list))
    
    print(squares)
    
    #-- Reduce Function --#
    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a*b, my_list)
    
    print(all_multiplied)
    
if __name__ == '__main__':
    run()