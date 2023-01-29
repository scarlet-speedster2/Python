from types import MappingProxyType

d = {1:'A'}
d_porxy = MappingProxyType(d)
#d_porxy[2] = 'X'
d[2] = 'X'
print(d_porxy)
