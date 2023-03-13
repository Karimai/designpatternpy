x = 10


def first_func():
    x = 20

    def inner_func_default():
        """
        default is nonlocal, it follows the search in scope chain order
        """
        print(x)  # 20

    def inner_func_nonlocal():
        nonlocal x
        print(x)  # 20

    def inner_func_global():
        global x
        print(x)  # 10

    def inner_func_mix():
        """
        It is a compile error and can be even compiled.
        Any attempt of access to a variable before nonlocal or global
        is a SyntaxError
        """
        global x
        print(x)
        try:
            nonlocal x
            print(x)
        except SyntaxError as e:
            print(f'not possible {e}')
            pass

    inner_func_default()
    inner_func_nonlocal()
    inner_func_global()
    inner_func_mix()


first_func()
