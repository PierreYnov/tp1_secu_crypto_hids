import hashlib

path_conf = "/etc/aide/aide.conf"
path_bdd = "/var/lib/aide/aide.db"

hasher2 = hashlib.md5()

# Hash aide.conf
file_conf = open(path_conf, 'rb')
buf2 = file_conf.read()
b = hasher2.update(buf2)
md5_b = (str(hasher2.hexdigest()))
# Hash in txt
aide_txt = open('aide_conf.txt', 'w')
aide_txt.writelines(md5_b)
aide_txt.close()

# Hash aide.db
file_db = open(path_bdd, 'rb')
buf = file_db.read()
b2 = hasher2.update(buf)
md5 = (str(hasher2.hexdigest()))
db_txt = open('db_conf.txt', 'w')
db_txt.writelines(md5)
db_txt.close()

print("HASH 'aide.conf': " + md5_b)
print("HASH 'aide.db': " + md5)
