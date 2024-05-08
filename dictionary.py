#Contoh cara membuat Dictionary pada Python

#dict = {'Name': 'Azzam', 'Age': '16', 'Class': '1 intensif', 'District': 'sidoarjo'}#
#print ("dict['Name']: ", dict['Name'])
#print ("dict['Age']: ", dict['Age'])
#print ("dict['Class']:", dict['Class'])
#print (dict) 

Biodata = {'Name': 'Yusuf', 'Age': 7, 'Class': 'First'}
Biodata['Name'] = "Yusuf"; # Mengubah entri yang sudah ada
Biodata['School'] = "Pesantren teknologi majapahit" # Menambah entri baru

print ("Biodata['Age']: ", Biodata['Age'])
print ("Biodata['School']: ", Biodata['School'])
print (Biodata)

del Biodata['Age']
print(Biodata)
Biodata.clear()
print(Biodata)
del Biodata
print(Biodata)