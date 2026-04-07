def add_element_to_tuple(_tuple, element, position):
    new_tuple = _tuple[:position] + (element,) + _tuple[position:]
    return new_tuple

_tuple = ('a', 'b', 'd', 'e')
_new_tuple = add_element_to_tuple(_tuple, 'c', 2)


def remove_duplicates(_tuple):
    new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)
    return new_tuple

_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
_new_tuple_2 = remove_duplicates(_tuple)


def remove_duplicates_keep_order(_tuple):
    seen = set()
    new_tuple = []
    for item in _tuple:
        if item not in seen:
            seen.add(item)
            new_tuple.append(item)
    return tuple(new_tuple)

_new_tuple_3 = remove_duplicates_keep_order(_tuple)