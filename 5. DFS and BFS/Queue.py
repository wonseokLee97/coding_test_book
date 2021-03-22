from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()


# 삽입, 삭제

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)



# 5 - 2 - 3 - 7 - 1 -4