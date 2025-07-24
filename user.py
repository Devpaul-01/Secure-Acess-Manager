import json
import os

class User:
    def __init__(self, name, role, pin):
        self.name = name
        self.pin = pin
        self.role = role

    def register(self):
        details = {
            "name": self.name,
            "role": self.role,
            "pin": self.pin
        }
        folder_name = "Secret Users"
        file_name = f"{self.name}.json"
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        with open(file_path, "w") as file:
            json.dump(details, file, indent=4)
            print("User registered successfully")

    @staticmethod
    def login(name, pin, role):
        file_name = f"{name}.json"
        folder_name = "Secret Users"
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                details = json.load(file)
                sav_pass = details["pin"]
                if pin == sav_pass:
                    print("Login successful")
                    print(details)
                    return True
                else:
                    print("Incorrect password")
        else:
            print("User not found")
        return False

    @staticmethod
    def verify_pin(name, role, pin):
        def check(pin):
            if not pin.isdigit():
                return None
            digits = [int(d) for d in pin]
            return pin if len(digits) == 4 else None

        def unique_test(pin):
            digits = [int(d) for d in pin]
            return pin if len(set(digits)) == 4 else None

        def palindrome_check(pin):
            return pin if pin != pin[::-1] else None

        def num_test(pin):
            digits = [int(d) for d in pin]
            return pin if digits[0] + digits[3] == digits[1] + digits[2] else None

        def division_test(pin):
            digits = [int(d) for d in pin]
            return pin if sum(digits) % 3 == 0 else None

        def even_test(pin):
            digits = [int(d) for d in pin]
            for i in range(3):
                if digits[i] % 2 == 0 and digits[i + 1] % 2 == 0:
                    return None  # failed test
            return pin  # passed

        if (check(pin) and unique_test(pin) and palindrome_check(pin)
            and num_test(pin) and division_test(pin) and even_test(pin)):
            return name, role, pin
        return None

    @staticmethod
    def check_lock(name, pin, role):
        file_name = f"{name}.json"
        folder_name = "Locked Users"
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            return None
        return True

    @staticmethod
    def lock_user(name, pin, role):
        new_folder = "Locked Users"
        file_name = f"{name}.json"
        folder_name = "Secret Users"
        file_path = os.path.join(folder_name, file_name)
        new_path = os.path.join(new_folder, file_name)

        if os.path.exists(file_path):
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
            with open(file_path, "r") as file:
                details = json.load(file)
            with open(new_path, "w") as file:
                json.dump(details, file, indent=4)
                print("User locked successfully")

class Admin:
    def __init__(self, pin="admin"):
        self.pin = pin

    def admin_login(self, password):
        if password == self.pin:
            folder_name = "Secret Users"
            new_folder = "Locked Users"
            print("Welcome to the admin section")
            secret_users = os.listdir(folder_name) if os.path.exists(folder_name) else []
            locked_users = os.listdir(new_folder) if os.path.exists(new_folder) else []

            if secret_users:
                print("Registered Users:")
                for user in secret_users:
                    print("-", user)
            else:
                print("No users at the moment")

            if locked_users:
                print("Locked Users:")
                for user in locked_users:
                    print("-", user)
            else:
                print("No locked users")
            return True
        else:
            print("Incorrect admin password")
            return False

    @staticmethod
    def add_user(name, pin, role):
        file_name = f"{name}.json"
        folder_name = "Secret Users"
        details = {"name": name, "pin": pin, "role": role}
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            json.dump(details, file, indent=4)
            print("User added successfully")

    @staticmethod
    def unlock_user(name):
        file_name = f"{name}.json"
        folder_name = "Locked Users"
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print("User removed from locked list successfully")
        else:
            print("User not in locked list")