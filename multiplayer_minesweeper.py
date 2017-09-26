import time
import random
import socket

s = socket.socket()
s.connect(('192.168.88.1', 5450))
rows = s.recv(1024)
rows = int(rows.decode('utf-8'))
print('rows: ' + str(rows))
time.sleep(0.5)
columns = s.recv(1024)
columns = int(columns.decode('utf-8'))
print('columns: ' + str(columns))
time.sleep(0.5)
Mine_Chance = s.recv(1024)
Mine_Chance = int(Mine_Chance.decode('utf-8'))
print('Mine chance: ' + str(Mine_Chance))
time.sleep(0.5)
input('\n\npress enter when you are ready... ')
s.send(str.encode('ready'))
print('Waiting for other player to ready up...\n')
time.sleep(0.5)
Player_Number = s.recv(1024)
Player_Number = Player_Number.decode('utf-8')
print(Player_Number)
time.sleep(0.5)

for x in range(3):
    
   print(3 - x)
   time.sleep(1)
   
print('\nGO!!!\n')
Start_Time = time.time()
Board = []

for x in range(rows):
    
    Board.append(["-"] * columns)

Mines = []

for x in range(rows):
    
    Mines.append([random.randint(0,Mine_Chance) for x in range(columns)])
   
Game_Over = False
print('')


Total_Spaces = 0

for row in Mines:
    for num in row:
        if num != Mine_Chance:
            Total_Spaces += 1

while Game_Over == False:
    
    #print('\n ', end = ' ' * len(str(rows)))
    print('')
    Digits = 0
    for y in range(len(str(columns))):

        print(' ' * (len(str(rows)) + 1), end='')

        for x in range(columns):

            bru = x + 1

            try:

                print(str(bru)[Digits], end = ' ')

            except:
                
                print(' ', end=' ')

        Digits += 1
        if y != int(len(str(columns)) - 1):
            print('')
        
    print('')
    bruh = 0
    
    for row in Board:
        
        bruh += 1
        print(str(bruh), end = ' ' * ((len(str(rows)) + 1) - len(str(bruh))))
        print(" ".join(row))

    Chosen_Row = 0
    Chosen_Column = 0

    while Chosen_Column not in range(1, columns + 1):
        
        try:

            Chosen_Column = int(input('\nchoose your column\n'))

        except:

            pass

    while Chosen_Row not in range(1, rows + 1):
        
        try:
            
            Chosen_Row = int(input('\nchoose your row\n'))

        except:
            
            pass


    Chosen_Row -= 1
    Chosen_Column -= 1
    Surrounding_Mines = 0

    if Mines[Chosen_Row][Chosen_Column] == Mine_Chance:
        
        print('\nYou hit a mine!!\n\n           Restart to retry')
        Game_Over = 2
        
    else:

        try:
            
            if Mines[Chosen_Row - 1][Chosen_Column - 1] == Mine_Chance and Chosen_Row > 0 and Chosen_Column > 0:
                
                Surrounding_Mines += 1
                #print('1')
                
                
        except:

            pass
            #print('oops')

        try:
            
            if Mines[Chosen_Row][Chosen_Column - 1] == Mine_Chance and Chosen_Column > 0:
                
                Surrounding_Mines += 1
                #print('2')
                
        except:

            pass
            #print('oops')
            
        try:
            
            if Mines[Chosen_Row + 1][Chosen_Column - 1] == Mine_Chance and Chosen_Column > 0:
                
                Surrounding_Mines += 1
                #print('3')
                
        except:

            pass
            #print('oops')
        
        try:
            
            if Mines[Chosen_Row - 1][Chosen_Column] == Mine_Chance and Chosen_Row > 0:
                
                Surrounding_Mines += 1
                #print('4')
                
        except:

            pass
            #print('oops')
            
        try:
            
            if Mines[Chosen_Row + 1][Chosen_Column] == Mine_Chance:
                
                Surrounding_Mines += 1
                #print('5')
                
        except:

            pass
            #print('oops')
            
        try:
            
            if Mines[Chosen_Row - 1][Chosen_Column + 1] == Mine_Chance and Chosen_Row > 0:
                
                Surrounding_Mines += 1
                #print('6')
                
        except:

            pass
            #print('oops')
            
        try:
            
            if Mines[Chosen_Row][Chosen_Column + 1] == Mine_Chance:
                
                Surrounding_Mines += 1
                #print('7')
                
        except:

            pass
            #print('oops')
            
        try:
            
            if Mines[Chosen_Row + 1][Chosen_Column + 1] == Mine_Chance:
                
                Surrounding_Mines += 1
                #print('8')
                
        except:

            pass
            #print('oops')
        
        Board[Chosen_Row][Chosen_Column] = str(Surrounding_Mines)
        Total_Spaces -= 1

        if Total_Spaces == 0:
            
            Game_Over = 1
            
if Game_Over == 1:
    
    End_Time = time.time()
    Completed_Time = End_Time - Start_Time
    s.send(str.encode(str(Completed_Time)))
    print('\nWaiting for opponent to finish...\n')
    time.sleep(0.5)
    End_Game_Info = s.recv(1024)
    print(End_Game_Info.decode('utf-8'))
    
else:
    
    s.send(str.encode('fail'))
    time.sleep(0.5)
    End_Game_Info = s.recv(1024)
    print(End_Game_Info.decode('utf-8'))



#Make the server calculate the mine field and send it to
#the clients so they both have the same board

#Eventually add the chain reaction where adjacent empty spaces are removed
