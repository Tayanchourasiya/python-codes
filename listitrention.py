my_list = [1,2,3,4,5,1,3,4,1,2,1,2,8,0,5,6,2,3,4,5,6,7,8,9,7,6,4,5,2,2,4,6,1,4]
def non_dup(a):
    n = sorted(set(a))
    itre_count(n)   
def itre_count(b):
    for i in b:
        print(str(i)+" =",my_list.count(i))
non_dup(my_list)
  
