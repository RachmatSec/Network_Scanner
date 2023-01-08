# Mengimpor modul atau pustaka socket
import socket

# Dari modul atau pustaka datetime mengimpor datetime
from datetime import datetime

# Memasukkan alamat IP
ip_address = input ("IP Address : ")

# Inisialisasi untuk membagi digit angka IP
splitted_ip_digits = ip_address.split('.')
dot = '.'

# Memulai membagi tiga digit IP pertama
first_three_ip_digits = splitted_ip_digits[0] + dot + splitted_ip_digits[1] + dot + splitted_ip_digits[2] + dot

# Memasukkan alamat IP pertama atau Host pertama
starting_number = int(input("Starting IP Number: "))

# Memasukkan alamat IP terakhir atau Host terakhir
ending_number = int(input("Ending IP Number: "))

# Waktu mulai scanning
start_time = datetime.now()

# Fungsi menginisialisasi scanning alamat IP
def scan(ip_address):
    # Menginisialisasikan socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # Menghubungkan
    result = sock.connect_ex((ip_address, 135))
    if result == 0:
        return 1
    else:
        return 0

# Fungsi untuk memulai eksekusi atau melakukan scanning pada jaringan yang telah diinisialisasi diatas
def execute():
    for ip in range(starting_number, ending_number):
        ip_address = first_three_ip_digits + str(ip)
        if (scan(ip_address)):
            print (ip_address, "is live")

# Pengembalian pada fungsi execute()
execute()

# Akhir waktu scanning
end_time = datetime.now()

# Menghitung total waktu scanning
total_time = end_time - start_time

# Mencetak total waktu scanning
print("Scanning completed in: ", total_time)