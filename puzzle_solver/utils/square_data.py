def square_data(lst, class_name):
    if 'piece' not in lst:
        print(lst)
    lst.remove("piece")
    lst.remove(class_name)
    return lst[0]
    
