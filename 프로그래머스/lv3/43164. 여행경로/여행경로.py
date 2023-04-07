def solution(tickets):
    path = []
    
    # graph 
    graph = dict()
    for s, e in tickets : 
        if s in graph : 
            graph[s].append(e)
        else : 
            graph[s] = [e]
    
    # 도착점 리스트 정렬 
    for key in graph.keys() : 
        graph[key].sort(reverse = True)
        
    # 출발지 ICN stack에 입력 
    stack = ['ICN']
    print(stack)
    # 모든 노드 순회
    while stack : 
        # stack에서 가장 위의 노드 꺼내오기
        top = stack.pop()
        
        # top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장 
        if top not in graph or not graph[top] :
            print('not top')
            path.append(top) 
        
        else : 
            print('top')
            stack.append(top) 
            stack.append(graph[top].pop())
        print('top : ', top, 'stack : ', stack, 'path : ', path)
    return path[::-1]