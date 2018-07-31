
# """------7--------------------"""


def common_values(list1, list2):

    starts_match = list1[0] == list2[0]
    ends_match = list1[-1] == list2[-1]

    return starts_match and ends_match


print(common_values([1, 4, 5, 6], [1, 3, 5, 6]) )

# --------8------------


def html_tag(text, tag):
    return '<{}>{}</{}>'.format(tag, text, tag)


print(html_tag('My Title', 'title'))
print(html_tag('bold title', 'title'))


# -----9----------------


"""global variable"""

largest_number = 0


def set_largest_number(list_):

    global largest_number
    largest = 0

    for number in list_:
        if number > largest:
            largest = number

    largest_number = largest
    print(largest_number)

    #return largest_number


set_largest_number([23, 45, 66, 77, 88])
print(largest_number)
