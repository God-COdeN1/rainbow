base = {}
while True:
    i = input("1 для регістрації, 2 для входу ")
    if i == "1":
        login = input("Логін: ")
        pasword = input("Пароль: ")
        if login in base:
            print("Користувач існує")
        else:
            base[login] = pasword
            print("Регістрація успішна")
            print(base)
    elif i == "2":
        login = input("Логін: ")
        if login in base:
            pasword = input("Пароль: ")
            if pasword == base[login]:
                print("Вхід успішний")
            else:
                print("Пароль не вірний")
        else:
            print("Добавте користувача")