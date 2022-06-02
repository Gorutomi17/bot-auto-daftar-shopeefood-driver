import requests, json, re, time, os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from lxml import html

ua = UserAgent(verify_ssl=False)

r = requests.Session()

os.system('cls')

time.sleep(1)
print(""" $$$$$$\  $$\   $$\ $$$$$$$$\  $$$$$$\        $$$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$ |  $$ |\__$$  __|$$  __$$\       $$  __$$\ $$  __$$\ $$  _____|\__$$  __|$$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |   $$ |   $$ /  $$ |      $$ |  $$ |$$ /  $$ |$$ |         $$ |   $$ /  $$ |$$ |  $$ |
$$$$$$$$ |$$ |  $$ |   $$ |   $$ |  $$ |      $$ |  $$ |$$$$$$$$ |$$$$$\       $$ |   $$$$$$$$ |$$$$$$$  |
$$  __$$ |$$ |  $$ |   $$ |   $$ |  $$ |      $$ |  $$ |$$  __$$ |$$  __|      $$ |   $$  __$$ |$$  __$$< 
$$ |  $$ |$$ |  $$ |   $$ |   $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |         $$ |   $$ |  $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |   $$ |    $$$$$$  |      $$$$$$$  |$$ |  $$ |$$ |         $$ |   $$ |  $$ |$$ |  $$ |
\__|  \__| \______/    \__|    \______/       \_______/ \__|  \__|\__|         \__|   \__|  \__|\__|  \__|
 $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\        
$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  _____|$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$\       
$$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ /  $$ |$$ /  $$ |$$ |  $$ |      
\$$$$$$\  $$$$$$$$ |$$ |  $$ |$$$$$$$  |$$$$$\    $$$$$\    $$$$$\    $$ |  $$ |$$ |  $$ |$$ |  $$ |      
 \____$$\ $$  __$$ |$$ |  $$ |$$  ____/ $$  __|   $$  __|   $$  __|   $$ |  $$ |$$ |  $$ |$$ |  $$ |      
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      
\$$$$$$  |$$ |  $$ | $$$$$$  |$$ |      $$$$$$$$\ $$$$$$$$\ $$ |       $$$$$$  | $$$$$$  |$$$$$$$  |      
 \______/ \__|  \__| \______/ \__|      \________|\________|\__|       \______/  \______/ \_______/       
$$$$$$$\  $$$$$$$\  $$$$$$\ $$\    $$\ $$$$$$$$\ $$$$$$$\                                                 
$$  __$$\ $$  __$$\ \_$$  _|$$ |   $$ |$$  _____|$$  __$$\                                                
$$ |  $$ |$$ |  $$ |  $$ |  $$ |   $$ |$$ |      $$ |  $$ |                                               
$$ |  $$ |$$$$$$$  |  $$ |  \$$\  $$  |$$$$$\    $$$$$$$  |                                               
$$ |  $$ |$$  __$$<   $$ |   \$$\$$  / $$  __|   $$  __$$<                                                
$$ |  $$ |$$ |  $$ |  $$ |    \$$$  /  $$ |      $$ |  $$ |                                               
$$$$$$$  |$$ |  $$ |$$$$$$\    \$  /   $$$$$$$$\ $$ |  $$ |                                               
\_______/ \__|  \__|\______|    \_/    \________|\__|  \__|                                               
                                                                                                          
                                                                                                          
                                                                                                          """)

time.sleep(1)
print("_Made By MrHecka_\n")


