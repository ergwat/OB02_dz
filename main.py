class User():
    def __init__(self, id, name, access):
        self.__id = id
        self.__name = name
        self.__access = "user"

    def user_info(self):
        return self.__id, self.__name, self.__access


class Admin(User):
    def __init__(self, id, name, access):
        super().__init__(id, name, access)
        self.__access = 'admin'
    def add_user(self, id, name, access):
        users.append(User(id, name, access))

    def remove_user(self, id):
        for user in users:
            if user.user_info()[0] == id:
                users.remove(user)
                break


admin1=Admin(1, 'admin1', 'admin') # создаем админа
users = []
admin1.add_user(2, 'user1_by_admin1', 'user') # добавляем юзера через админа
user2 = User(3, 'user2_directly', 'user') # создаем юзера напрямую
admin1.add_user(4, 'user3_by_admin', 'user') # добавляем юзера через админа
user3 = User(5, 'user4_directly', 'user') # создаем юзера напрямую
admin1.add_user(6, 'admin2_by_admin1', 'admin') # добавляем второго админа через админа. При этом создастся юзер, а не админ, т.к. при создании юзера жестко прописан юзерский доступ
admin1.add_user(7, 'admin3_by_admin2', 'admin') # добавляем третьего админа через админа

for user in users:
    print(user.user_info())

print("\nУдаляем пользователя №4 \n")
admin1.remove_user(4)

for user in users:
    print(user.user_info())