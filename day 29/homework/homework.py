def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum_odd_numbers([1, 2, 3, 4, 5]))


def names_with_four_letters(names):
    result = []
    for name in names:
        if len(name) == 4:
            result.append(name)
    return result
print(names_with_four_letters(["Luka", "Nino", "Giorgi", "Ana"]))

def divisible_by_3_and_5(numbers):
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print(num)
divisible_by_3_and_5([10, 15, 30, 7, 45])

name = "Dato"
age = 15

print(f"გამარჯობა, ჩემი სახელი არის {name} და მე ვარ {age} წლის.")