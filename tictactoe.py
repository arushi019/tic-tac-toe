from SimpleGraphics import *
from math import *
from copy import deepcopy
from random import randint
#SHIFT FROM 2P to PLAYER VS COMPUTER
#problem of multiple windows solved
#problem of drawing all figures at once solved 
#problem of placement of nought and cross solved
#problem of placement in correct cell solved
#problem of winner line solved
#past_stats.txt contains stats of last matches-->remember function implemented
#opponent moves recorded 
#past_stats now remembers all games
#on defensive mode
#try adding block mode
"""def zone(v1,v2,v3,x,y,x1,y1):
	#identifies the zone of (x1,y1) respective to a particular tuple(x,y matrix co-ordinates received as parameters) and returns a character indicating the zone
	#wiil work inside probability function
	if (x1,y1)==(x+1,y) or (x1,y1)==(x-1,y) or (x1,y1)==(x,y+1) or (x1,y1)==(x,y-1):
		return 'p1'
	elif (x1,y1)==(x+1,y+1) or (x1,y1)==(x+1,y-1) or (x1,y1)==(x-1,y-1) or (x1,y1)==(x-1,y+1):
		return 'p2'
	elif (x1,y1)==(x+2,y+2) or (x1,y1)==(x+2,y) or (x1,y1)==(x,y+2):
		return 'p3'
	elif (x1,y1)==(x+1,y+2) or (x1,y1)==(x+1,y-2) or (x1,y1)==(x-1,y+2) or (x1,y1)==(x-1,y-2) or (x1,y1)==(x+2,y+1) or (x1,y1)==(x+2,y-1) or (x1,y1)==(x-2,y+1) or (x1,y1)==(x-2,y-1):
		return 'p4'
def prob():
	#calculates probabilities of opponent's all moves and returns the action to be taken based on highest probability
	#if probability is same for two possibilities choose the more recent one
	#first you need to read the file and understand
	fo1=open("move.txt","r")
	ls=fo1.read()
	print(ls)
	#ls=ls.split()
	#print(ls)
	#print(ls)
	l1=[]
	for line in ls:
		#print(line)
		if line in '012':
			print(line)
			line=int(line)	
		l1.append(line)
	print(l1)
	with open('move.txt') as f:
		mylist=[tuple(map(int,i.split(','))) for i in f]
	print(mylist)	
prob()"""
#-----------------------------------predicting the opponent's move---------------------------------
"""				read the opponent's moves as list of list-->file_read()
				each sub-list contains moves made in a particular game
							|
							|
							|
							V
				calculate frequency of indexth move using the list compiled above
							|
							|
							|
							V
				find the last move made at indexth move--->history function
***index is the order of opponent's move w.r.t the computer					"""
def file_read():
	#reads list of opponent's moves from file move.txt
	#moves are recorded in the form of co-ordinates(not as tuples)
	#l2 is the list returned by this function
	fo=open("move.txt")
	ls=fo.readlines()
	l2=[]
	for x in ls:
		key=x.index('\n')
		x=x[:key]
		l1=[]
		for y in x:
			if y in'012':
				y=int(y)
				l1.append(y)
		l2.append(l1)
	return(l2)
#print(file_read()) 
def calc_prob(index):
	#calculates the probability of (index)th move::::index starts from 0
	#move_lst contains list of list-->each element is a list that contains the 
	#  opponent's moves in form of matrix co-ordinates--->file_read()
	#you need to integrate it with navigate function
	x=[]
	y=[]	
	move_lst=file_read()
	#print(move_lst)
	for sl in move_lst:
		if ((2*index+1)<=len(sl)):
			x.append(sl[2*index])
			y.append(sl[2*index+1])
		else:
			x.append(5)
			y.append(5)
	#print(x)
	#print(y)
	prob=[0,0,0,0,0,0,0,0,0]
	for n in range(len(x)):
		if x[n]==0 and y[n]==0:
			prob[0]+=1
		if x[n]==1 and y[n]==0:
			prob[1]+=1
		if x[n]==2 and y[n]==0:
			prob[2]+=1
		if x[n]==0 and y[n]==1:
			prob[3]+=1
		if x[n]==1 and y[n]==1:
			prob[4]+=1
		if x[n]==2 and y[n]==1:
			prob[5]+=1
		if x[n]==0 and y[n]==2:
			prob[6]+=1
		if x[n]==1 and y[n]==2:
			prob[7]+=1
		if x[n]==2 and y[n]==2:
			prob[8]+=1
	#print(prob)
	return prob
