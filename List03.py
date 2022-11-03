def main(list1,list2):
    """
    lists list1 and list2 are given. Add them (combine) and return.
    Args:
        list1 (list): parameter
        list2 (list): parameter
    Returns:
        list: return answer
    """
    list3 = list1 + list2
    return list3
print(main([1,"x",3],["z",5,6]))