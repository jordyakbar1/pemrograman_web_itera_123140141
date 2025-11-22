from abc import ABC, abstractmethod

# ABSTRACT CLASS
class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.__item_id = item_id     # private
        self._title = title          # protected

    @property
    def item_id(self):
        return self.__item_id

    @property
    def title(self):
        return self._title

    @abstractmethod
    def display_info(self):
        pass


# SUBCLASS BOOK
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display_info(self):
        print(f"BOOK     | ID: {self.item_id} | {self.title} | Author: {self.author}")


# SUBCLASS MAGAZINE
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)
        self.issue = issue

    def display_info(self):
        print(f"MAGAZINE | ID: {self.item_id} | {self.title} | Issue: {self.issue}")


# LIBRARY CLASS
class Library:
    def __init__(self):
        self.__items = []   # private list

    def add_item(self, item):
        self.__items.append(item)
        print("\nItem berhasil ditambahkan!\n")

    def show_items(self):
        if not self.__items:
            print("\nTidak ada item dalam perpustakaan.\n")
            return
        print("\n=== DAFTAR ITEM PERPUSTAKAAN ===")
        for item in self.__items:
            item.display_info()
        print()

    def search(self, keyword):
        print(f"\nHasil pencarian untuk '{keyword}':")
        found = False
        for item in self.__items:
            if keyword.lower() in item.title.lower() or keyword == str(item.item_id):
                item.display_info()
                found = True
        if not found:
            print("Item tidak ditemukan.")
        print()



def main():
    library = Library()

    while True:
        print("==== MENU PERPUSTAKAAN ====")
        print("1. Tambah Item")
        print("2. Tampilkan Semua Item")
        print("3. Cari Item")
        print("4. Keluar")

        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            print("\nTambah Item:")
            print("1. Book")
            print("2. Magazine")
            tipe = input("Pilih tipe item (1/2): ")

            item_id = input("Masukkan ID: ")
            title = input("Masukkan Judul: ")

            if tipe == "1":  # Book
                author = input("Masukkan Author: ")
                item = Book(item_id, title, author)
                library.add_item(item)

            elif tipe == "2":  # Magazine
                issue = input("Masukkan Issue Number: ")
                item = Magazine(item_id, title, issue)
                library.add_item(item)

            else:
                print("Tipe item tidak valid.\n")

        elif choice == "2":
            library.show_items()

        elif choice == "3":
            keyword = input("Masukkan judul atau ID untuk dicari: ")
            library.search(keyword)

        elif choice == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
