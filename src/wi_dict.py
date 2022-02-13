"""
----- Hash collisions: -----

>>> (hash(1)    == 1   and
...  hash(1.0)  == 1   and
...  hash(True) == 1)
True

>>> my_dict = {1: 'val_1', 1.0: 'val_2', True: 'val_3'}
>>> my_dict
{1: 'val_3'}

>>> my_dict = {}
>>> my_dict
{}
>>> my_dict[1.0]  = 'val_1'
>>> my_dict
{1.0: 'val_1'}
>>> my_dict[1]    = 'val_2'
>>> my_dict
{1.0: 'val_2'}
>>> my_dict[True] = 'val_3'
>>> my_dict
{1.0: 'val_3'}
"""


if __name__ == '__main__':
    from doctest import testmod
    testmod(name='wi_dict', verbose=True)
