#subject 03 수건돌리기
import random
# 13명 리스트
woman = ['01-Kim','02-Lee','03-Hur','04-Choi','05-Ho','06-Sin','07-Kang',
'08-Li','09-Hwang','10-Song','11-Jung','12-Oh','13-Park']


# 노드 생성
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 원형 연결리스트로  풀기 
class LinkedList:
    def __init__(self):
        self.head = None
     

    # 연결 리스트에 sortList 값 넣기 
    def add(self,data):
      cur = self.head
      if cur == None:
        self.head = Node(data)
        self.head.next = self.head
      else:
        while cur.next != self.head:
          cur = cur.next
        cur.next = Node(data)
        cur.next.next = self.head
    

    # 인덱스로 값 접근하기 
    def access(self, idx):
        current = self.head
        i = 0
        while i < idx:
            i += 1
            current = current.next
        return current
    
    # 전체출력
    def desc(self):
        cur = self.head
        if cur == None:
          print("출력에서 값 없음.")
          return
        while cur.next != self.head:
            print (cur.data)
            cur = cur.next
        
    # rand 값까지 가는 주소
    def index(self, idx):
      cur = self.head # 첫 시작 노드 
      for _ in range(0,idx):# rand 값까지 이동
        cur = cur.next 
      return cur # 주소값 반환 

    # rand 값에서 4칸 이동(삭제할 값으로 이동)
    def cursor(self,ads):
      prev = None
      cursor = ads # 주소값을 cursor 로 지정
      for _ in range(0,4):
        prev = cursor
        cursor = cursor.next #4번 뛰어서 
      print('삭제되는 사람:',cursor.data)
      if cursor==self.head:
        self.head = cursor.next
      prev.next = cursor.next
      return cursor.next #next 반환  

    def size(self):
      cur = self.head
      size = 0
      if cur == None:
        return size
      while cur.next != self.head:
        size += 1
        cur = cur.next
      return size


sIdx = 0
eIdx = len(woman)-1
start = random.randint(sIdx,eIdx)
print('시작하는 사람 인덱스:',start)

nd = LinkedList() # head 값 

# 이 번호 포함 5번째 사람 delete, pop(print)
for i in range(0,len(woman)):
  nd.add(woman[i])
  
start -= 1

sads = nd.index(start)

while nd.size()>2:
  cur = nd.cursor(sads) # 이동하고 삭제까지
  sads = cur


#2명 남은 사람.
nd.desc()
