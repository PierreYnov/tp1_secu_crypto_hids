import hashlib

question = input("Entrez le nom du fichier (avec sa direction si il n'est pas la) : ")

hasher2 = hashlib.md5()
afile2 = open(question, 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b = (str(hasher2.hexdigest()))

file1 = open('myfile.txt', 'w')
file1.writelines(md5_b)
file1.close()

