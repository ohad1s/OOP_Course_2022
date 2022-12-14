class ReallySpecialMap:
    def __init__(self):
        self.__map = dict()

    def add(self, key, value):
        self.__map[key] = value

#We can now iterate over the map data structure

    def __iter__(self):
        return self.__map.__iter__()

    def __getitem__(self, item):
        return self.__map.get(item)

map = ReallySpecialMap()
map.add(0, 1)
map.add(1, 2)
map.add(2, 3)
map.add(3, 4)
map.add(4, 5)
map.add(5, 6)

# for key in map:
#     print(map[key])

it = map.__iter__()
print(next(it))

