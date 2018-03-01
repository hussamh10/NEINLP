from tqdm import tqdm

file_path = "..\\data\\whatsapp.txt"

file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()
data = ""

for l in tqdm(lines):
    data += l[23:]

data = data.encode('ascii',"ignore")
data = data.decode('ascii',"ignore")
data = str(data)

file.close() 

file = open("..\\data\\normalized_whatsapp", 'w')

file.write(data)
file.close() 
