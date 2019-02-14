
def check_overlap(l1,l2):
    # for overlap: lines partially overlap,at point or complete overlap
    big_line,short_line = (l1,l2) if l1[1]>l2[1] else (l2,l1)

    #for no-overlap: short_line highest point < big_line lowest point
    print("overlap found at {0} to {1}".
          format(max(big_line[0],short_line[0]),
          short_line[1])) if big_line[0]<= short_line[1] else print("no overlap")





if __name__ == "__main__":
    # user input
    l1 = sorted(tuple(map(int,input("Enter line 1 \n").split(","))))
    l2 = sorted(tuple(map(int,input("Enter line 2 \n").split(","))))

    #input is sorted for consistency
    print("Line 1 is {0},{1}".format(*l1))
    print("Line 2 is {0},{1}".format(*l2))

    check_overlap(l1,l2)


'''
testcases:
no-overlap : (1,2),(3,4)
overlap :
    partial : (-1,2),(0,3)
    total : (2,4),(2,3)
    point : (4,2),(1,2)

cases not covered :
    1.assumed user always enter integers
    2.user enters 2 digits seperated with ","
'''
