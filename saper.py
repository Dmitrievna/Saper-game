import copy


n , m = map (int, input().split(' '))

playground = []

inputN = 0

while ( inputN != n ):
	playground.append(list(input()))
	inputN+=1


resultGround = [ [0]*(m + 2) for x in range(n+2) ]



for i in range(1,n+1):
	for j in range(1,m+1):
		if ( i-1 < n and j-1 < m ):
			if (playground[i-1][j-1] == "*"):
				resultGround[i][j] = "*"
				if(resultGround[i+1][j] != "*"):
					resultGround[i+1][j]+=1
				if(resultGround[i+1][j+1] != "*"):
					resultGround[i+1][j+1]+=1
				if(resultGround[i][j+1] != "*"):
					resultGround[i][j+1]+=1
				if(resultGround[i-1][j] != "*"):
					resultGround[i-1][j]+=1
				if(resultGround[i-1][j-1] != "*"):
					resultGround[i-1][j-1]+=1
				if(resultGround[i][j-1] != "*"):
					resultGround[i][j-1]+=1
				if(resultGround[i+1][j-1] != "*"):
					resultGround[i+1][j-1]+=1
				if(resultGround[i-1][j+1] != "*"):
					resultGround[i-1][j+1]+=1


for i in range(1,n+1):
	for j in range(1,m+1):
		print(resultGround[i][j])





			
		