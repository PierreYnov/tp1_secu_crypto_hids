import hashlib

#question = input("Entrez le nom du fichier (avec sa direction si il n'est pas la) : ")

# Fichier BDD
path_conf = "/etc/aide/aide.conf"
path_db = "/var/lib/aide/aide.db"

hasher2 = hashlib.md5()

# Conf aide
afile1 = open(path_conf, 'rb')
buf1 = afile1.read()
a = hasher2.update(buf1)
md5_a = (str(hasher2.hexdigest()))
hash_fichier_conf = str(md5_a)


# Aide bdd
afile2 = open(path_db, 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b = (str(hasher2.hexdigest()))
hash_fichier_db = str(md5_b)


print("HASH 'aide.conf' : " + hash_fichier_conf)
print("HASH 'aide.db' : " + hash_fichier_db)

# Lecture du Hash de l'ancienne BDD
f = open("aide_conf.txt", "r")
f2 = open("db_conf.txt", "r")


hash_conf_orig = f.read()
hash_bdd_orig = f2.read()

print("")
print("HASH ORIGINE 'aide.conf' : " + hash_conf_orig)
print("HASH ORIGINE 'aide.db' : " + hash_bdd_orig)

# Compare md5
if (hash_fichier_conf == hash_conf_orig) and (hash_fichier_db == hash_bdd_orig) :
    print("Ce sont les mêmes HASH, vous pouvez lancer le fichier")
else:
    print("STOP, fichier corrompu !")
