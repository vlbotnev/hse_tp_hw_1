class Contact:
    def __init__(self, s_name, name, f_name, phone, email, id):
        self.s_name = s_name
        self.name = name
        self.f_name = f_name
        self.phone = phone
        self.email = email
        self.id = id

    def info(self):
        print("Фамилия: ", self.s_name)
        print("Имя: ", self.name)
        print("Отчество: ", self.f_name)
        print("Телефон: ", self.phone)
        print("email: ", self.email)
        print("id: ", self.id)
        print("\n")


def snf_search():
    print("Ищем по ФИО:", "Введите имя")
    name_input = input()
    name_check = set(name_input.split())
    f = 0
    for v in range(len(all_contacts)):
        fullname = set()
        fullname.add(all_contacts[v].s_name)
        fullname.add(all_contacts[v].name)
        fullname.add(all_contacts[v].f_name)
        if name_check.issubset(fullname):
            f = 1
            all_contacts[v].info()
    if f == 0:
        print("Такого контакта нет", "\n")


def phone_search():
    print("Ищем по номеру телефона:", "Номер указан?: ", "1)Да", "2)Нет", sep="\n")
    num_phone = int(input())
    f = 0
    if num_phone == 1:
        print("Введите номер")
        phone_input = input()
        for p in range(len(all_contacts)):
            if phone_input == all_contacts[p].phone:
                all_contacts[p].info()
                f = 1
    elif num_phone == 2:
        print("Список контактов без номера:", "\n")
        for m in range(len(all_contacts)):
            if all_contacts[m].phone == "Нет":
                all_contacts[m].info()
                f = 1
    else:
        f = 1
        print("Такой команды нет", "\n")
    if f == 0:
        print("Такого контакта нет", "\n")


def email_search():
    print("Ищем по email:", "Email указан?: ", "1)Да", "2)Нет", sep="\n")
    num_email = int(input())
    f = 0
    if num_email == 1:
        print("Введите email")
        email_input = input()
        for n in range(len(all_contacts)):
            if email_input == all_contacts[n].email:
                all_contacts[n].info()
                f = 1
    elif num_email == 2:
        print("Список контактов без email:", "\n")
        for k in range(len(all_contacts)):
            if all_contacts[k].email == "Нет":
                all_contacts[k].info()
                f = 1
    else:
        f = 1
        print("Такой команды нет", "\n")
    if f == 0:
        print("Такого контакта нет", "\n")


def edit_contact():
    print("Чтобы отредактировать контакт нужно знать его id.",
          "Вы знаете id нужного контакта?: ", "1)Да", "2)Нет", sep="\n")
    num_id = int(input())
    if num_id == 1:
        print("Введите id")
        edit_id_input = int(input())
        for h in range(len(all_contacts)):
            if all_contacts[h].id == edit_id_input:
                all_contacts[h].info()
                print("Введите новую фамилию")
                edit_s_name = input()
                print("Введите новое имя")
                edit_name = input()
                print("Введите новое отчество")
                edit_f_name = input()
                print("Введите новый телефон")
                edit_phone = input()
                print("Введите новый email")
                edit_email = input()
                new_edit_contact = Contact(edit_s_name, edit_name, edit_f_name,
                                           edit_phone, edit_email, all_contacts[h].id)
                all_contacts[h] = new_edit_contact
                print("Контакт редактирован")
    if num_id == 2:
        print("Используйте поиск контактов(2-5) или посмотрите все(1), чтобы узнать id")


print("Введите название бд")
bdn = input()
all_contacts = list()
file = open(bdn)
a = file.read().splitlines()
a = list(filter(None, a))
for i in range(len(a)):
    b = a[i].split(",")
    snf = b[0].split()
    for j in range(3-len(snf)):
        snf.append("Нет")
    if b[1] == '':
        b[1] = "Нет"
    if b[2] == '':
        b[2] = "Нет"
    new_contact = Contact(snf[0], snf[1], snf[2], b[1].replace(" ", ""), b[2].replace(" ", ""), i)
    all_contacts.append(new_contact)

while True:
    print("Введите цифру:", "1)Все контакты", "2)Поиск по ФИО", "3)Поиск по номеру телефона",
          "4)Поиск по email", "5)Контакты без email и номера телефона",
          "6)Редактировать контакт", "7)Закрыть программу", sep="\n")
    num = int(input())
    if num == 1:
        for i in range(len(all_contacts)):
            all_contacts[i].info()
    if num == 2:
        snf_search()
    if num == 3:
        phone_search()
    if num == 4:
        email_search()
    if num == 5:
        print("Список контактов без телефона и email", "\n")
        for i in range(len(all_contacts)):
            if all_contacts[i].email == "Нет" and all_contacts[i].phone == "Нет":
                all_contacts[i].info()
    if num == 6:
        edit_contact()
    if num == 7:
        print("Закрываем")
        break
