import os # dosya ve dizin işlemleri için import ettim.
import time # Bazı işlemler 1 saniye bosluk bırakmak için import ettim.
import datetime # yıl için

class Library: # Sorunun istediği gibi class oluşturuyorum
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.reset_file()
    def reset_file(self):
        """
        Eğer dosya mevcutsa, dosyayı siler.
        Daha sonra, dosyayı 'a+' (yazma ve mevcut içeriği koruyarak) modunda açar.

        """
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        self.file = open(self.file_name, "a+")
    def to_ext(self):
        """
        Çıkış yapmak için kullanılır.
        Dosyayı kapatır ve varsa dosyayı siler.
        """
        self.file.close()
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
    def list_books(self):
        """
        Kütüphanedeki kitapları listelemek için kullanılır.
        Eğer kütüphanede kitap mevcut ise , kitap adı ve yazarı olarak listeler.
        Eğer kütüphanede herhangi bir kitap yoksa fonksiyon uyarı verir.
        """
        self.file.seek(0)
        books = self.file.read().splitlines() # txt dosyasın listeliyorum.
        if books:
            print(f"Kütüphanede {len(books)} kitap bulunmaktadır: ")
            for book in books: # kitap listelemek için liste içinde geziniyorum
                time.sleep(0.50)
                print(f"Title: {book.split(',')[0]}, Author: {book.split(',')[1]}")
        else:
            self.show_warning("No books available in the library.") # hata mesajı
    def add_book(self):
        """
        Kütüphaneye kitap eklemek için kullanılır.
        Burada 4 tane input kullanılır.
        Bunlar ;
        kitap adı (book_title) -> string type
        kitap yazarı (book_author) -> string type
        yayınlanma tarihi (year_input) -> date type
        sayfa sayısı (num_pages) -> ınteger type
        Kitap adı kullanıcıdan input olarak alınır ; kalan 3 tanesi 3 farklı fonksiyon çağrılır.

        NOTE :
        Eğer bir kitap zaten mevcutsa, eklenemez.
        Kitap adı ve yazar adı boş girilemez.
        Yazar adı sadece harf içermelidir, rakam içeremez.
        Yayınlanma tarihi geçmiş bir yıl olmalıdır
        Sayfa sayısı pozitif bir tam sayı olmalıdır.
        """
        book_title = input("Please enter the title of the book: ")
        time.sleep(0.25)

        if not book_title.strip(): # kitap adı boş mu diye kontrol edilir.
            self.show_warning("The book title cannot be empty.")
            time.sleep(0.5)
            print("To Main Menu...")
            return

        self.file.seek(0)
        books = self.file.read().splitlines()

        # Eğer daha önceden eklenmiş bir kitap var ise ;
        for book in books:
            if book.split(',')[0] == book_title:
                self.show_warning(f"This book named '{book_title}' has already been added.")
                return

        # Kitap yazarı , yayınlanma yılı ve sayfa sayıları 3 farklı fonksiyon tarafından alınır.
        book_author = self.yazar_adi_al()
        release_year = self.kitap_yili_al()
        num_pages = self.sayfa_sayisi_al()

        # Yukarıda alınan bilgiler txt dosyasına ekleniyor.
        book_details = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_details)
        time.sleep(1)
        print(f"The book named '{book_title}' added successfully.")
    def remove_book(self):
        """
        Kütüphaneden kitap silmek için kullanılır.
        Kullanıcıdan 1 tane input alır.
        Bu ;
        kitap adı (book_title) -> string type

        NOTE:
        Kitap adına göre silme işlemi yapılır.
        Eğer kütüphanede herhangi bir kitap yoksa uyarı mesajı yayınlanır
        Kitap silme işlemi sırasında kullanıcıdan onay alınır.Bunun için "are_you_sure" fonksiyonu çağırılır.
        Silinecek olan kitap yoksa uyarı mesajı yayınlanır.
        """

        self.file.seek(0)
        books = self.file.read().splitlines()

        # Kütüphanede kitap olup olmadıgı kontrolü
        if not books:
            print("There is no book in the library.Therefore,you can not remove anything.")
            return

        book_title = input("Enter the title of the book to remove: ")
        time.sleep(1)

        index_to_remove = None
        found = True # silinmek istenilen kitap yok diyelim ilk olarak
        for index, book in enumerate(books): # silinecek kitabın indexi alınır.
            if book.split(',')[0] == book_title:
                index_to_remove = index
                found = False # silinecek kitap varsa false olur bu sayede alt kısmdanı if bloguna girmez.
                self.are_you_sure(book_title,books,index_to_remove) # kitap silme işleminden once bir işlem doğrulama yapılır.Buradan dönen değere göre silme işlemi yapılır

        if found: # Silinecek olan kitap kütüphanede yoksa burası calısır
            self.show_warning(f"The book named '{book_title}' is not found.Please try again !!")
            time.sleep(0.5)
            print("To Main Menu..")

        self.file.seek(0)
        self.file.truncate() # dosya içeriği silinir.

        for book in books: # Dosyalar tekrardan listedeki kitaplar yazılır.
            self.file.write(book + '\n')
    def change_book_information(self):
        """
        Kütüphanedeki bir kitabın bilgilerini güncellemek için kullanılır.
        Kullanıcıdan kitap adı alınır ve bu kitabın bilgileri güncellenir.

        NOTE:
        Kütüphanede adı olmayan bir kitap güncellenemez, hata mesajı yayınlanır.
        Kitap eklerkenki kurallar aynen geçerlidir (add_book fonksiyonu)
        Güncellenecek olan kitap kütüphanede mevcutsa güncelleme işlemi yapılmaz.
        """
        self.file.seek(0)
        books = self.file.read().splitlines()

        if not books:
            print("No books available in the library. Please first add books !! ")
            return

        book_title = input("Enter the title of the book to change information: ")
        time.sleep(1)

        #girilen kitap var mı ?
        found = False
        for index, book in enumerate(books):
            if book.split(',')[0] == book_title:
                found = True
                # varsa buradan güncelleme işlemine devam

                new_book_title = input("Please enter the new title of the book: ") # yeni kitap adı alınır

                if not new_book_title.strip(): #yeni kitap adı için boş olup olmadıgına bakıyorum
                    self.show_warning("The book title cannot be empty")
                    return

                # yeni kitap yazarı , yeni kitap yılı , yeni kitap sayfası alınır.
                new_book_author = self.yazar_adi_al()
                new_release_year = self.kitap_yili_al()
                new_num_pages = self.sayfa_sayisi_al()

                # Güncellenecek olan kitabın kütüphanede mevcut olup olunmadıgına bakılır.
                for kitap in books:
                    if kitap.split(',')[0] == new_book_title:
                        self.show_warning(f"The book named '{book_title}' is already exists.Please try again !!")
                        return

                # Kitap bilgilerini güncelliyorum
                books[index] = books[index].replace(book_title, new_book_title)
                books[index] = f"{new_book_title},{new_book_author},{new_release_year},{new_num_pages}"
                time.sleep(1)
                print(f"The book information updated successfully.")
                break
        # Güncellenmek istenilen kitap kütüphanede mevcut değilse
        if not found:
            self.show_warning(f"The book named '{book_title}' is not found.Please try again !!")

        # Dosyayı güncelle
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(book + '\n')
    def yazar_adi_al(self):
        """
        add_book fonksiyonunun içinde kullanılır.
        Kitap eklemek için gerekli olan yazar adını döndürür.

        NOTE:
        Yazar adı boşluk olmamalıdır.
        Yazar adı rakam içermemelidir.
        """
        while True:
            book_author = input("Please enter the author of the book: ")
            if not book_author.strip():  # Boşluk kontrolü
                self.show_warning("Author name cannot be empty.Please enter in correct form")
            elif any(char.isdigit() for char in book_author):
                time.sleep(1)
                self.show_warning("Author name cannot contain numeric characters.Please enter in correct form")
            else:
                time.sleep(0.25)
                return book_author
    def kitap_yili_al(self):
        """
        add_book fonksiyonunun içinde kullanılır.
        Kitap eklemek için gerekli olan kitap yayımlanma tarihini döndürür.

        NOTE:
        Kitap yayımlanma tarihi yıl olarak girilmelidir.
        Kitap yayımlanma tarihi bugünün tarihinden ileri olamaz.
         """
        while True: # ValueEror durumundan progrmaın durmaması için try-expect blogu kullandım.
            try:
                year_input = input("Please enter the release year of the book in year format: ")
                release_year = datetime.datetime.strptime(year_input, "%Y").year # girilen inputu date tipine çevirdim
                current_year = datetime.datetime.now().year # bugunun yılını aldım

                # Yayınlanma tarihi bugunun tarihinden ileri mi diye bakıyorum
                if release_year > current_year:
                    self.show_warning("Release year cannot be in the future.Please check your input..")
                    continue
                time.sleep(0.25)
                return release_year
            except ValueError:
                self.show_warning("Please enter a valid year in the format such as 2015")
    def sayfa_sayisi_al(self):
        """
        add_book fonksiyonunun içinde kullanılır.
        Kitap eklemek için gerekli olan kitap sayfa sayısını  döndürür.

        NOTE:
        Kitap sayfa sayısı negatif sayı olamaz.
        Kitap sayfa sayısı integer girilmelidir ; string(elli) ya da float değer girilmemelidir.
         """
        while True:
            try:
                num_pages = int(input("Please enter the number of pages of the book: "))
                if num_pages < 0:
                    self.show_warning("Please enter a non-negative number of pages.")
                    continue
                time.sleep(0.25)
                return num_pages
            except ValueError:
                self.show_warning("Please enter a valid number of pages as a number.")
    def show_warning(self, message):
        """
        Fonksiyonlarda yanlış durumlarda uyarmak için kullanılır.

        NOTE :
        Çok fazla validasyon işlemi olduğu için bu fonksiyon yazıldı
         """
        time.sleep(1)
        print(f"Warning: {message}")
        time.sleep(1)
    def are_you_sure(self, book_title,books,silinecek_index):
        """
        remove_book fonksiyonu içinde kullanılır.
        Kitap silme işlemi için gerekli onay için kullanılır ve silme işlemi yapılır.

        :param book_title: Silinecek kitap adı
        :param books: Kitabın sileceği listemiz (kütüphanemiz)
        :param silinecek_index: Siliencek kitabın indeksi

        NOTE :
        Gerekli onay işlemi için kullanıcıdan input olarak alınır ve buna göre kitap silinir ya da silinmez.

        """
        yes_or_no = input(f"Are you sure you want to remove book named '{book_title}' ? (y/n): ")
        if yes_or_no == "y" or yes_or_no == "Y":
            del books[silinecek_index] # silme işlemi
            time.sleep(1)
            print(f"The book named '{book_title}' removed successfully.")
            time.sleep(1)
            print("To Main Menu...")
            return
        elif yes_or_no == "n" or yes_or_no == "N" :
            time.sleep(0.5)
            print(f"The book named '{book_title}' is not removed")
            time.sleep(0.5)
            print("To Main Menu...")
            time.sleep(0.5)
            return
        else:
            time.sleep(0.50)
            print("Invalid input...Try again...")
            time.sleep(0.50)
            return
