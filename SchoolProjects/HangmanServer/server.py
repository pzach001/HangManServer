import socket
import sys
import time
import threading
from thread import *
HOST = ''
PORT = 1114


'''
THINGS TO DO:
1. MAKE SURE TO FLUSH OUT ALL VARIABLES
2. ADMIN
3. WHEN EXITING NOT ALL OF THEM EXIT
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
myList =[]
try:
    s.bind((HOST,PORT))
except socket.error ,msg:
    print 'Bind failed. Error code: ' + str(msg[0]) + 'Message' + msg[1]
    sys.exit()

print 'Socket bind complete'
dummy = ['dummy','test']
UsrPswArray  = [dummy]
Dictionary = ["dog","cat","bird","puppy"]
GameNameList = [None]
HOFlist =[]
myList=[]
lives = 0
playername="dummy"
s.listen(10)
GameList = []
connqueue = []
doneflag =0
print 'Socket now listening'
def InGame(conn,GameObject):
	global doneflag
        doneflag = 0 
	currplayernum = 0
#GameObject = [gamename,lives,PlayerandScoreList,GameWord,currentspread,connectionlist]
 	currentspread = []
        #print "connection with object4"
        #print len(GameObject[5])
        #print "\n"
        for x in GameObject[5]:
         #       print str(x);
                sendstring = "----------------------this player has joined: "                 
                x.sendall("\n") 
                x.sendall(sendstring)
                x.sendall(GameObject[2][len(GameObject[2])-1][0])
                x.sendall("\n\n")
 	for i in range( len(GameObject[3]) ):
                currentspread.append('_')
 	GameObject[4]= currentspread
        conn.sendall("-----------------------------------------------------------\n")
	conn.sendall( "this is current spread:\n")
        for i in range(len(GameObject[4]) ):			
                conn.sendall( GameObject[4][i])
                conn.sendall( " ")
        conn.sendall("\n")
        conn.sendall("Number of Lives left: ")
        conn.sendall(str(GameObject[1]))
        conn.sendall("\n")
        conn.sendall("LIST OF PLAYERS AND SCORES:\n")
        for i in range(len(GameObject[2])):
		conn.sendall(str(GameObject[2][i][0]))
        	conn.sendall(" ")
       		conn.sendall(str(GameObject[2][i][1]))     
		conn.sendall("\n")
        conn.sendall("-----------------------------------------------------------\n")
 	while 1:
                letterflag = 0  
                pos =0
         #      print "doneflag"
	 # 	print doneflag
		if doneflag == 1:
			doneflag = 0
			break
                currplayer =GameObject[5][currplayernum]
                for m in GameObject[5]:
                        playturn = "Players Turn:"+GameObject[2][currplayernum][0]
                	m.sendall(playturn)
                        m.sendall("\n")
		if doneflag == 1:
		      doneflag = 0
                      for x in Gameobject[5]:
				break
       		currplayer.sendall("make your move: \n")
          	currletter = currplayer.recv(1024)
         #       print currletter
                answersize = len(currletter.rstrip())
         #       print answersize
		if doneflag == 1:
			doneflag = 0
			break
                if(answersize > 1):
			if(currletter.rstrip() == GameObject[3]):
				GameObject[2][currplayernum][1] = GameObject[2][currplayernum][1]+answersize
				conn.sendall("YOU WIN\n")
                                for i in GameObject[5]:
					i.sendall("Whole Word has been found: Game Over\n")
                                HOFlist.append(GameObject[2][currplayernum][0])
			#	print "length of Gamelist" + str(len(GameList))
                      		GameList.remove(GameObject)		
		                doneflag = 1 
				time.sleep(3) 
				return
			else:
				conn.sendall("YOU GUESSED WORD INCORRECTLY: KICKED FROM GAME")
                                del GameObject[2][currplayernum]
				return
		else:
                	for i in range(len(GameObject[3]) ):
                		if((currletter[0] == GameObject[3][i]) and (GameObject[4][i] == '_')):
					letterflag = 1
                                	pos = i
               		if(letterflag == 1):
                		conn.sendall("Correct!\n")
				GameObject[4][pos] = currletter[0]
               			GameObject[2][currplayernum][1] =   GameObject[2][currplayernum][1]+1
                       		currplayernum = currplayernum -1
			
			else:
                       		conn.sendall("Wrong!\n")
		       		GameObject[1] =  GameObject[1]-1
               		if(GameObject[1] == 0 ):
                                for i in GameObject[5]:
					i.sendall("GAME OVER LIVES IS ZERO\n")
				doneflag = 1
                      		GameList.remove(GameObject)	
                                return
		if doneflag == 1:
			doneflag = 0
			break
         	for m in GameObject[5]:
       			m.sendall("-----------------------------------------------------------\n")
	        	m.sendall( "this is current spread:\n")
	        	for i in range(len(GameObject[4]) ):			
                		m.sendall( GameObject[4][i])
                		m.sendall( " ")
			m.sendall("\n")
        		m.sendall("Number of Lives left: ")
        		m.sendall(str(GameObject[1]))
        		m.sendall("\n")
        		m.sendall("LIST OF PLAYERS AND SCORES:\n")
        		for i in range(len(GameObject[2])):
				m.sendall(str(GameObject[2][i][0]))
                        	m.sendall(" ")
                        	m.sendall(str(GameObject[2][i][1]))     
				m.sendall("\n")
		        m.sendall("-----------------------------------------------------------\n")
		if doneflag == 1:
			doneflag = 0
			break
               	winflag = 0
                for i in range(len(GameObject[4])):
			if GameObject[4][i] == '_' :
				winflag = 1
                if  winflag == 0:
                        for x in GameObject[5]:
          #                      print(str(x))
				x.sendall("Word Found....exiting game \n")
				bestplayer = GameList[currplayernum][2][0][1]
				bestplayindex = 0
                                doneflag = 1
			
			for i in range(len(GameObject[2])):
				if bestplayer < GameObject[2][i][1]:
					bestplayer = GameList[currplayernum][2][0][1] 
					bestplayindex = i
                        HOFlist.append(GameObject[2][bestplayindex][0])
			#for i in range(len(GameObject[5])):
			#	if i !=GameObject[5][currplayernum]:  	
                      	GameList.remove(GameObject)		
		        for i in range(len(GameObject[2])):
				del GameObject[2][currplayernum]
			conn.sendall("checking to see where this is; \n")                              
			time.sleep(3)
			return
                if (currplayernum >=len(GameObject[5])-1):
			currplayernum = 0
		else:
			currplayernum = currplayernum +1
                 #               conn.sendall("end of file\n")
		if doneflag == 1:
			doneflag = 0
			break




def GameLoginFunc(conn): 
 #print str(conn)
# connqueue.append(conn)
 conn.sendall("WHAT IS YOUR PLAYER NAME: ")
 playername = conn.recv(1024)

 while True:
        conn.sendall("PLEASE CHOOSE AN OPTION:\n1.Start New Game\n2.Get List of the Games\n3.Hall of Fame\n4.Exit\n") 
	data = conn.recv(1024)
       # print "data received from in game"
        if(data[0] == '1'):
        	GameWordNum = conn.sendall("Pick a Number from the dictionary:\n")
		 
		GameWord = Dictionary[int(conn.recv(1024) )]
        #        print GameWord 
                conn.sendall("name your game!:" )
                gamename = conn.recv(1024)
                GameNameList.append(gamename.rstrip())
                #print len(Gamelist)
		conn.sendall("Select Level of Difficulty:\n1.Easy\n2.Medium\n3.Hard\n")
                lvl  = conn.recv(1024)
                if(lvl[0] == '1'):
                	lives = 3*len(GameWord.rstrip())
                if(lvl[0] == '2'):
                	lives = 2*len(GameWord.rstrip())
                if(lvl[0] == '3'):
                	lives = len(GameWord.rstrip())
                conn.sendall("difficulty chosen! \n")
                PlayerandScoreList =[]
                currentspread =[]
                score =0
                #Gameobject consists of:gamename(string),lives(int),PlayerList(arrayofString, GameWord)                  # also consists of string  currentspreaad
                NameAndScoreObj = [playername.rstrip(),score]
                PlayerandScoreList.append(NameAndScoreObj)
                #index = 0
                #print "player list length: "
                #print len(PlayerandScoreList)
                #connectionlist.append(connqueue[curr])
                
                connectionlist=[]
                connectionlist.append(conn)
                GameObject = [gamename,lives,PlayerandScoreList,GameWord,currentspread,connectionlist]
                GameList.append(GameObject)
                #print "GameList " + str(len(GameList))
                gamelistsize = len(GameList)
		conn.sendall(str(gamelistsize))
		#index= index+1 	
                #STARTING GAME WITH THIS FUNCTION
                #print " Game is Starting \n"
                InGame(conn,GameObject)
        if(data[0] == '2'):
                
		if len(GameList) == 0:
			conn.sendall("no game being played! \n")
		else:
	
        		conn.sendall("LIST OF GAMES: \n")
			for i in range(len(GameList)):
                        	x = i+1
                        	numstring = str(x)+ '.'
                        	conn.sendall(numstring)
                		conn.sendall( GameList[i][0] )
                                conn.sendall("\n")
			conn.sendall("\n")
                        conn.sendall("PICK A GAME TO JOIN: ")
			gamechoice = conn.recv(1024)
                        newplayerandscore= [playername.rstrip(),0]
                        GameList[int(gamechoice[0])-1][2].append(newplayerandscore)
                        GameList[int(gamechoice[0])-1][5].append(conn)
                        #.append(connqueue[curr])
			InGame(conn,GameList[int(gamechoice[0])-1])
				
	if(data[0] == '3'):
	       conn.sendall("HALL OF FAME: \n")
               for i in range(len(HOFlist)):
               		conn.sendall(str(HOFlist[i]))
                        conn.sendall("\n")
        if(data[0] == '4'):
               break;

def clientthread(conn):
    #initalizes list to zero  NOTE: POSSIBLE BUG 
   
    while True:
        #sendall does not mean sends to all other clients
        conn.sendall("PLEASE CHOOSE AN OPTION:\n1.login\n2.Make New User\n3. Hall of Fame\n4.Exit\n")
        data = conn.recv(1024)
        #print "just received data"
        #print data
        if data[0] == '1':
         #   print "inside 1"
            conn.sendall("username: ")
            UsrName = conn.recv(1024)
            conn.sendall("password: ")
            Psword  = conn.recv(1024)
            a = [UsrName.rstrip(),Psword.rstrip()]
            flag = 0
            for i in range(len(UsrPswArray)):
                if( (str(UsrPswArray[i][0]) == a[0]) and str(UsrPswArray[i][1]) == (a[1])) :
                    flag = 1
            if(flag == 0):
               conn.sendall("invalid username and password\n")
            else:
               conn.sendall("Login confirmed! \n")  
               conn.sendall("logging in...............\n")
               GameLoginFunc(conn)
        if data[0] == '2':
            conn.sendall("new username: ")
            newUsrName = conn.recv(1024)
            conn.sendall("new password: ")
            newPsword  = conn.recv(1024)
            b = [newUsrName.rstrip(),newPsword.rstrip()]
            flag = 0
            for j in range(len(UsrPswArray)):
                if(str(UsrPswArray[j][0]) == b[0]) :
                    flag = 1
            if(flag == 0):
               conn.sendall("new login combination saved!\n")
               UsrPswArray.append(b)
            else:
               conn.sendall("ERROR: existing login. Did not save login information.\n")
        if data[0] =='3':
               conn.sendall("HALL OF FAME: \n")
               for i in range(len(HOFlist)):
               		conn.sendall(str(HOFlist[i]))
        if data[0] == '4':
               break
        if not data:
            break
     
    

    conn.close()
def serverthread(x):
	while 1:
		print("1.Current List of User")
		print("2.Current List of Words")
		print("3.Add new word to the list of words")
		value = raw_input("choose option: ")
		if value[0] == '1':
			for x in myList:
				print str(x)
		if value[0] == '2':
			for x in Dictionary:
				print x
		if value[0] == '3':
			word = raw_input("enter word: ")
			Dictionary.append(word.rstrip())
start_new_thread(serverthread,(0,))
while 1:

    conn, addr = s.accept() 
    myList.append(conn)
    #print 'Connected with '+ addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread,(conn,))


s.close()


