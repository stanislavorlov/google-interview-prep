def towersHanoi(n: int, source: [], helper: [], target: []):
    if n > 0:
        towersHanoi(n-1, source, target, helper)
        if source:
            target.append(source.pop())
            
        towersHanoi(n-1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []

towersHanoi(len(source), source, helper, target)

print(source, target, helper)