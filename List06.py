def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    ls = []
    
    i = 0
    l = []
    
    while i < len(list1):
        if list1[i]==1:
            list1[i]=["True"]
            ls += list1[i]
        else:
            list1[i]=[0]
            ls +=list1[i]
        i +=1
    return l +ls
print(main([1,1,0,1]))