def history(index):
	#returns the co-ordinates of last move by the opponent
	#needs (index)th as argument
	#index starts from 0
	l1=file_read()
	key=len(l1)-1
	while key>=0:
		#need to look at this more carefully
		if (2*index)>=(len(l1[key])):
			index=index-1
			#print(key)
		else:
			break
	last_game=l1[key]
	#print(last_game)	
	last_x=last_game[2*index]
	last_y=last_game[2*index+1]
	return(last_x,last_y)
#print(history(3))
def next_move(pr_move,index):
	#predicts the next move of opponent using probability calculated in calc_prob
	#finds maximum frequency-- if maxima occurs twice or more:
	#	invoke history--->pick the most recent move	
	#classifies the move into zones
	#how to classify to zones???--->define new function
	#return zone
	pr_max=max(pr_move)
	index_of_max=[]
	flag=0
	copy_max=deepcopy(pr_move)
	for x in range(len(pr_move)):
		if pr_move[x]==pr_max:
			index_of_max.append(x)
			flag=x
			copy_max=copy_max[flag+1:]
	last_move=history(index)
	last_move=list(last_move)
	return last_move		
	#print(index,pr_move.count(pr_max))
def final_output(index):
	p=calc_prob(index)
	final=next_move(p,index)
	return final
#----------------------------------------now i can predict the next move of the opponent----------------------------------------------------------
def block(v1,v2,v3,x,y):
	h1=[v1[0],v2[0],v3[0]]
	h2=[v1[1],v2[1],v3[1]]
	h3=[v1[2],v2[2],v3[2]]
	d1=[v1[0],v2[1],v3[2]]
	d2=[v1[2],v2[1],v3[0]]
	X=x
	Y=y
	for x in [v1,v2,v3,h1,h2,h3,d1,d2]:
		if x.count(1)==2 and x.count(0)==1:
			#get the co-ordinates of the zero point
			if x==v1:
				X=0
				Y=x.index(0)
			elif x==v2:
				X=1
				Y=x.index(0)
			elif x==v3:
				X=2
				Y=x.index(0)
			elif x==h1:
				Y=0
				X=x.index(0)
			elif x==h2:
				Y=1
				X=x.index(0)
			elif x==h3:
				Y=2
				X=x.index(0)
			elif x==d1:
				Y=x.index(0)
				X=x.index(0)
			elif x==d2:
				Y=x.index(0)
				X=x.index(0)
			elif x==d3:
				Y=x.index(0)
				X=x.index(0)
			break;
	l=[X,Y]	
	return l
def comp_is_winner(v1,v2,v3,x,y):
	h1=[v1[0],v2[0],v3[0]]
	h2=[v1[1],v2[1],v3[1]]
	h3=[v1[2],v2[2],v3[2]]
	d1=[v1[0],v2[1],v3[2]]
	d2=[v1[2],v2[1],v3[0]]
	X=x
	Y=y
	for x in [v1,v2,v3,h1,h2,h3,d1,d2]:
		if x.count(2)==2 and x.count(0)==1:
			#get the co-ordinates of the zero point
			if x==v1:
				X=0
				Y=x.index(0)
			elif x==v2:
				X=1
				Y=x.index(0)
			elif x==v3:
				X=2
				Y=x.index(0)
			elif x==h1:
				Y=0
				X=x.index(0)
			elif x==h2:
				Y=1
				X=x.index(0)
			elif x==h3:
				Y=2
				X=x.index(0)
			elif x==d1:
				Y=x.index(0)
				X=x.index(0)
			elif x==d2:
				Y=x.index(0)
				X=x.index(0)
			elif x==d3:
				Y=x.index(0)
				X=x.index(0)
			break;
	l=[X,Y]	
	return l
def draw(v,x3,y3):
	#recieves matrix co-ordinates as parameters
	#draw noughts and crosses
	x1=4*x3-4
	y1=6-4*y3
	if v==1:		
		DrawDisk(x1,y1,1,FillColor=WHITE,EdgeColor=BLACK,EdgeWidth=3)
	if v==2:
		DrawLineSeg(x1+1,y1+1,x1-1,y1-1,LineWidth=2)
		DrawLineSeg(x1-1,y1+1,x1+1,y1-1,LineWidth=2)
def disp(v1,v2,v3):
	#render the tictactoe table in GUI
	#does not close the window
	MakeWindow(9,labels=False)
	DrawLineSeg(-6,4,6,4,LineWidth=3)
	DrawLineSeg(-6,0,6,0,LineWidth=3)
	DrawLineSeg(-2,8,-2,-4,LineWidth=3)
	DrawLineSeg(2,8,2,-4,LineWidth=3)
	for i in range(3):
		if v1[i]==1:
			draw(1,0,i)
		if v1[i]==2:
			draw(2,0,i)
	for i in range(3):
		if v2[i]==1:
			draw(1,1,i)
		if v2[i]==2:
			draw(2,1,i)
	for i in range(3):
		if v3[i]==1:
			draw(1,2,i)
		if v3[i]==2:
			draw(2,2,i)
