def convert(skill, skill_tree) :
    skill_tree = list(skill_tree) 
    skill_tree = [s for s in skill_tree if s in skill]
    return ''.join(skill_tree)
    

def solution(skill, skill_trees):
    answer = -1
    skill_trees = [convert(skill, skill_tree) for skill_tree in skill_trees]
    skill_trees = [1 if s == skill[:len(s)] else 0 for s in skill_trees]
    return sum(skill_trees)