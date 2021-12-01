class Library:
    def __init__(self, name, genre, year, author):
        self.name=name
        self.grade=genre
        self.year=year
        self.author=author

booka = ("Nineteen Eighty-Four","social science fiction","1949","George Orwell")
bookb = ("The Alchemist","fantasy","1988","Paulo Coelho")

print("Домашня бібліотека")

while True:
    print("1. Бібліотека.\n2. Пошук.\n3. Додати книгу.\n4. Видалити книгу.\n5. Вихід.\n")
    userInput = str(input())

    if userInput == "1":
        print(booka)
        print(bookb)
        
    elif userInput == "2":
        while True:
            choice = input("Пошук книги за допомогою...\n1. name.\n2. genrе.\n3. year.\n4. author.\n")
            if choice == "1":
                while True:
                    choice = input("Уведіть дані для пошуку.\n")
                    if choice == "Nineteen Eighty-Four":
                        print("social science fiction","1949","George Orwell")
                    else:
                        print("Уведіть дані для пошуку.")
                        if choice == "The Alchemist":
                            print("fantasy","1988","Paulo Coelho")
            if choice == "2":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == "social science fiction":
                        print("Nineteen Eighty-Four","1949","George Orwell")
                    else:
                        print("Уведіть дані для пошуку.")
                        if choice == "fantasy":
                            print("The Alchemist","1988","Paulo Coelho")
            if choice == "3":
                while True:
                    choice = input("Уведіть дані для пошуку.\n")
                    if choice == "1949":
                        print("Nineteen Eighty-Four","social science fiction","George Orwell")
                    else:
                        print("Уведіть дані для пошуку")
                        if choice == "1988":
                            print("The Alchemist","fantasy","Paulo Coelho")
            if choice == "4":
                while True:
                    choice = input("ВВедіть дані для пошуку.\n")
                    if choice == "George Orwell":
                        print("Nineteen Eighty-Four","social science fiction","1949")
                    else:
                        print("ВВедіть дані для пошуку.")
                        if choice == "Paulo Coelho":
                            print("The Alchemist","fantasy","Paulo Coelho","1988")
                    
                        
    elif userInput == "3":
        print("Додайте книгу.")
        filename = input()
        print("Операція успішна.")
    elif userInput == "4":
        import os
        os.remove(" D:\\booktext.txt")
    elif userInput == "5":
        break