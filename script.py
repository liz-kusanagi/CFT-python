import socket
import string

holding_array = []
sending_array = []
para_array = []
line_array = []
word_array = []
data_array = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 10000))
s.send('GET')
data = s.recv(2048)
print(data)

data_array = data.split("\n")
data_array = data_array[:-1]

with open('backdoor.txt', 'r') as file_cipher:
  para_array = file_cipher.read().split("\n\n")
  for item in data_array:

    para_number, line_number, word_number = item.split(', ')
    

    para = para_array[int(para_number)-1]

    line_array = para.split('\n')

    line = line_array[int(line_number)-1]

    word_array = line.split(' ')

    word = word_array[int(word_number)-1]
    word = word.translate(None, string.punctuation)
    print(word)

    word += "\n"
    sending_array.append(word)
      
send_string = ''.join(sending_array)

s.send(send_string)
data2 = s.recv(2048)
print(data2)
