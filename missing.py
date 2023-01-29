
import collections
class strtodict(dict):

    def __missing__(self, key):

        if isinstance(key,str):
            raise KeyError
        return self[str(key)]

    def get(self,key,default=None):

        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

class streff(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError
        return self[str(key)]
    def __contains__(self, item):
        return item in self.data
    def __setitem__(self, key, value):
        self.data[str(key)] = value

#d = strtodict([('2', 'two'), ('4', 'four')])
d = streff([('2', 'two'), ('4', 'four')])
print(d[2])