# 미로 문제 5점
maze = [
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,1,1,1,0,0,1,1,1],
  [1,1,0,1,1,1,1,0,1,0,1],
  [1,0,0,1,1,1,1,0,1,1,1],
  [1,0,1,1,1,1,1,0,0,1,1],
  [1,0,0,0,0,0,0,0,1,1,1],
  [1,1,1,1,0,1,1,1,1,1,1],
  [1,0,0,0,0,1,1,1,1,1,1],
  [1,0,1,1,1,1,1,0,0,0,1],
  [1,0,0,0,0,0,0,0,1,0,1],
  [1,1,1,1,1,1,1,1,1,1,1]
]

mark = [
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0]
]
# 입구는 (1,1) 출구는 (9,9)
# 한 번 시도한 경로로는 다시 시도하지 않는다.

stack =[]
move =[(-1,0),(0,1),(1,0),(0,-1)]
#dirt = [0,1,2,3]
# 0,1,2,3 인덱스  // 0은 위(북) 1는 오른쪽(동) 2은 왼쪽(서) 3는 아래(남)


def mazePath(i,j):
  stack.append((i,j,move[1])) # 스택에 출발 값 넣기
  # 사방이 1일 때의 예외 제거해주기 , 배열 범위 밖은 받지 않는다.
  if i<0 or j<0 or i>11 or j>11:
    return -1
  
  while stack:
    i,j,_= stack.pop(-1) #꺼내고
    #print(i,j) # 길 좌표 
    maze[i][j]=1 #1로 바꾼다.

    # 되는 방향 찾기: 북-동-서-남 순으로!
    for x,y in move:
      dx = x+i # 다음 위치 x 
      dy = y+j # 다음 위치 y
    
      # (dx,dy)가 (9,9)면 종료
      if dx==9 and dy==9 :
        print("the path is as follows.")
        print('스택에 저장된 경로!:',stack)
        print('출구!:',dx,dy)
        print('i,j:',i,j)
        stack.pop()
        break

      # maze(dx,dy)가 0이고 와본적 없는 길(mark에서도 0)1로 바꾸고 스택 저장
      elif maze[dx][dy]==0 and mark[dx][dy]==0:
        mark[dx][dy] =1 # 시도해본 곳이면 1로 바꾸기 
        idx = move.index((x,y)) # 이동방향 move의 인덱스
        stack.append((dx,dy,move[idx])) # 이동위치, 이동방향 스택에 저장 
        continue
        
      else:
        continue

mazePath(1,1)  
