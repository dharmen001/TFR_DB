class Boat(object):
    pass


my_boat = Boat()
my_boat2 = Boat()

if my_boat is my_boat2:
    print("they point the same address in memory")


'''cast to new str for string representation'''
hex_str_boat = str(my_boat)[-19:-1]
hex_str_boat2 = str(my_boat2)[-19:-1]

'''address of memory'''
print(int(hex_str_boat, 16))
print((int(hex_str_boat2, 16)))
print(id(my_boat))
print(id(my_boat2))


