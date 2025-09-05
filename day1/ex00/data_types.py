def data_types():
    var_int = 22
    var_str = 'Radzhab'
    var_float = 22.05
    var_bool = True
    var_list = [1, 2, 3, 4, 5]
    var_dict = {"Radzhab": 22, "Dad": 62, "Mom": 50}
    var_tuple = (1, 2, 3, 4, 5)
    var_set = {1, 2, 3, 4, 5}

    types = [type(var_int).__name__, type(var_str).__name__, type(var_float).__name__,
             type(var_bool).__name__, type(var_list).__name__, type(var_dict).__name__,
             type(var_tuple).__name__, type(var_set).__name__]
    print("[" + ", ".join(types) + "]")


if __name__ == '__main__':
    data_types()
