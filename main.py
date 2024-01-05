class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_name(self):
        '''Mengembalikan nama kontak'''
        return self.name

    def get_phone(self):
        '''Mengembalikan nomor telepon kontak'''
        return self.phone

    def __str__(self):
        return f'{self.name:<10} : {self.phone}'

class ContactList:
    def __init__(self):
        '''Variabel daftar kontak dari fungsi init sebagai List.'''
        self.contacts = []

    def add_contact(self, contact):
        '''Menambahkan kontak ke dalam daftar kontak'''
        self.contacts.append(contact)

    def delete_contact(self, name):
        '''Menghapus kontak berdasarkan nama'''
        for hapus in self.contacts:
            if hapus.get_name() == name:
                self.contacts.remove(hapus)
                print(f'Kontak {name} telah dihapus.')
                return
        print('Kontak tidak ditemukan.')

    def search_contact(self, name):
        '''Mencari kontak berdasarkan nama'''
        for cari in self.contacts:
            if cari.get_name() == name:
                nomor = cari.get_phone()
                print(f'\nKontak {name} ditemukan dengan nomor: {nomor}')
                return
        print('Kontak tidak ditemukan.')
            
    def display_contacts(self,urutan):
        '''Menampilkan semua kontak dalam daftar'''
        if self.contacts:
            if urutan == 'abjad':
                abjad = sorted(self.contacts, key=lambda x: x.get_name())
                print('\nDaftar kontak:')
                [print(i) for i in abjad]
            elif urutan == 'terbaru':
                terbaru = reversed(self.contacts)
                print('\nDaftar kontak:')
                [print(i) for i in terbaru]
            elif urutan == 'terlama':
                print('\nDaftar kontak:')
                [print(i) for i in self.contacts]
            else:
                print('Input yang Anda masukkan tidak sesuai')
        else:
            print('Kontak kosong')

# Membuat objek daftar kontak
contact_list = ContactList()

while True:
    print('\nMenu:')
    print('1. Tambahkan kontak.')
    print('2. Hapus kontak.')
    print('3. Cari kontak.')
    print('4. Tampilkan semua kontak.')
    print('5. Selesai.')

    choice = input('Pilih menu: ')

    if choice == '1':
        name = input('Masukkan nama kontak: ')
        phone = input('Masukkan nomor telepon kontak: ')
        # Panggil metode untuk menambah kontak
        contact = Contact(name.lower(), phone)
        contact_list.add_contact(contact)
        print(f'Kontak {name} telah ditambahkan.')

    elif choice == '2':
        name = input('Masukkan nama kontak yang akan dihapus: ')
        # Panggil metode untuk menghapus kontak berdasarkan nama
        contact_list.delete_contact(name.lower())

    elif choice == '3':
        name = input('Masukkan nama kontak yang akan dicari: ')
        # Panggil metode untuk mencari kontak berdasarkan nama
        contact_list.search_contact(name.lower())

    elif choice == '4':
        tampilan = input('Tampilkan menurut?(abjad/terbaru/terlama): ')
        # Panggil metode untuk menampilkan semua kontak
        contact_list.display_contacts(tampilan.lower())

    elif choice == '5':
        print('Terima kasih! Program selesai.')
        break

    else:
        print('Pilihan tidak valid. Silakan pilih menu yang sesuai.')
