#Vidit Jain
#2017370
#A2
from fractions import Fraction
def swapRows(A,row1,row2):
	temprow=A[row1]
	A[row1]=A[row2]
	A[row2]=temprow
	return A

def Row_Transformation(A,x,row1,row2):
	for i in range(len(A[row1])):
		A[row2][i]=A[row2][i]+x*A[row1][i]
	return A

def Transpose(A):
	rows=len(A)
	columns=len(A[0])
	AT=[]
	l1=[]
	for j in range(columns):
		for i in range(rows):
			l1.append(A[i][j])
		AT.append(l1)
		l1=[]
	return AT

def MatrixRank(A):
	rows=len(A)
	columns=len(A[0])
	rank=columns
	for i in range(rows):
		count=0
		for j in range(columns):
			if A[i][j]==0:
				count+=1
		if count==columns:
			A=swapRows(A,i,rows-1)
	if rows>=columns:
		for i in range(rank):
			if A[i][i]!=0:
				for j in range(columns):
					if j!=i:
						if A[j][i]>0 and A[i][i]>0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=-int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=-Fraction(A[j][i]/A[i][i])
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]<0 and A[i][i]<0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=-int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(A[j][i]/abs(A[i][i]))
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]>0 and A[i][i]<0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(A[j][i]/abs(A[i][i]))
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]<0 and A[i][i]>0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(abs(A[j][i])/A[i][i])
								A=Row_Transformation(A,x,i,j)
			elif A[i][i]==0:
				for j in range(i+1,columns):
					if A[j][i]!=0:
						A=swapRows(A,j,i)
					else:
						AT=Transpose(A)
						AT=swapRows(AT,j,i)
						A=Transpose(AT)
				rank=rank-1
				i=i-1
	else:
		A=Transpose(A)
		rows=len(A)
		columns=len(A[0])
		rank=columns
		for i in range(rank):
			if A[i][i]!=0:
				for j in range(columns):
					if j!=i:
						if A[j][i]>0 and A[i][i]>0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=-int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=-Fraction(A[j][i]/A[i][i])
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]<0 and A[i][i]<0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=-int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(A[j][i]/abs(A[i][i]))
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]>0 and A[i][i]<0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(A[j][i]/abs(A[i][i]))
								A=Row_Transformation(A,x,i,j)
						elif A[j][i]<0 and A[i][i]>0:
							if A[j][i]%A[i][i]==0 or A[i][i]%A[j][i]==0:
								a=max(abs(A[j][i]),abs(A[i][i]))
								b=min(abs(A[j][i]),abs(A[i][i]))
								x=int(a/b)
								A=Row_Transformation(A,x,i,j)
							elif A[j][i]%A[i][i]!=0 or A[i][i]%A[j][i]!=0:
								x=Fraction(abs(A[j][i])/A[i][i])
								A=Row_Transformation(A,x,i,j)
			elif A[i][i]==0:
				for j in range(i+1,columns):
					if A[j][i]!=0:
						A=swapRows(A,j,i)
					else:
						AT=Transpose(A)
						AT=swapRows(AT,j,i)
						A=Transpose(AT)
				rank=rank-1
				i=i-1

	return rank

if __name__=='__main__':
	rows=int(input())
	columns=int(input())
	mat=[]
	rank=columns
	for i in range(rows):
		l=input()
		l=l.split()
		for j in range(len(l)):
			l[j]=int(l[j])
		mat.append(l)
		l=[]
	print(MatrixRank(mat))
