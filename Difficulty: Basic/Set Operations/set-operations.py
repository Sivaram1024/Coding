def setInsert(arr, n):
    return set(arr)
    #code here
    
def setDisplay(s):
    for i in sorted(s):
        print(i , end = " ")
    print()
    
def setErase(s, x):
    if x in s:
        s.remove(x)
        print(f"erased {x}")
    else:
        print("not found")
        
    return s
