def solution(nums):
    length = len(nums)
    half = divmod(length, 2)[0]
    dict_ = {}
    
    for n in nums :
        if n in dict_ : 
            dict_[n] += 1 
        else : 
            dict_[n] = 1 
    
    if len(dict_) >= half :
        return half
    else : 
        return len(dict_)
