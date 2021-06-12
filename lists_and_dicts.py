def run():
    """Nesting List and dicts
    """
    #my_list = [1, "Hello", True, 4.5]
    #my_dict = {"firstname": "Jose", "lastname": "Jaraba"}
    
    super_list = [
        {"firstname": "Jose", "lastname": "Jaraba"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Laura", "lastname": "Perez"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Pablo", "lastname": "Marmol"}
    ]
    
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1.1,2.2,3.3,4.4,5.5]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for dicts in super_list:
        print(dicts["firstname"], "-", dicts["lastname"])
        

if __name__ == '__main__':
    run()