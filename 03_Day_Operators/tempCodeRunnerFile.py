def findSlope(e):
    p = e.replace("y=","").split("x")
    s = float(p[0])    
    # i = float(p[1])
    return s

def findIntercept(e):    
    p = e.replace("y=","").split("x")
    # s = float(p[0])    
    i = float(p[1])
    return i
      
e = "y=2x-2"

slope=findSlope(e)
print(f"Hệ số góc (slope) là: {slope}")

xi = - findIntercept(e) / findSlope(e)
print(f"X-intercept là: ({xi},0)")

yi = findIntercept(e)
print(f"Y-intercept là: (0,{yi})")

#================================================================
# breakpoint()
# e = "y = 2x-2"
# p = e.replace("y = ", "").split("x")
# s = float(p[0])
# i = float(p[1])

# print(f"Hệ số góc (slope) là: {s}")
# yi = s * 0 + i
# print(f"Y-intercept là: {yi}")
# xi = -i / s
# print(f"X-intercept là: {xi}")

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1=2 
y1=2
x2=6 
y2=10
#x1, y1, x2, y2 = 1, 2, 4, 6 
def findSlope(m):
    # m = float((y2-y1)/(x2-x1))
    print(f"Hệ số góc m={m}")
    return m

def findEuclideanDistance(x1,y1,x2,y2):
    d = math.sqrt((pow(x2-x1,2))+(pow(y2-y1,2)))
    print(f"Khoảng cách là: {d}") 
    return d

m = float((y2-y1)/(x2-x1))
s9 = findSlope(m)
s9_2 = findEuclideanDistance(x1,y1,x2,y2)

#10. Compare the slopes in tasks 8 and 9.

if slope == s9:
    print("Hệ tọa độ của bài 8 và 9 bằng nhau")
elif slope > s9:
    print("Hệ tọa độ của bài 8 lớn hơn bài 9")    
else:
    print("Hệ tọa độ của bài 8 bé hơn bài 9")
    