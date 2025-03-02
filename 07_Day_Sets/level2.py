# 1. Join A and B
# 1. Find A intersection B
# 1. Is A subset of B
# 1. Are A and B disjoint sets
# 1. Join A with B and B with A
# 1. What is the symmetric difference between A and B
# 1. Delete the sets completely

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Hợp 2 set 
C = A.union(B)
print(C)

#Giao 2 set
D = A.intersection(B)
print(D)

#Tập hợp con
E = A.issubset(B)
print(E)

#Check isdisjoint() nếu có phần tử chung thì false, ngược lại thì true(tức là chúng rời rạc)
F = A.isdisjoint(B)
print(F)

G = A.union(B)
H = B.union(A)
print(f'{G}\n{H}')

#(A\B)∪(B\A) nghĩa là A hiệu B (lấy A không lấy B và phần chung của A và B) hợp với B hiệu A (lấy B không lấy A và phần chung của A và B)
I = A.symmetric_difference(B)
print(I)

try:
    del A
    del B
    print(A)
    print(B)
    print('Đã xóa set A và set B')
except NameError as n:
    print(f'Lỗi {n}')   