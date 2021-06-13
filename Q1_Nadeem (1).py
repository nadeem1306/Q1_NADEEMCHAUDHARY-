def run():
    n=int(input())
    if n<1:
        print("Invalid Input")
        return
    else:
        arr=[]
        for i in range(n+1):
            x=str(input())
            arr.append(x)
        
        arr.sort(key=len)
        print(arr)
run()