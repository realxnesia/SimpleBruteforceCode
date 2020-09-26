import requests                                  #ini untuk import module request, yang dipakai buat nanti kirim request ke url
import sys                                       #sys dipakai buat nanti ngambil argumen dari command prompt

url = sys.argv[1]                                #mengambil url dari inputan di command prompt ex=google.com
ext = sys.argv[2]                                #mengambil extension dari inputan di command prompt ex=.pdf
wordlist = "wordlist.txt"                        #masukin wordlist.txt ke variabel wordlist

def write(word):                                 #ini function buat nambahin word kalau ketemu pas brute force
	fp1 = open(wordlist,"a")                     #buka file wordlist, terus actionnya append (menambahkan)
	fp1.write(word +"\n")                        #tulis nama word yang ketemu saat bruteforce, terus print enter biar word berikutnya juga keenter

fp2 = open(wordlist,"r+")                        #buka file wordlist, terus actionnya read and write

for i in range(1000):
	word = fp2.readline().strip()               #readline untuk baca 1 line, strip kalo misalnya di ujung kiri kanan ada spasi, dia hilangin spasinya. 
	temp = url+word+ext                         # buat menggabungkan url/wordlist.ext -> facebook.com/admin.php
	response = requests.get(temp)               # buat coba kirim request ke file temp (url yang sudah dibuat).

	if (response.status_code == 200):           #kalau responsenya 200 (sukses), nanti print status code dan urlnya, terus masukkan ke file wordlist 
		print ("[*] found : ",temp)
		write(word)
	else:
		print ("[*] Not found : ",temp)         #kalau responsenya bukan 200 (gagal), tidak dilakukan apa-apa.
		pass