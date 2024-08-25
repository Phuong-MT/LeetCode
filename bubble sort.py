import random
def sinh_mang(n):
    mang = []
    for i in range (n):
        mang.append(random.randint(0,100))
    return mang
def bubble_sort(mang):
    size = len(mang)
    for i in range (size-1,0,-1):
        for j in range (1, i+1):
            if(mang[j-1]>mang[i]):
                mang[j-1],mang[i] = mang[i], mang[j-1]
                print(mang)
if __name__ =="__main__":
    n = int(input("nhap chieu dai cua mang "))
    mang = sinh_mang(n)
    print("mang ban dau la ",mang)
    bubble_sort(mang)
    print("mang sau khi swap la ", mang)
