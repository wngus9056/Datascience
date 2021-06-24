a = [(1, 2, 8), (3, 4, 5), (5, 6, 3)]   # a에 (1, 2, 8), (3, 4, 5), (5, 6, 3) 3개 값을 저장하고

for (first, middle, last) in a:     # 1번째 for문 돌 때 (1, 2, 8)에서 1은 first, 2는 middel, 8은 last에 각각 저장해주고
	print (first + last + middle)   # (1 + 2 + 8) 값을 출력한다.
    
                                    # 2번째 for문 돌 때 (3, 4, 5)에서 3은 first, 4는 middel, 5은 last에 각각 저장해주고
                                    # (3 + 4 + 5) 값을 출력한다. 
                                    # ...
                                    # ...