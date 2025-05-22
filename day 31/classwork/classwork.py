# ცვლადში შენახული საკუთარი სახელი
my_name = "giorgi"

# მომხმარებლის მიერ შემოტანილი სახელი
user_name = input("შეიყვანე შენი სახელი: ")

# შევადაროთ სახელები lower() ფუნქციის გამოყენებით
if my_name.lower() == user_name.lower():
    print("True")
else:
    print("False")
