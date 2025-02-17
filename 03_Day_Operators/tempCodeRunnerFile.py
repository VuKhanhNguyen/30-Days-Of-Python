import math
print("Nhập vào 3 cạnh của tam giác: ")
while True:
    try:
        a = float(input(f"Nhập cạnh a: "))
        if a<=0 or not a.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        b = float(input(f"Nhập cạnh b: "))
        if b<=0 or not b.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        c = float(input(f"Nhập cạnh c: "))
        if c<=0 or not c.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        break
    except ValueError:
        print("Nhập sai mời nhập lại!")
perimeter = a + b + c
print(f'Chu vi của tam giác là: ', perimeter)       