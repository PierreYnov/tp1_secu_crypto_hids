import hashlib

question = input("Entrez le nom du fichier (avec sa direction si il n'est pas la) : ")

# Fichier BDD
hasher1 = hashlib.md5()
afile1 = open(question, 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a = (str(hasher1.hexdigest()))
hash_fichier = str(md5_a)
print(hash_fichier)

# Lecture du Hash de l'ancienne BDD
f = open("myfile.txt", "r")

hash_bdd_orig = f.read()
print(hash_bdd_orig)

# Compare md5
if hash_fichier == hash_bdd_orig:
    print("C'est le même hash, vous pouvez lancer le fichier")
else:
    print("Non arrêtez tout !")
