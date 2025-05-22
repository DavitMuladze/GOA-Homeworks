# --- სტრინგის ფუნქციები ---
# .lower() - გადაყავს სტრინგი პატარა ასოებში
# .upper() - გადაყავს სტრინგი დიდ ასოებში
# .capitalize() - მხოლოდ პირველი ასო გადაჰყავს დიდ ასოდ
# .strip() - აშორებს ცარიელ სივრცეს (space) სტრინგის დასაწყისიდან და ბოლოდან
# .replace(old, new) - ცვლის ტექსტში სიმბოლოს ან ნაწილის სხვით
# .find(word) - აბრუნებს სტრინგში მონაწილის პირველ ინდექსს (თუ ვერ იპოვის, აბრუნებს -1)
# .startswith() - ამოწმებს იწყება თუ არა სტრინგი კონკრეტული ასოთი/ნაწილით
# .endswith() - ამოწმებს მთავრდება თუ არა სტრინგი კონკრეტული ასოთი/ნაწილით
# len() - აბრუნებს სტრინგის სიგრძეს

# --- სიის (list-ის) ფუნქციები ---
# .append() - სიას ამატებს ახალ ელემენტს ბოლოში
# .pop() - შლის ელემენტს სიიდან (ბოლოსას ან მითითებული ინდექსის)
# .remove(value) - შლის კონკრეტულ მნიშვნელობას სიიდან
# .insert(index, value) - ამატებს ელემენტს კონკრეტულ ადგილას
# .clear() - აცარიელებს მთელ სიას
# .sort() - ალაგებს სიას ზრდადობით
# .reverse() - აბრუნებს სიის მიმდევრობას უკუღმა
# len() - აბრუნებს სიის სიგრძეს (ელემენტების რაოდენობას)


my_surname = "Muladze"
user_surname = input("შეიყვანე შენი გვარი: ")

if my_surname.lower() == user_surname.lower():
    print("Our surnames are similar.")
else:
    print("We have different surnames.")


# არაჯანსაღი საკვების სია
food = ["burger", "fries", "pizza", "soda"]

# .pop() — ვშლით არაჯანსაღ საკვებს
food.pop()        # შლის "soda"
food.pop(0)       # შლის "burger"

# .append() — ვამატებთ ჯანსაღ საკვებს
food.append("salad")
food.append("fruit")

# საბოლოო შედეგის დაბეჭდვა
print(food)
# ['fries', 'pizza', 'salad', 'fruit']


my_name = "Dato"
user_name = input("შეიყვანე შენი სახელი: ")

# ვადარებთ Case-insensitive რეჟიმში
my_name = my_name.lower()
user_name = user_name.lower()

if my_name[0] == user_name[0] and my_name[-1] == user_name[-1]:
    print(2)
elif my_name[0] == user_name[0] or my_name[-1] == user_name[-1]:
    print(1)
else:
    print(0)
