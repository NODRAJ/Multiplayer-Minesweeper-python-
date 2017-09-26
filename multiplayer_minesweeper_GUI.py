import time
import random
import socket
from tkinter import *

Game_Over = 0
Total_Spaces = 0
First_Click = 0

def click_checker(event):

    global Game_Over
    global Total_Spaces
    global First_Click

    
    print(event.widget)
    string_widget = str(event.widget)
    
    if string_widget == '.!button':
        
        string_widget += '1'
        
    widge = int(string_widget[8:])
    print(widge)
    chosen_row, chosen_column = divmod(widge, columns)
    
    if chosen_column == 0:
        
        chosen_column = columns
        chosen_row -= 1
        
    print('row: ' + str(chosen_row + 1) + '\n\ncolumn: ' + str(chosen_column))
    chosen_column -= 1
    Surrounding_Mines = 0

    if First_Click == 0:
        
        Mines[chosen_row][chosen_column] = 0
        First_Click +=1

    if Mines[chosen_row][chosen_column] == Mine_Chance:
            
        print('\nYou hit a mine!!\n\n           Restart to retry')
        Game_Over = 2
            
    else:

        try:
                
            if Mines[chosen_row - 1][chosen_column - 1] == Mine_Chance and chosen_row > 0 and chosen_column > 0:
                    
                    Surrounding_Mines += 1
                    #print('1')
                    
                    
        except:

            pass
                #print('oops')

        try:
                
            if Mines[chosen_row][chosen_column - 1] == Mine_Chance and chosen_column > 0:
                    
                    Surrounding_Mines += 1
                    #print('2')
                    
        except:

            pass
                #print('oops')
                
        try:
                
            if Mines[chosen_row + 1][chosen_column - 1] == Mine_Chance and chosen_column > 0:
                    
                    Surrounding_Mines += 1
                    #print('3')
                    
        except:

            pass
                #print('oops')
            
        try:
                
            if Mines[chosen_row - 1][chosen_column] == Mine_Chance and chosen_row > 0:
                    
                    Surrounding_Mines += 1
                    #print('4')
                    
        except:

            pass
                #print('oops')
                
        try:
                
            if Mines[chosen_row + 1][chosen_column] == Mine_Chance:
                    
                    Surrounding_Mines += 1
                    #print('5')
                    
        except:

            pass
                #print('oops')
                
        try:
                
            if Mines[chosen_row - 1][chosen_column + 1] == Mine_Chance and chosen_row > 0:
                    
                    Surrounding_Mines += 1
                    #print('6')
                    
        except:

            pass
                #print('oops')
                
        try:
                
            if Mines[chosen_row][chosen_column + 1] == Mine_Chance:
                    
                    Surrounding_Mines += 1
                    #print('7')
                    
        except:

            pass
                #print('oops')
                
        try:
                
            if Mines[chosen_row + 1][chosen_column + 1] == Mine_Chance:
                    
                    Surrounding_Mines += 1
                    #print('8')
                    
        except:

            pass
                #print('oops')
            
            #Board[chosen_row][chosen_column] = str(Surrounding_Mines)

            #CHANGE TO FRAME INSTEAD OF ROOT
        print(chosen_column)
        print(chosen_row)
        event.widget.grid_forget()
        b = Button(root, text='     ', bg='white')
        b.grid(column=chosen_column, row=chosen_row)
        l = Label(root, text=str(Surrounding_Mines), fg='blue', bg='white')
        l.grid(column=chosen_column, row=chosen_row)
        
        event.widget.grid_forget()
                
        if Game_Over != 2:
                
            Total_Spaces -= 1
            print('spaces ' + str(Total_Spaces))

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
        
    elif Game_Over == 2:
        
        s.send(str.encode('fail'))
        time.sleep(0.5)
        End_Game_Info = s.recv(1024)
        print(End_Game_Info.decode('utf-8'))

#def Flag_Maker(event):
    
#    string_widget = str(event.widget)
    
#    if string_widget == '.!button':
        
#        string_widget += '1'
        
#    widge = int(string_widget[8:])
#    print(widge)
#    chosen_row, chosen_column = divmod(widge, columns)
    
