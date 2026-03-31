def common_elements(lst1, lst2):
    result = []
    
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
            
    return result

# Example
print(common_elements([1,2,3], [2,3,4]))  # [2,3]

#output-def common_elements(lst1, lst2):
result = []
    
for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
            
return result

# Example
print(common_elements([1,2,3], [2,3,4]))  # [2,3]

#output: [2, 3]
