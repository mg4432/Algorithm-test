from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    
    total = 0
    while truck_weights :
        total -= bridge[-1]
        bridge.rotate(1)
        bridge[0] = 0
        if total + truck_weights[0] <= weight :
            cur_truck = truck_weights.popleft()
            bridge[0] = cur_truck 
            total += cur_truck
        answer += 1  
        
    for i in range(len(bridge)) : 
        if bridge[i] != 0 : 
            break
    
    answer += (len(bridge) - i)
    return answer