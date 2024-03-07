"""Filter"""
import json

_X = str(input())
_Y = float(input())
_DATADICT = json.loads(_X)
_DATALIST = list(_DATADICT.items())
_DATAOUT = []

for i in _DATALIST:
    if i[1] >= _Y:
        _DATAOUT.append(i)
        #print(str(i[0]) + "    " + str(i[1]))

if len(_DATAOUT) > 0:
    def custom_sort_key(item):
        """custom_sort_key"""
        return item[0]

    _DATAOUT.sort(key=custom_sort_key)

    for i in _DATAOUT:
        print(str(i[0]) + "\t" + str("%.2f" % (i[1])))
else:
    print("Nope")
