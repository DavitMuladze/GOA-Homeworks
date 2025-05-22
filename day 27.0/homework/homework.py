#1
def to_upper(text):
    return text.upper()

# მაგალითი
print(to_upper("გამარჯობა"))  # გამოიტანს: "გamarjoba"

#2
name = input("შეიყვანე შენი სახელი: ")
first_letter_upper = name[0].upper()
print("შენი სახელის პირველი ასოა:", first_letter_upper)

#3
sentence = input("შეიყვანე წინადადება: ")
word_to_find = input("შეიყვანე სიტყვა, რომელიც გინდა მოძებნო: ")

if word_to_find in sentence:
    print(f"სიტყვა '{word_to_find}' მოიძებნა წინადადებაში.")
else:
    print(f"სიტყვა '{word_to_find}' არ მოიძებნა წინადადებაში.")

#4
def format_and_combine(arg1, arg2):
    return arg1.upper() + arg2.lower()

# მაგალითი
print(format_and_combine("hello", "WORLD"))  # გამოიტანს: "HELLOworld"

#5
print("hello".upper())      # HELLO
print("გამარჯობა".upper())  # გამარჯობა (არ ცვლის ქართულში)
print("Test123".upper())    # TEST123
print("python".upper())     # PYTHON
print("MixedCase".upper())  # MIXEDCASE

print("HELLO".lower())      # hello
print("Test123".lower())    # test123
print("PYTHON".lower())     # python
print("მიქსდქეის".lower())  # იგივე დარჩება ქართულში
print("MixedCASE".lower())  # mixedcase

# ვერ აჩვენებს მაგალითებს ავტომატურად, რადგან უნდა შემოიტანოს მომხმარებელმა.
# თუმცა ასე გამოიყურება:
name = input("შეიყვანე სახელი: ")
sentence = input("შეიყვანე წინადადება: ")
word = input("სიტყვა მოსაძებნად: ")
text = input("შეიყვანე ტექსტი: ")

print("cat" in "catalog")       # True
print("dog" in "catalog")       # False
print("რა" in "გაგრა")          # True
print("sun" in "sunshine")      # True
print("moon" in "planet")       # False

print("Hello" + "World")      # HelloWorld
print("Good" + "Morning")     # GoodMorning
print("123" + "456")          # 123456
print("😊" + "🔥")            # 😊🔥
print("Python" + "3")         # Python3