def oppn_move(x,y,status,o1):
	#if status=='w'--> generates a list containing co-ordinates of opponent's moves with each entry as a tuple in sequential order of the moves
	#if status=='r'--> returns a string to remember function which can be appended to past_stats
	#will be invoked in inp function whenever player 1 makes a move
	if status=='w':
		o1.append(x)
		o1.append(y)
	if status=='r':
		s=str(o1)
		return s	
def inp(v1,v2,v3,x,y,turn1):
	#recieves matrix co-ordinates x,y as parameters
	if turn1%2==1:
		print("Player1")
		oppn_move(x,y,'w',o1)
		val=1
	else:
		print("Computer")
		val=2
	if (x,y)==(0,0):
		if v1[0]==0:
			v1[0]=val
	if (x,y)==(1,0):
		if v2[0]==0:
			v2[0]=val
	if (x,y)==(2,0):
		if v3[0]==0:
			v3[0]=val
	if (x,y)==(0,1):
		if v1[1]==0:
			v1[1]=val
	if (x,y)==(1,1):
		if v2[1]==0:
			v2[1]=val
	if (x,y)==(2,1):
		if v3[1]==0:
			v3[1]=val
	if (x,y)==(0,2):
		if v1[2]==0:
			v1[2]=val
	if (x,y)==(1,2):
		if v2[2]==0:
			v2[2]=val
	if (x,y)==(2,2):
		if v3[2]==0:
			v3[2]=val
	#loop through v1,v2,v3 to draw figures 
	#Show window after looping through all three
	disp(v1,v2,v3)
	ShowWindow()
	CloseWindow()
def cursor(x1,y1,v1,v2,v3):
	#displays the position of cursor
	disp(v1,v2,v3)
	DrawDisk(x1,y1,0.1,FillColor=RED,EdgeColor=RED)
	ShowWindow()
	CloseWindow()
