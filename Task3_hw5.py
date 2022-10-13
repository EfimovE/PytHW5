# Создайте программу для игры в 'Крестики-нолики'.
position = list (range(1, 10))
# for i in range(1, 10):
#     position.append(i)

sign = "O"
moves = []

win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
def winCondition():
    for i in win:
        if position[i[0]-1] == position[i[1]-1] == position[i[2]-1]:
            print ('Game over')
            exit()

def printField(position):
    print ("-" * 15)
    for i in range (3):
        print ("|", position[0+i*3], "|", position[1+i*3], "|", position[2+i*3], "|")
        print ("-" * 15)
 
counter = 0
while True:
    while True:
        printField(position)
        valid = False
        while not valid:
            player_answer = int(input(f"\n\n Ход {'игрока' if sign == 'X' else 'противника'}: "))
            

            if player_answer >= 1 and player_answer <= 9:
                if (str(position[player_answer - 1]) not in "XO"):
                    position[player_answer - 1] = sign
                    valid = True
                else:
                    print ('Эта клетка уже занята')
            else:
                print ('Введите число от 1 до 9.')

        if player_answer in moves:
            print ('Эта клетка уже занята')
        else:
            if sign == "O":
                sign = "X"
            else:
                sign = "O"
            moves.append(player_answer)
            position[player_answer - 1] = sign
            winCondition()
            print(sign)
            counter += 1
            print(counter)
            if counter == 9:
                print ("Ничья!")
                exit()
            break
