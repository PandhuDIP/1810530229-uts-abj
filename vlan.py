f = open('vlan-database.txt', 'w')
while True:
    ch = input("Input Data VLAN Baru (y/t)? ")
    if ch == 'y' or ch == 'Y':
        print("*" * 60)
        idvlan = input("Masukkan VLAN ID: ")
        nvlan = input("Masukkan Nama VLAN: ")
        f.write(str("VLAN ID: "+idvlan+", Name: "+nvlan) + '\n')
        print("-" * 60)
    elif ch == 't' or ch == 'T':
        f.close()
        f = open('vlan-database.txt', "r")
        print (f.read())
        break
    else :
        print("Invalid Command")
