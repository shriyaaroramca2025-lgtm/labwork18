def find_pairs(lst, target):
    pairs = []
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
                
    return pairs

# Example
print(find_pairs([1,2,3,4,5], 5))  

#Output- [(1,4), (2,3)]
