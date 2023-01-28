from array import array
from random import random


a = array('d',(random() for x in range(10**7)))

fp = open('file','wb')
a.tofile(fp)