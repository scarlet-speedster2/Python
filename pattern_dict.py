from collections import OrderedDict
def get(record:dict) -> list:

    match record:

        case {'type':'book','api':2,'authors':[*names]}:
            return names

        case {'type':'book','api':1,'author':name}:
            return [name]
        case {'type':'book'}:
            raise ValueError("Invalid book")
        case {'type':'movie','director':name}:
            return [name]
        case _:
            raise ValueError(f"Invalid Record")

b1 = dict(api=1, author='Douglas Hofstadter',
type='book', title='Gödel, Escher, Bach')
b2 = OrderedDict(api=2, type='book',
title='Python in a Nutshell',
authors='Martelli Ravenscroft Holden'.split())

print(get(b1))
print(get(b2))