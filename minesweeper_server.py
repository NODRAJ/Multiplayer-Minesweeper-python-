import socket
import time

ready = 0

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 5450))


s.listen(2)
c1, addr1 = s.accept()
print(addr1)
c2, addr2 = s.accept()
print('working')

#Rows
c1.send(str.encode('10'))
c2.send(str.encode('10'))
time.sleep(0.5)

#Columns
c1.send(str.encode('10'))
c2.send(str.encode('10'))
time.sleep(0.5)

#Mine chance
c1.send(str.encode('4'))
c2.send(str.encode('4'))
time.sleep(0.5)

ready = 0
stop = 0

while stop == 0:
    
   data1 = c1.recv(1024)
   data2 = c2.recv(1024)
   
   #if not data1 and not data2:
       
    #   stop = 2
     #  print('Both clients left')
      # break
    
   if data1.decode('utf-8') == 'ready':
       
       ready += 1
       
   if data2.decode('utf-8') == 'ready':
       
       ready += 1
       
   if ready == 2:
       
       c1.send(str.encode('You are Player 1'))
       c2.send(str.encode('You are Player 2'))
       stop = 1
       
while stop == 1:
    
   data3 = c1.recv(1024)
   data4 = c2.recv(1024)
   
   if not data1 and not data2:
       
       stop = 2
       print('Both clients left')
       break

   data3 = data3.decode('utf-8')
   data4 = data4.decode('utf-8')
   print(data3)
   print(data4)

   if data3 == 'fail' and data4 == 'fail':
       End_Message = '\nBOTH PLAYERS HIT MINES!!!!'
       c1.send(str.encode(End_Message))
       c2.send(str.encode(End_Message))
       stop = 2

   elif data3 == 'fail' and data4 != 'fail':
       End_Message = ('Player 1 hit a mine! Player 2 got a time of: ' + str(data4))
       c1.send(str.encode(End_Message))
       c2.send(str.encode(End_Message))
       stop = 2

   elif data3 != 'fail' and data4 == 'fail':
       End_Message = ('Player 2 hit a mine! Player 1 got a time of: ' + str(data3))
       c1.send(str.encode(End_Message))
       c2.send(str.encode(End_Message))
       stop = 2
       
       
   elif float(data3) < float(data4):
       
       WinMsg = str('You won!!! \n\nYou got a time of: ' + str(data3) + '\n\nPlayer 2 got a time of: ' + str(data4))
       LoseMsg = str('You lost! \n\nYou got a time of: ' + str(data4) + '\n\nPlayer 1 got a time of: ' + str(data3))
       c1.send(str.encode(WinMsg))
       c2.send(str.encode(LoseMsg))
       stop = 2
       
   else:
       
       WinMsg = str('You won!!! \n\nYou got a time of: ' + str(data4) + '\n\nPlayer 2 got a time of: ' + str(data3))
       LoseMsg = str('You lost! \n\nYou got a time of: ' + str(data3) + '\n\nPlayer 1 got a time of: ' + str(data4))
       c1.send(str.encode(LoseMsg))
       c2.send(str.encode(WinMsg))
       stop = 2






#print('bruh')
#s.listen(1) #make it 2
#c , addr = s.accept()
#print('Connection from: ' + str(addr))
#while True:
#    data = c.recv(1024)
#    if not data:
#        break
#    print('Recieved: ' + str(data))
#    c.send(data.upper())
#c.close()
