def main(list1):
    """
    A list of several elements is given. Return the first item.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i = 0
    s = 0
    while i < len(list1):
        if i == 0:
            s +=list1[i]
        i +=1
        return s
print(main([1,2,3,4,5]))
    
