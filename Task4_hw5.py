# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

# from itertools import count


path = 'txt1.txt'
dataTxt = ''
with open (path, 'r', encoding= 'utf_8') as data:
    dataTxt = data.read()
print (dataTxt)

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding
text_compression = rle_encode(dataTxt)
with open('txt2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)