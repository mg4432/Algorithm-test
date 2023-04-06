def solution(genres, plays):
    answer = []
    plays = [[i, genres[i], plays[i]] for i in range(len(plays))]
    
    counter_dict = {}
    for genre in list(set(genres)) : 
        counter_dict[genre] = sum([p[2] for p in plays if p[1] == genre])
        
    counter = [[key, value] for key, value in counter_dict.items()]
    counter = sorted(counter, key = lambda x : -x[1])
        
    genre_lst = [cnt[0] for cnt in counter]
    

    # search 
    for genre in genre_lst : 
        tmp = [x for x in plays if x[1] == genre]
        tmp = sorted(tmp, key = lambda x : -x[2])
        
        if len(tmp) == 1 : 
            answer.append(tmp[0][0])
        else : 
            for i in range(2) : 
                answer.append(tmp[i][0])
    return answer