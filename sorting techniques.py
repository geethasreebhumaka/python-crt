'''#bubble sort technique
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=list(map(int,input().split()))
bubble_sort(arr)
print("sorted array:",arr)'''

#insertion sort technique
def insertion_sort(arr):
    for i in range(1,len(arr)):
        start=arr[i]
        j=i-1 
        while j>=0 and start<arr[j]:
            arr[j+1]=arr[j]
            j-=1 
        arr[j+1]=start
arr=list(map(int,input().split()))
insertion_sort(arr)
print("sorted array:",arr)

#selection_sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        lower=i 
        for j in range(i+1,n):
           if arr[j]<arr[lower]:
              lower=j 
        arr[i],arr[lower]=arr[lower],arr[i]
arr=list(map(int,input().split()))
selection_sort(arr)
print("sorted array:",arr)