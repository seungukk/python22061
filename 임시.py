# 임시
def change(x):
    #복사본(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

#호출
wordlist = ["J","A","M"]
change(wordlist)