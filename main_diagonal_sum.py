input_lst=list(map(int,input().split()))
r=input_lst[0]
c= input_lst[1]
lst=input_lst[2:]
def matrix(lst, r):
    if len(lst) <= r:
        return [lst]
    else:
        return [lst[:r]] + matrix(lst[r:], r)
matrix_=matrix(lst,r)
sum_=0
for i in range(r):
    for j in range(c):
        if i ==j:
            sum_+= matrix_[i][j]
print(sum_)