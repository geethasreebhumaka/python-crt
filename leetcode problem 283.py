#leetcode version
def movezeros(nums):
    idx=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[idx]=nums[i]
            idx+=1
    for i in range(idx,len(nums)):
        nums[i]=0
    return nums
          
nums=[0,1,0,3,12]
print(movezeros(nums))



#using copy of the bytearraydef movezeros(nums):
def movezeros(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=y+x
    print(z)
nums=[0,1,0,3,12]
movezeros(nums)


#inplace notation program
x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
    x[l],x[r]=x[r],x[l]
    l+=1
    r-=1
print(x)
    