#    if chosen_column == 0:
        
  #      chosen_column = columns
 #       chosen_row -= 1
        
#    chosen_column -= 1

 #   event.widget.grid_forget()
 #   b = Button(root, text='     ', bg='red')
#    b.grid(column=chosen_column, row=chosen_row)
#    b.bind('<Button-2>', Button_Finder)
#    print('bruh')
#    print(b.invoke())
#    b.bind('<Button-3>', Flag_Remover)
    
#def Button_Finder(Event):

    #return event.widget
    
#def Flag_Remover(event):

    #string_widget = str(event.widget)
    
    #if string_widget == '.!button':
        
    #    string_widget += '1'
        
    #widge = int(string_widget[8:])
    #print(widge)
    #chosen_row, chosen_column = divmod(widge, columns)
    
    #if chosen_column == 0:
        
     #   chosen_column = columns
    #    chosen_row -= 1
        
    #chosen_column -= 1
   # print(chosen_column)
    #print('\n' + str(chosen_row))

#    event.widget.grid_forget()
#    b = Button(root, text='     ', bg='grey')
#    b.bind('<Button-1>', click_checker)
#    b.bind('<Button-3>', Flag_Maker)
#    b.grid(column=chosen_column, row=chosen_row)

##FIND OUT HOW TO GET THE NEW RED BUTTONS EVENT.WIDGET AND LINK IT WITH THE BUTTON
##BEFORE'S EVENT.WIDGET THEN USE THE EVENT.WIDGET ASSIGNED TO THE CURRENT ONE IN
##FLAG REMOVER TO REPLACE THE FLAG WITH A NORMAL BUTTON

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

root = Tk()

row_count = 0
column_count = 0
#l = Label(root, text='PySweeper')
#l.grid(row=0,sticky=N)

for y in range(rows):
    
    for x in range(columns):
        
        b = Button(root, text='     ', bg='grey')
        b.bind('<Button-1>', click_checker)
        #b.bind('<Button-3>', Flag_Maker)
        b.grid(column=x, row=y)
        column_count += 1

    row_count += 1
    column_count = 0

Mines = []

for x in range(rows):
    
    Mines.append([random.randint(0,Mine_Chance) for x in range(columns)])

print(Mines)

for row in Mines:
    
        for num in row:
        
            if num != Mine_Chance:
            
                Total_Spaces += 1

#Mine board still needs to be made
   
for x in range(3):
    
   print(3 - x)
   time.sleep(1)
   
print('\nGO!!!\n')
Start_Time = time.time()

#start tk function to display board
root.mainloop()



#SORT OUT COLUMN AND ROW ALIGNEMENT





#while Game_Over == False:
    
    #print('\n ', end = ' ' * len(str(rows)))
    #print('')
#Digits = 0
    #for y in range(len(str(columns))):

    #    print(' ' * (len(str(rows)) + 1), end='')

    #    for x in range(columns):

    #        bru = x + 1

    #        try:

    #            print(str(bru)[Digits], end = ' ')

     #       except:
                
     #           print(' ', end=' ')

    #    Digits += 1
     #   if y != int(len(str(columns)) - 1):
     #       print('')
        
    #print('')
    #bruh = 0
    
    #for row in Board:
        
        #bruh += 1
        #print(str(bruh), end = ' ' * ((len(str(rows)) + 1) - len(str(bruh))))
        #print(" ".join(row))

#BOARD PRINTING IS NOT NEEDED AS THE BOARD IS IN TK

    #chosen_row = 0
    #chosen_column = 0

    #while chosen_column not in range(1, columns + 1):
        
        #try:

            #chosen_column = int(input('\nchoose your column\n'))

        #except:

            #pass

    #while chosen_row not in range(1, rows + 1):
        
        #try:
            
            #chosen_row = int(input('\nchoose your row\n'))

        #except:
            
           # pass

#ROWS AND COLUMNS ARE CHOSEN BY THE USER WHEN CLICKING

    #chosen_row -= 1
           
#CHOSEN ROW STARTS FROM 0 HOWEVER CHOSEN COLUMN DOES NOT
    




#Make the server calculate the mine field and send it to
#the clients so they both have the same board

#Eventually add the chain reaction where adjacent empty spaces are removed
