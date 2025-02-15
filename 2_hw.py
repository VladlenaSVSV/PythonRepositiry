def task_1():
    my_int: int = 20                      # Тип int
    my_float: float = 4.15                # Тип float
    my_str: str = "Here you go"           # Тип str
    my_list: list = [1, 2, 3, 4, 5]       # Тип list
    my_bool: bool = True                  # Тип bool

    print('my_int ', type(my_int))
    print('my_float ', type(my_float))
    print('my_str ', type(my_str))
    print('my_list ', type(my_list))
    print('my_bool ', type(my_bool))

    task_1()

    def task_2():
        mylist: list = [1, 2, 3, 5, 8, 13, 21]  # ряд фибоначчи
        print(mylist[0:3])

    task_2()

    def task_3(a: int) -> int:
        return a * a

    print(task_3(5))
