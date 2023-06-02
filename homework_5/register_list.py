login = []
password = []
while True:
    i = input("Ведіть 1 для входу, 2 для регістрації: ")
    if i == "1":
        inp_lg = str(input("Ведіть логін: "))
        if inp_lg in login:
            inp_pass = str(input("Ведіть пароль: "))
            if inp_pass == password[login.index(inp_lg)]:
                print("Вхід здійснено")
                pr = True
                while pr:
                    print("1-вихід \n2-змінити пароль \n3-видалити акаунт")
                    i1 = input()
                    if i1 == "1":
                        pr = False
                    elif i1 == "2":
                        new_pass = str(input("Новий пароль: "))
                        pass_ver = str(input("Підтвердіть пароль: "))
                        # password[login.index(inp_lg)] = new_pass if new_pass == pass_ver else print("Паролі не
                        # співпадають")
                        if new_pass == pass_ver:
                            print("Пароль змінено")
                            password[login.index(inp_lg)] = new_pass
                        else:
                            print("Паролі не співпадають")
                    elif i1 == "3":
                        user_index = login.index(inp_lg)
                        login.pop(user_index)
                        password.pop(user_index)
                        print("Акаунт видалено")
                        pr = False
                    else:
                        print("Натисніть кнопку від 1 до 3")
            else:
                print("Пароль не вірний")
        else:
            print("Такого користувача не знайдено")
    elif i == "2":
        inp_lg = str(input("Ведіть новий логін: "))
        if inp_lg in login:
            print("Такий логін вже є")
        else:
            login.append(inp_lg)
            inp_pass = str(input("Ведіть новий пароль: "))
            password.append(inp_pass)
    else:
        print("Натисніть 1 або 2")
    print(login, password)
