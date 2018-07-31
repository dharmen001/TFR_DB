# some of the double underscore functions

# __init__
# __del__ #called when refrence count reaches zero
# __len__
# __str__


class ShoppingList(object):

    def __init__(self, **items):

        self.shopping_list = items

    # len returns the len of shopping list
    def __len__(self):

        total_items = 0

        for _ in self.shopping_list:
            total_items += 1

        return total_items

    # String representation of the object : # Return String
    def __str__(self):
        return "List contains Items: " + ",".join(self.shopping_list.keys())

    # object refrence count  = 0, when object is about to get destroyed
    def __del__(self):
        print("Object gets destroyed")

    # add multiple items in one dict
    def __add__(self, obj):
        new_dict = {}

        for key, value in self.shopping_list.items():
            new_dict[key] = value

        for key, value in obj.shopping_list.items():

            if key in self.shopping_list:
                new_dict[key] = new_dict[key] + value
            else:
                new_dict[key] = value

        return new_dict


will_items = ShoppingList(Apple=4, Pie=2, Mango=23, grape=24)
ryan_items = ShoppingList(Pear=20, Pie=2, Orange=20)
print(len(will_items))
print(str(will_items))
print(will_items + ryan_items)
