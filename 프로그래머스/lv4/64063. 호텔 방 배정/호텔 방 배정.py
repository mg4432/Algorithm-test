def solution(k, room_number):
    room_dict = {} 
    answer = []
    for i in room_number : 
        n = i # 손님이 지정한 방 
        visit = [n]
        while n in room_dict :
            n = room_dict[n]
            visit.append(n)
        answer.append(n)
        for j in visit : 
            room_dict[j] = n + 1
        
    return answer