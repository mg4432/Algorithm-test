def solution(genres, plays):
    answer = []
    genre_dict = {} 
    
    for i in range(len(genres)) :
        gen, play = genres[i], plays[i]
        if gen in genre_dict : 
            genre_dict[gen] += play
        else : 
            genre_dict[gen] = play
            
    genre_rank = sorted(genre_dict.items(), key = lambda item : item[1], reverse = True)
    genre_rank = [pair[0] for pair in genre_rank]
    
    pair_dict = {}
    for i in range(len(genres)) : 
        pair_dict[i] = (genres[i], plays[i])
        
    for gr in genre_rank : 
        lst = [(k, v[1])  for k, v in pair_dict.items() if v[0] == gr]
        lst = sorted(lst, key = lambda x : x[1], reverse = True)[:2]
        lst = [x[0] for x in lst]
        answer.extend(lst)
        
    return answer