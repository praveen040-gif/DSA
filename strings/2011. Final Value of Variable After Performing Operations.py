def finalValueAfterOperations(self, operations: List[str]) -> int:
    x=0
    for word in operations:
        if word=="X++" or word=="++X":
            x+=1
        else:
            x-=1
    return x 