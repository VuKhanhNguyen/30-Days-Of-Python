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

xi = - findIntercept(e) / findSlope(e)
print(f"X-intercept là: ({xi},0)")
yi = findIntercept(e)
print(f"Y-intercept là: (0,{yi})")
slope=findSlope(e)
print(f"Hệ số góc (slope) là: {slope}")