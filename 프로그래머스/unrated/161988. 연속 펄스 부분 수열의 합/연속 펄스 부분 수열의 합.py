def solution(sequence):
    sequence = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(len(sequence))]    
    
    for i in range(1, len(sequence)) : 
        sequence[i] += sequence[i-1]
    
    sequence = [0] + sequence
    
    Max, Min = 1, 1
    Max = max(sequence[1:]) - min(sequence)
    Min = abs(min(sequence[1:]) - max(sequence))
    
    return max(Max, Min)
