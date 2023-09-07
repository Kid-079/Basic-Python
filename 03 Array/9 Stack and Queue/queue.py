from collections import deque

List = deque([1,2,3,4,5,6])
print('Queue List :', List)

# Add Data
List.append(7)
print('Input : ', 7)
print('Queue List Now : ', List)

# Queue --> Reduce Data from ahead
out = List.popleft()
print('Output : ', out)
print('Queue List Now : ', List)

out = List.popleft()
print('Output : ', out)
print('Queue List Now : ', List)

# Add Data
out = List.append(8)
print('Input : ', 8)
print('Queue List Now : ', List)

# Queue --> Reduce Data from ahead
out = List.popleft()
print('Output : ', out)
print('Queue List Now : ', List)