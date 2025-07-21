class Password:
    def __init__(self, password):
        self.__password = password  # Private variable
        print("Password set successfully.")

    def set_password(self, new_password):
        self.__password = new_password  # Public method

    def __check_password(self, password):  # 🔒 Private method
        return self.__password == password

    def verify_password(self, password):  # ✅ Public interface to use the private method
        return self.__check_password(password)

    def get_password(self):
        return self.__password


# Create first user
s1 = Password("Nihar@123")
print("PASSWORD SET:", s1.get_password())

s1.set_password("Nihar@456")

# ✅ Uses public method that internally calls the private one
print("Password correct?", s1.verify_password("Nihar@456"))

print("CURRENT PASSWORD:", s1.get_password())

s2 = Password("Tarun@123")

del s2  # Delete the object to free up memory

print("PASSWORD SET:", s2.get_password())




