#Captone Module 1
#Riko Yoga Pratama
# Perpustakaan - Manajemen Peminjaman Buku

books = []
loans = []

def display_books():
    if not books:
        print("Tidak ada buku yang tersedia.")
    else:
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book['title']} - {book['author']} (ID: {book['id']})")

def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan penulis buku: ")
    book_id = len(books) + 1
    books.append({'id': book_id, 'title': title, 'author': author})
    print("Buku berhasil ditambahkan.")

def update_book():
    display_books()
    book_id = int(input("Masukkan ID buku yang ingin diperbarui: "))
    for book in books:
        if book['id'] == book_id:
            book['title'] = input(f"Masukkan judul baru (sebelumnya: {book['title']}): ")
            book['author'] = input(f"Masukkan penulis baru (sebelumnya: {book['author']}): ")
            print("Data buku berhasil diperbarui.")
            return
    print("Buku tidak ditemukan.")

def delete_book():
    display_books()
    book_id = int(input("Masukkan ID buku yang ingin dihapus: "))
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print("Buku berhasil dihapus.")
            return
    print("Buku tidak ditemukan.")

def loan_book():
    display_books()
    book_id = int(input("Masukkan ID buku yang ingin dipinjam: "))
    for book in books:
        if book['id'] == book_id:
            if book_id in [loan['book_id'] for loan in loans]:
                print("Buku ini sedang dipinjam.")
            else:
                borrower = input("Masukkan nama peminjam: ")
                loans.append({'book_id': book_id, 'borrower': borrower})
                print("Buku berhasil dipinjam.")
            return
    print("Buku tidak ditemukan.")

def return_book():
    book_id = int(input("Masukkan ID buku yang ingin dikembalikan: "))
    for loan in loans:
        if loan['book_id'] == book_id:
            loans.remove(loan)
            print("Buku berhasil dikembalikan.")
            return
    print("Buku tidak ditemukan atau tidak sedang dipinjam.")

def main_menu():
    while True:
        print("\nPerpustakaan - Manajemen Peminjaman Buku")
        print("1. Tampilkan data buku")
        print("2. Tambah buku")
        print("3. Perbarui data buku")
        print("4. Hapus buku")
        print("5. Pinjam buku")
        print("6. Kembalikan buku")
        print("7. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            display_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            loan_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            print("Terima kasih telah menggunakan sistem peminjaman buku.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main_menu()
