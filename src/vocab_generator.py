file_path = "..\\data\\normalized_whatsapp"
file = open(file_path, 'r', encoding='utf8')
data = file.read().lower()
file.close()

data = data.encode('ascii',"ignore")
data = data.decode('ascii',"ignore")
data = str(data)

data = data.split()
print(data.__len__())
unique_words = set(data)
data = ""
for word in unique_words:
    data += word + '\n'

file_path = "..\\data\\vocab"

file = open(file_path, 'w')
file.write(data)
