# Разработай систему управления учетными записями пользователей для небольшой компании.

# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и
# удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "user"
    def get_user_id(self):
        return self._user_id
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def  set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = "admin"
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список")
        print(user_list)
    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь удален из списка")
        print(user_list)

users = []
admin = Admin("a1", "Григорий")
user2 = User("u2", "Семен Семеныч")

print(user2.get_name())
admin.add_user(users, user2)

print(admin.get_name())
user1 = User("u1", "Сара Абрамовна")
print(user1.get_name())
admin.add_user(users, user1)

user3 = User("u3", "от Иван Иваныча")
print(user3.get_name())
admin.add_user(users, user3)
admin.remove_user(users, user2)