# Квадратичне зондування (quadratic probing)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        i = 0

        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:  # Оновлення значення, якщо ключ вже існує
                self.table[(index + i**2) % self.size] = (key, value)
                return
            i += 1
            if i == self.size:  # Якщо вся таблиця заповнена
                raise Exception("Hash table is full")

        self.table[(index + i**2) % self.size] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        i = 0

        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:
                return self.table[(index + i**2) % self.size][1]
            i += 1
            if i == self.size:  # Якщо перебрали всю таблицю
                break

        return None  # Якщо елемент не знайдено

    def delete(self, key):
        index = self.hash_function(key)
        i = 0

        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:
                self.table[(index + i**2) % self.size] = None  # Видаляємо елемент
                return True
            i += 1
            if i == self.size:
                break

        return False  # Якщо елемент не знайдено

    def display(self):
        for i, pair in enumerate(self.table):
            print(f"{i}: {pair}")

# 🔹 Тестування
ht = HashTable(10)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)
ht.insert("orange", 400)
ht.display()

print("Search apple:", ht.search("apple"))
ht.delete("banana")
ht.display()
