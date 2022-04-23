from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # *args for positional arguments
        # **kwargs for keyworded arguments
        print(f'{func.__name__}(', end='')

        res_args = []
        for arg in args:
            res_args.append(f'{str(arg)}: {type(arg)}')
        if kwargs:
            print(', '.join(res_args), end=', ')
        else:
            print(', '.join(res_args), end=') ')

        res_kwargs = []
        for key, value in kwargs.items():
            res_kwargs.append(f'{str(key)}: {type(key)}, {str(value)}: {type(value)}')
        if kwargs:
            print(', '.join(res_kwargs), end=')\n ')
        else:
            print(end='\n ')

        return func(*args, **kwargs)

    return wrapper


@type_logger  # for positional arguments
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)


@type_logger  # for positional and keyworded arguments
def calc_cube(x, **kwargs):
    return x ** 3


a = calc_cube(5, num=5)
print(a)
