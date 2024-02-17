# Akbank python bootcamp global aı library management
Projemde ; kullanıcıların kütüphanede bulunan kitapları listeleme, kitap ekleme, kitap silme, kitap bilgilerini güncelleme ve çıkış yapma gibi temel işlevleri gerçekleştirebilmeleri sağlanmaktadır.Kullanıcıdan inputa göre bu işleveler gerçekleştirilir.

Kitap listeme (lists_books) fonksiyonunda kütüphanede kitap mevcut ise kitaplar listelenir yoksa listelenmez.

Kitap ekleme (add_book) fonksiyonu kütüphaneye kitap eklemek için kullanılır.Eğer eklenmek istenen kitap mevcutsa tekrar eklenemez ve kitap eklemek için gerekli olan 4 farklı input'tan (kitap adı , yazar adı , yayınlama yılı , sayfa sayısı) kitap adı bu fonksiyonun içinde alınır , diğer 3 input 3 farklı fonksiyon(yazar_adi_al, kitap_yili_al, sayfa_sayisi_al) cağırılarak alınır.

  yazar_adi_al ile kitap eklerken alınan yazar adı döndürülür.
  kitap_yili_al ile kitap eklerken alınan kitap yılı döndürülür.
  sayfa_sayisi_al fonksiyonu ile kitap eklerken alınan sayfa sayısı döndürülür.

Kitap silme (remove_book) fonksiyonu kütüphaneden kitap silmek için kullanılır.Kütüphanede kitap yoksa uyarı verir.Silinmek istenilen kitabın kütüphanede olup olmadıgına dair kontrol bir fonksiyon cağırılarak (are_you_sure) yapılır.

  are_you_sure fonksiyonu ile kitap silme işlemi için gerekli onay alınır ve buna 
  göre işlem devam eder

Kitap bilgilerini güncelleme fonksiyonu (change_book_information) kütüphanede mevcut olan bir kitabın bilgilerini güncellemek için kullanılır.Kütüphanede olmayan bir kitap güncellenemez.Eğer güncellenmek istelen kitabın yeni adı zaten kütüphanede varsa bu işlem yapılamaz.

show_warning fonksiyonu ile uyarı mesajları yayınlanır.

to_ext fonksiyonu ile sistemden çıkış yapılır.
