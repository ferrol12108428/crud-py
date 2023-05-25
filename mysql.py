import mysql.connector  

koneksi = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "crud_py"
)

mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1.Lihat User")
    print("2.Tambah User")
    print("3.Ubah User")
    print("4.Hapus User")
    print("5.Keluar")
    print("")
    
    p = int(input("Pilih Menu:"))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("======================")
        print("(id, nama, email, no hp)")
        for x in myresult:
            print(x)
    elif(p == 2):
        nama = input("Nama :")
        email = input("Email :")
        no_hp = input("No Hp :")
        sql = "INSERT INTO user (nama, email, no_hp) VALUES (%s, %s, %s)"
        val = (nama, email, no_hp)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data user berhasil di tambah")
    elif(p == 3):
        id = input("Id USER :")
        mycursor.execute("SELECT * FROM user where id = "+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            nama = input("Nama ("+user[1]+") :") or user [1]
            email = input("Email ("+user[2]+") :") or user [2]
            no_hp = input("No Hp ("+user[3]+") :") or user [3]
            sql = "UPDATE user SET nama=%s,email=%s,no_hp=%s where user_id=%s"
            val = (nama, email, no_hp)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user baerhasil di simpan")
        else:
            print("data tidak ditemukan")
    elif(p == 4):
        id = input("Id User :")
        mycursor.execute("SELECT * FROM user WHERE user_id="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("Menghapus data :", user)
            sql = "DELETE FROM user WHERE id="+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif(p == 5):
        lanjut = False