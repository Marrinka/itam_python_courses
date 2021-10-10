def debug_control(*args, **kwargs):
    a = {'str': 0, 'int': 0, 'float': 0}
    for el in args:
        if type(el) is str :
            a['str'] += 1
        if type(el) is int :
            a['int'] += 1
        if type(el) is float :
            a['float'] += 1
    for el in kwargs:
        if type(el) is str:
            a['str'] += 1
        if type(el) is int:
            a['int'] += 1
        if type(el) is float:
            a['float'] += 1
    return 'srt: {}, int: {}, float: {}'.format(a['str'], a['int'], a['float'])