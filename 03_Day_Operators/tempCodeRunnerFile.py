def checkEvenNumber(n):
    if(n%2 == 0):
        return(f"Đây là số chẵn")
    return(f"Đây là số lẻ")
while True: 
    num=int(input("Nhập 1 số: "))
    print(checkEvenNumber(num))     
    break