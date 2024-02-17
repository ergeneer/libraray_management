import time
from Library_Management_System import Library  # Library sınıfını içe aktarıyoruz

lib = Library() # Oluşturdugum sınıftan nesne oluşturdum ve bu nesne ile aşağı devam ediyorum.

time.sleep(1)
print("Please Waiting...")
time.sleep(1)

print("""
╔═══════════════════════════ MENU ═══════════════════════════╗
║                       1. List Books                        ║
║                       2. Add Book                          ║
║                       3. Remove Book                       ║
║                       4. Update Book Information           ║
║                       5. Quit                              ║
╚══════════════════════════════════════════════════════════=═╝
""")
print("Please enter input from 1 to 5")


devam = True

while devam:
    time.sleep(1)
    choice = input("Enter your choice:")
    time.sleep(1)
    if choice == "1":
        print("Please waiting...")
        time.sleep(1)  # programımız 1 saniye beklesin.
        lib.list_books()
    elif choice == "2":
        print("Please waiting...")
        time.sleep(1)
        lib.add_book()
        time.sleep(1)
    elif choice == "3":
        print("Please waiting...")
        time.sleep(1)
        lib.remove_book()
        time.sleep(1)
    elif choice == "4":
        print("Please waiting...")
        time.sleep(1)
        lib.change_book_information()
        time.sleep(1)
    elif choice == "5":
        print("Please waiting...")
        time.sleep(1)
        print("Exiting the program...Good Bye :)")
        time.sleep(1)
        lib.to_ext()
        devam = False
    else:
        time.sleep(1)
        print("Invalid choice.Please choose from 1 to 5.")
        time.sleep(1)
        print("To Main Menu...")
        time.sleep(1)
