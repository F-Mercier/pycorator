from data import TYPES


def pycorator(*args, **kwargs):
    def decorator(func):
        def wrapper(*func_args, **func_kwargs):
            icheck = kwargs.get('icheck')
            exp_i = kwargs.get('i')
            exp_o = kwargs.get('o')
            if icheck is None:
                icheck = range(len(args))
            if exp_i is not None:
                exp_i = TYPES.get(exp_i)
                for arg in func_args:
                    assert isinstance(arg, exp_i), 'Type {} of arg {} should be {}'.format(type(arg), arg, exp_i)
            res = func(*func_args, **func_kwargs)
            if exp_o is not None:
                exp_o = TYPES.get(exp_o)
                assert isinstance(res, exp_o), 'Type {} of result {} should be {}'.format(type(res), res, exp_o)
            return res
        return wrapper
    return decorator
