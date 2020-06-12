# subject#2- 이진검색 프로그램

# (1) Array, 2.5점
print("Array")
sortList = [1,3,5,6,7,8,11,12,14,15,24,26,42,43,49,48,51,55,56,59,66,67,69,70, 71, 73, 75, 80, 96, 99] # 0~29
sortList.sort()

def bs_array(sortList,num):
  start = 0 # index 시작점 
  end = len(sortList)-1 #index 끝

  while(start < end+1):
    M = (start+end)//2 # 중간 값 index
    if sortList[M] < num:  # 중간 값이 찾고자하는 num보다 작으면 
      start = M+1  #  왼쪽
    elif sortList[M] > num: # 중간 값이 찾고자 하는 num보다 크면
      end = M-1 # 오른쪽
    else:
      return M # 다른 경우는 같은 경우니까 return 
  return -1

print('3:',bs_array(sortList,3))
print('96:',bs_array(sortList,96))
print('15:',bs_array(sortList,15))
print('66:',bs_array(sortList,66))
print('99:',bs_array(sortList,99))


# (2) LinkedList 2.5점
import sys
print("LinkedList")
sortList = [1,3,5,6,7,8,11,12,14,15,24,26,42,43,49,48,51,55,56,59,66,67,69,70, 71, 73, 75, 80, 96, 99] # 0~29
sortList.sort()

# 노드 선언 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결리스트 만들기 
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 연결 리스트에 sortList 값 넣기 
    def add(self,data):
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
    
    # 인덱스로 값 접근하기 
    def access(self, idx):
        current = self.head
        i = 0
        while i < idx:
            i += 1
            current = current.next
        return current.data

# 연결 리스트에 값 넣기
nd = LinkedList(sortList[0])
slen = len(sortList)
for i in range(1,slen):
  nd.add(sortList[i])

# 중간 값 넣기 
def linked(num):
  start = 0
  end = slen-1

  while(start < end+1):
    M = (start+end)//2
    mdata = nd.access(M)
    if mdata < num:  # 중간 값이 찾고자하는 num보다 작으면 
      start = M+1  #  왼쪽
    elif mdata > num: # 중간 값이 찾고자 하는 num보다 크면
      end = M-1 # 오른쪽
    else:
      return M # 다른 경우는 같은 경우니까 return 
  return -1

print('3:',linked(3))
print('96:',linked(96))
print('15:',linked(15))
print('66:',linked(66))
print('99:',linked(99))


# def desc(self):
#         node = self.head
#         while node:
#             print (node.data)
#             node = node.next