import sys
import string



def string_filter(versions):
    q = map(lambda x : list(map(int,x.split("_")[1].split("."))),versions)
    for v1,v2 in zip(*q):
        if v1>v2:
            print("{} is the latest version".format(versions[0]))
            break
        if v2> v1:
            print("{} is the latest version".format(versions[1]))
            break

    
    


    
    
if __name__ == "__main__":
    versions = sys.argv[1:]
    string_filter(versions)
    
'''
string examples :
app_1.23
app_1.0.2
app_2.31
'''


