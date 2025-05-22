def name_to_upper(name):
    result = []
    for char in name:
        result.append(char.upper())
    return result
print(name_to_upper("giorgi"))


def print_list_elements(lst):
    for item in lst:
        print(item)
print_list_elements(["apple", "banana", "cherry"])