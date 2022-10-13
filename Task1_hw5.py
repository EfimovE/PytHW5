# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст для редактирования через пробел:\n")
find_txt = 'абв'
print(f'Удаляем -{find_txt}- из текста: {text}')
result_list = [i for i in text.split() if find_txt not in i]
print(f'Результат: {" ".join(result_list)}')
# exit()