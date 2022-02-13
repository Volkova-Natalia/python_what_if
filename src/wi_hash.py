"""
>>> (hash(0)     == 0   and
...  hash(-0)    == 0   and
...  hash(0.0)   == 0   and
...  hash(False) == 0   and
...  hash("")    == 0)
False

>>> (hash(1)    == 1   and
...  hash(1.0)  == 1   and
...  hash(True) == 1)
True

>>> (hash(-1)   == -2   and
...  hash(-1.0) == -2)
True

>>> (hash(None) != 0   and
...  hash("0")  != 0   and
...  hash(" ")  != 0   and
...  hash("1")  != 1)
True

>>> hash(tuple())
5740354900026072187
>>> hash((tuple(), ))
-5486347211504344842

>>> (hash((0, ))     ==
...  hash((-0, ))    ==
...  hash((0.0, ))   ==
...  hash((False, )) ==
...  hash(("", ))    ==
...  -8753497827991233192)
True

>>> (hash((1, ))    ==
...  hash((1.0, ))  ==
...  hash((True, )) ==
...  -6644214454873602895)
True

>>> (hash((None, )) != hash((0, ))    and
...  hash(("0", ))  != hash((0, ))    and
...  hash((" ", ))  != hash(("", ))   and
...  hash(("1", ))  != hash((1, )))
True
"""


if __name__ == '__main__':
    from doctest import testmod
    testmod(name='wi_hash', verbose=True)