def daftar():
    of = open('data.txt','r').readline()
    datas = of.split(':')
    url = "https://survey.alchemer.com/s3/6406341/Formulir-Pendaftaran-Driver-ShopeeFood"

    hd = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "origin":"https://survey.alchemer.com",
        "referer":"https://survey.alchemer.com/s3/6406341/Formulir-Pendaftaran-Driver-ShopeeFood",
        "user-agent": ua.random
    }

    body = {
        "sg_currentpageid": "3",
        "sgE-6406341-3-3": datas[0],
        "sgE-6406341-3-4": datas[1],
        "sgE-6406341-3-5": datas[2],
        "sgE-6406341-3-6": datas[3],
        "sgE-6406341-3-7": "10056",
        "sGizmoNextButton": "Next"
    }


    # ISI PAGE 1 DAFTAR SHOPEEFOOD DRIVER
    isi1 = r.post(url, headers=hd, data=json.dumps(body))

    # AMBIL SESI ISI1
    soup1 = BeautifulSoup(isi1.text, 'html.parser')
    findsesi1 = str(soup1.find_all('script')[3])
    session = re.search('"session": \"(.*?)\"', findsesi1).group(1)
    id1 = re.search(r'"id": [^,]*', findsesi1).group(0).replace('"id": ', '')

    # MASUKKAN PAGE 2
    body2 = {
    "sg_currentpageid": "3",
    "sgE-6406341-3-3": datas[0],
    "sgE-6406341-3-4": datas[1],
    "sgE-6406341-3-5": datas[2],
    "sgE-6406341-3-6": datas[3],
    "sgE-6406341-3-7": "10056",
    "sGizmoNextButton": "Next",
    "sg_currentpageid": "4",
    "sg_surveyident": id1,
    "sg_sessionid": session,
    "sgE-6406341-4-9": datas[4],
    "sgE-6406341-4-8": datas[5],
    "sGizmoSubmitButton": "Submit"
    }

    # LAKUKAN POST DAFTAR KE PAGE 2 DAN TARUH SESI DARI PAGE 1
    isi2 = r.post(url, headers=hd, data=json.dumps(body2))

    # CEK APAKAH BERHASIL GAN?
    gets = html.fromstring(isi2.content)
    cekstatus = gets.xpath('/html/body/form/div[2]/div[2]/div[2]/div/div/strong/span/text()')[0]
    if cekstatus == "Terima kasih atas ketertarikanmu untuk berpartisipasi menjadi Calon Mitra Pengemudi ShopeeFood!":
        time.sleep(1)
        print("===================")
        print("Berhasil Mendaftar!")
        print("===================")
        time.sleep(1)
        print("")
        print("[=]=====DATA DIRI=====[=]")
        print(f"Nama : {datas[0]}\nNomor : {datas[1]}\nJenis Kelamin : {datas[2]}\nEmail : {datas[3]}\nDomisi : {datas[4]}\nTahun Kendaraan : {datas[5]}")
        print("[=]=====DATA DIRI=====[=]")
        print("")
        print(f"Pesan : {cekstatus}")
    else:
        print("GAGAL MENDAFTAR :(")
        print(f"Pesan : {cekstatus}")




# AWAL

tanya1 = input("Mau Ngapain?\n(1) DAFTAR\n(2) RESET DATA DIRI : ")

if tanya1 == "1":
    cekempty = os.path.getsize("data.txt")
    if cekempty == 0:
        print("DATA TERDETEKSI KOSONG, MASUKKAN DATA MANUAL! (HANYA SEKALI)")
        print("")
        nama = input("\nMasukkin Data Diri Nama (Sesuai KTP) : ")
        nomorhp = input("Masukkan Nomor Handphone Anda Yang Aktif Dengan Format (628212xxxxx) : ")
        jk = input("Jenis Kelamin Anda ?\n(1) Laki-Laki\n(2) Perempuan : ")
        jks = None
        jkss = None
        if jk == "1":
            jks = 10005
            jkss = "Laki-Laki"
        elif jk == "2":
            jks = 10006
            jkss = "Perempuan"
        else:
            print("Format Salah, Ulang!")
            jks = None
            jkss = None
            os.system('py botdriver.py')
        email = input("Masukkan Email Anda Yang Aktif : ")
        domisili = input("Masukkan Domisili Tempat Tinggal Anda : ")
        tkendaraan = input("Masukkan Tahun Pembuatan Kendaraan Anda (Isi Dengan Angka) : ")
        print("")
        print("DATA DIRI ANDA :\n")
        print(f"Nama : {nama}\nNomor : {nomorhp}\nJenis Kelamin : {jkss}\nEmail : {email}\nDomisi : {domisili}\nTahun Kendaraan : {tkendaraan}")
        print("")
        benarga = input("Apakah Benar ? (y/n) ")
        if benarga == "y":
            with open('data.txt', 'a') as o:
                o.write(f'{nama}:{nomorhp}:{jks}:{email}:{domisili}:{tkendaraan}')
                print("\nDATA BERHASIL DISIMPAN!")
                print("[!] SILAHKAN JALANKAN ULANG SCRIPT! [!] ")
                time.sleep(5)
                os.system('pause')
        elif benarga == "n":
            print("OKE ULANG!")
            os.system('py botdriver.py')
        else:
            print("FORMAT SALAH! ULANG!!!!")
            os.system('py botdriver.py')
    else:
        print("")
        print("MENDAFTAR....\n")
        time.sleep(1)
        daftar()


elif tanya1 == "2":
    open("data.txt", "w").close()
    print("DATA DIRI BERHASIL DI RESET!")
    os.system('py botdriver.py')
else:
    print("Perintah Salah Ngab, Ulang!")
    os.system('py botdriver.py')




