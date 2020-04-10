import numpy as np;

def gen_UMU(UM_mat):
	M = UM_mat.dot(UM_mat.T)
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/UMU.csv",S,delimiter = ',')
	print("UMU done")
	gen_MUM(UM_mat)

def gen_UMDMU(UM_mat):
	##Reading movie director
	f = open(datapath+"/movie_director.dat", "r")
	data = list()
	for i in f:
		data.append(list(map(float, i.split())))
	f.close();
	data = np.array(data)
	movie = 12677 #total number of movies
	director = int(max(data.T[1]))
	print(movie,director, len(data))
	MD_mat = np.zeros((movie,director))
	for i in data:
		MD_mat[int(i[0]-1)][int(i[1]-1)] = 1
	#till here
	temp = (MD_mat).dot(MD_mat.T)
	gen_MDM(temp)

	M = UM_mat.dot(temp).dot(UM_mat.T)
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/UMDMU.csv",S,delimiter = ',')
	print("UMDMU done")
	

def gen_UMAMU(UM_mat):
	##Reading movie actor
	f = open(datapath+"/movie_actor.dat", "r")
	data = list()
	for i in f:
		data.append(list(map(float, i.split())))
	f.close();
	data = np.array(data)
	movie = 12677 #total number of movies
	actor = int(max(data.T[1]))
	print(movie,actor, len(data))
	MA_mat = np.zeros((movie,actor))
	for i in data:
		MA_mat[int(i[0]-1)][int(i[1]-1)] = 1
	##till here
	temp = (MA_mat).dot(MA_mat.T)
	gen_MAM(temp)

	M = UM_mat.dot(temp).dot(UM_mat.T)
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/UMAMU.csv",S,delimiter = ',')
	print("UMAMU done")


def gen_UMTMU(UM_mat):
	##reading Movie_type
	f = open(datapath+"/movie_type.dat", "r")
	data = list()
	for i in f:
		data.append(list(map(float, i.split())))
	f.close();
	data = np.array(data)
	movie = 12677 #total number of movies
	type_ = int(max(data.T[1]))
	print(movie,type_, len(data))
	MT_mat = np.zeros((movie,type_))
	for i in data:
		MT_mat[int(i[0]-1)][int(i[1]-1)] = 1
	##till here
	temp = (MT_mat).dot(MT_mat.T)
	gen_MTM(temp)

	M = UM_mat.dot(temp).dot(UM_mat.T)
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/UMTMU.csv",S,delimiter = ',')
	print("UMTMU done")


def gen_MUM(UM_mat):
	M = (UM_mat.T).dot(UM_mat)
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/MUM.csv",S,delimiter = ',')
	print("MUM done")


def gen_MAM(M):
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/MAM.csv",S,delimiter = ',')
	print("MAM done")

def gen_MDM(M):
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/MDM.csv",S,delimiter = ',')
	print("MDM done")	

def gen_MTM(M):
	S = np.zeros((len(M), len(M[0])))
	for i in range(len(M)):
		if M[i][i] == 0:   ##if m[i][i] is 0,this implies that there is no entry(data unavailable) for the ith movie 
			continue   ##hence we assume that there is no similarity between ith and other objects
		for j in range(len(M[0])):
			if M[j][j] == 0:
				continue
			S[i][j] = (2*M[i][j])/(M[i][i]+M[j][j])
	np.savetxt(simstoragepath+"/MTM.csv",S,delimiter = ',')
	print("MTM done")

def final_simU(r):
	mat1 = list();
	f1 = open("simstoragepath+"/UMU.csv", "r")
	f2 = open(simstoragepath+"/UMDMU.csv", "r")
	f3 = open(simstoragepath+"UMAMU.csv", "r")
	f4 = open(simstoragepath+"/UMTMU.csv", "r")
	mat1 = list()
	for i in f1:
		t1 = list(map(float,i.split(',')))
		t2 = list(map(float,f2.readline().split(',')))
		t3 = list(map(float,f3.readline().split(',')))
		t4 = list(map(float,f4.readline().split(',')))
		for j in range(len(t1)):
			t1[j] = r[0]*t1[j] + r[1]*t2[j] + r[2]*t3[j] + r[3]*t4[j]
		mat1.append(t1)
	print("saving")
	np.savetxt("/home/smoke/Documents/ML/project/Datasets/simU.csv", mat1,delimiter = ',')	

def final_simM(r):
	mat1 = list();
	f1 = open(simstoragepath+"/MUM.csv", "r")
	f2 = open(simstoragepath+"/MDM.csv", "r")
	f3 = open(simstoragepath+"MAM.csv", "r")
	f4 = open(simstoragepath+"/MTM.csv", "r")
	mat1 = list()
	for i in f1:
		t1 = list(map(float,i.split(',')))
		t2 = list(map(float,f2.readline().split(',')))
		t3 = list(map(float,f3.readline().split(',')))
		t4 = list(map(float,f4.readline().split(',')))
		for j in range(len(t1)):
			t1[j] = r[0]*t1[j] + r[1]*t2[j] + r[2]*t3[j] + r[3]*t4[j]
		mat1.append(t1)
	print("saving")
	np.savetxt("/home/smoke/Documents/ML/project/Datasets/simM.csv", mat1,delimiter = ',')	
############################################################################################
######             Execution starts here                       #############################

datapath = input()
simstoragepath = input()
f = open(datapath+"/user_movie.dat", "r")
data = list()
for i in f:
	data.append(list(map(float, i.split())))
f.close();
data = np.array(data)
user = int(max(data.T[0]))
movie = int(max(data.T[1]))
print(user, movie, len(data))
UM_mat = np.zeros((user,movie))
for i in data:
	UM_mat[int(i[0]-1)][int(i[1]-1)] = 1
f.close();

Uweights = [.25]*4
Mweights = [.25]*4

gen_UMU(UM_mat)
gen_UMDMU(UM_mat)
gen_UMAMU(UM_mat)
gen_UMTMU(UM_mat)

final_simM(Uweights)
final_simU(Mweights)