def win(v1,v2,v3):
	#checks and displays the winner
	h1=[v1[0],v2[0],v3[0]]
	h2=[v1[1],v2[1],v3[1]]
	h3=[v1[2],v2[2],v3[2]]
	d1=[v1[0],v2[1],v3[2]]
	d2=[v1[2],v2[1],v3[0]]
	if 0 not in v1:
		if 1 not in v1:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,8,-4,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in v1:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,8,-4,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in v2:
		if 1 not in v2:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(0,8,0,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in v2:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(0,8,0,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in v3:
		if 1 not in v3:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(4,8,4,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in v3:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(4,8,4,-4,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in h1:
		if 1 not in h1:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,6,5,6,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in h1:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,6,5,6,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in h2:
		if 1 not in h2:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,2,5,2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in h2:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,2,5,2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in h3:
		if 1 not in h3:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,-2,5,-2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in h3:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-5,-2,5,-2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in d1:
		if 1 not in d1:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,6,4,-2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in d1:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,6,4,-2,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
	if 0 not in d2:
		if 1 not in d2:
			print("Computer wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,-2,4,6,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()
			return True
		if 2 not in d2:
			print("Player1 wins")
			disp(v1,v2,v3)
			DrawLineSeg(-4,-2,4,6,LineColor=RED,LineWidth=4)
			ShowWindow()
			CloseWindow()	
			return True
	else:
		return False		
def tie(v1,v2,v3):
	if 0 not in v1 and 0 not in v2 and 0 not in v3 and win(v1,v2,v3)==False:
		print("it is a tie")
		return True
def checker(v1,v2,v3,x,y):
	if x==0 and y==0:
		if v1[0]!=0:
			return True
	elif x==1 and y==0:
		if v2[0]!=0:
			return True
	elif x==2 and y==0:
		if v3[0]!=0:
			return True
	elif x==0 and y==1:
		if v1[1]!=0:
			return True
	elif x==1 and y==1:
		if v2[1]!=0:
			return True
	elif x==2 and y==1:
		if v3[1]!=0:
			return True
	elif x==0 and y==2:
		if v1[2]!=0:
			return True
	elif x==1 and y==2:
		if v2[2]!=0:
			return True
	elif x==2 and y==2:
		if v3[2]!=0:
			return True
	else:
		return False
def remember(v1,v2,v3):
	#writes the opponent's moves and the matrix to a file
	h1=[v1[0],v2[0],v3[0]]
	h2=[v1[1],v2[1],v3[1]]
	h3=[v1[2],v2[2],v3[2]]
	d1=[v1[0],v2[1],v3[2]]
	d2=[v1[2],v2[1],v3[0]]
	"""fo=open("past_stats.txt","r")
	st=fo.read() 
	s1=str(v1)+str(v2)+str(v3)
	if win(v1,v2,v3)==True: 
		if 2 not in v1 or 2 not in v2 or 2 not in v3 or 2 not in h1 or 2 not in h2 or 2 not in h3 or 2 not in d1 or 2 not in d2:
			s1=s1+"p1"+oppn_move(0,0,'r',o1)+"\n"
		else:
			s1=s1+"p2"+oppn_move(0,0,'r',o1)+"\n"
	if tie(v1,v2,v3)==False:
		s1=s1+"tie"
	st=st+s1
	fo.close()
	fo=open("past_stats.txt","a")
	#GOOD JOB!!!!
	fo.write(s1)
	fo.close()"""
	fo1=open("matrix.txt","a")
	fo2=open("move.txt","a")
	t1=[v1,v2,v3]
	t1=str(t1)
	t1=t1+'\n'
	m1=oppn_move(0,0,'r',o1)
	m1=m1+'\n'
	if win(v1,v2,v3)==True:
		if 2 not in v1 or 2 not in v2 or 2 not in v3 or 2 not in h1 or 2 not in h2 or 2 not in h3 or 2 not in d1 or 2 not in d2:
			fo1.write(t1)
			fo2.write(m1)
	fo1.close()
	fo2.close()
"""def i_am_the_winner(v1,v2,v3):
	h1=[v1[0],v2[0],v3[0]]
	h2=[v1[1],v2[1],v3[1]]
	h3=[v1[2],v2[2],v3[2]]
	d1=[v1[0],v2[1],v3[2]]
	d2=[v1[2],v2[1],v3[0]]
	fo=open("past_stats.txt","r")
	s=fo.read()"""
def navigate_and_place(v1,v2,v3):
	#use wasd to navigate,t to terminate,i to input
	#x11,y11 are cursor co-ordinates
	#x2,y2 are matrix co-ordinates-->passed on to inp function	
	(x11,y11)=(-4,-2)
	key=input('')
	turn=1
	while key!='t':
		print(turn)
		while turn%2==1:
			if key=='w' and abs(y11)<=6 and abs(x11)<=6:
				cursor(x11,y11+4,v1,v2,v3)
				y11+=4
			if key=='s' and abs(y11)<=6 and abs(x11)<=6:
				cursor(x11,y11-4,v1,v2,v3)
				y11-=4
			if key=='a' and abs(x11)<=6 and abs(y11)<=6:
				cursor(x11-4,y11,v1,v2,v3)
				x11-=4
			if key=='d' and abs(x11)<=6 and abs(y11)<=6:
				cursor(x11+4,y11,v1,v2,v3)
				x11+=4
			if key=='i':
				print("check player1")
				flag=1 
				#incorporate computer as player--->if turn%2==0: computer's turn
				x2=(4+x11)//4
				y2=(6-y11)//4
				inp(v1,v2,v3,x2,y2,turn)
				if win(v1,v2,v3)==True:
					remember(v1,v2,v3)
					break;
				elif tie(v1,v2,v3)==True:
					remember(v1,v2,v3)
					break;
				break;
			key=input('')
		if turn%2==0:
			index=(turn+1)//2
			move=final_output(index)
			while checker(v1,v2,v3,move[0],move[1])==False:
				x1=randint(2)
				y1=randint(2)
				move=[x1,y1]
			p=block(v1,v2,v3,move[0],move[1])
			q=comp_is_winner(v1,v2,v3,p[0],p[1])
			inp(v1,v2,v3,q[0],q[1],turn)
			#computer to beyimani par utar aaya lol :p :p :p
			if win(v1,v2,v3)==True:
				remember(v1,v2,v3)
				break;
			elif tie(v1,v2,v3)==True:
				remember(v1,v2,v3)
				break;			
		turn+=1				
		key=input('')
v1=[0,0,0]
v2=[0,0,0]
v3=[0,0,0]
o1=[]
h1=[v1[0],v2[0],v3[0]]
h2=[v1[1],v2[1],v3[1]]
h3=[v1[2],v2[2],v3[2]]
d1=[v1[0],v2[1],v3[2]]
d2=[v1[2],v2[1],v3[0]]
print("Welcome to TicTacToe!\n---------------------------------------------------------------------\nThe game begins with the cursor at (0,2).\nPlayer1 gets noughts and Player2 gets crosses")
print("Use wasd to navigate through the board, i to insert and t to terminate the game")
#inp(v1,v2,v3,h1,h2,h3,0,1)
#disp(v1,v2,v3)
#cursor(0,3)
navigate_and_place(v1,v2,v3)
