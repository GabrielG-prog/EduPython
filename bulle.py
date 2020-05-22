tb=[6,3,7,2,3,5]

def comparer():
    rang=0
    while rang != len(tb):
        if tb[rang]>tb[rang+1] and rang <=len(tb):
            x=tb[range+1]
            tb[range+1]=tb[rang]
            tb[rang]=x

        rang=rang+1

    print(tb)


