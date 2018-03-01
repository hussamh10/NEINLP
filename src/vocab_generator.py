
file_path = "..\\data\\test"

file = open(file_path, 'r')
data = file.read()

data = data.encode('ascii',"ignore")
data = data.decode('ascii',"ignore")
data = str(data)

file.close() 

file = open("ok", 'w')
file.write(data)
file.close() 
