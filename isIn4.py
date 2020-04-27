def rect(firstCorner,secondCorner, k):
    '''
    Determines the bottom-right and top-left corners of a rectangle 
    regardless how its corners are originally stated
    
    Returns: bottom-right and top-left vertices of rectangle
    '''
    
    # Initialize placeholders
    a=[0,0,0,0]
    b=[0,0,0,0]
    
    # Determine other two vertices of rectangle
    a[(1+k)%4], b[(1+k)%4] = firstCorner[0], firstCorner[1]
    a[(3+k)%4], b[(3+k)%4] = secondCorner[0], secondCorner[1]
    
    # Establish four uniform vertices of Rectangle
    a[(2+k)%4], b[(2+k)%4] = a[(1+k)%4], b[(3+k)%4]
    a[(0+k)%4], b[(0+k)%4] = a[(3+k)%4], b[(1+k)%4]

    if k%2 != 0:
        temp = a[3],b[3]
        a[3],b[3]=a[1],b[1]
        a[1],b[1]=temp
        

    return a,b


# Define slope function
import math
def slope(a,b):
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    
    try:
        slope = (y2-y1)/(x2-x1)
    except ZeroDivisionError:
        if y1>y2:
            return -math.inf
        elif y1==y2:
            return "point"
        return math.inf
    return slope
    
    
def isIn4(firstCorner=(0,0), secondCorner=(0,0), point=(0,0)):

    a1,b1=firstCorner[0], firstCorner[1]
    a3,b3=secondCorner[0], secondCorner[1]
    x, y = point[0], point[1]
    
    # Treats edge case. Establish if rectangle is a line and point is outside of this line
    if b1==b3:
        if b1==b3==y:
            if (a1<=x<=a3) or (a1>=x>=a3):
                return True
            else:
                return False
        else:
            return False
    elif a1==a3:
        if a1==a3==x:
            if (b1<=y<=b3) or (b1>=y>=b3):
                return True
            else:
                return False
        else:
            return False
    
    # Establish vertices of rectangle
    a,b=0,0
    k=0
    rect_sides = {}
    if a1 < a3:
        if b1 < b3:
            rect_sides['bottom left'] = (a1,b1)
            rect_sides['top right'] = (a3, b3)
            k=0
            a,b=rect(rect_sides['bottom left'],rect_sides['top right'], k)
        if b1 > b3:
            rect_sides['top left'] = (a1,b1)
            rect_sides['bottom right'] = (a3,b3)
            k=1
            a,b=rect(rect_sides['top left'],rect_sides['bottom right'], k)
    elif a1 > a3:
        if b1 > b3:
            rect_sides['top right'] = (a1,b1)
            rect_sides['bottom left'] = (a3,b3)
            k=2
            a,b=rect(rect_sides['top right'],rect_sides['bottom left'], k)
        if b1 < b3:
            rect_sides['bottom right'] = (a1,b1)
            rect_sides['top left'] = (a3,b3)
            k=3
            a,b=rect(rect_sides['bottom right'],rect_sides['top left'], k)
    
    

    if point == (a[1],b[1]) or point == (a[2],b[2]) or point == (a[3],b[3]) or \
    point == (a[0],b[0]):
        return True
    
    # Carry out slope calculations. There will be four slopes in total.
    # if point is in rectangle, then slope of point from bottom left corner should
    # range from +Inf to 0 and have positive values
    slope1 = slope((a[1],b[1]), (x,y))   
    slope2 = slope((a[2],b[2]), (x,y)) 
    slope3 = slope((x,y), (a[3],b[3]))
    slope4 = slope((x,y), (a[0],b[0]))
    

    # Conduct final check with slopes
    if ((0<=slope1<=math.inf)) \
    and ((-math.inf<=slope2<=0)) \
    and ((0<=slope3<=math.inf)) \
    and ((-math.inf<=slope4<=0)):
        return True
    else:
        return False
    

def header():
    print('-'*20+'-'*12*3)
    print('{:^20}|{:^12}|{:^12}|{:^12}'.format('rectangle','point','calculated','given'))
    print('-'*20+'-'*12*3) 

   
if __name__ == '__main__':
    list_of_points = [[(1,2), (3,4), (1.5, 3.2), 'True'], [(4,3.5), (2,1), (3, 2), 'True'],
                 [(-1,0), (5,5), (6,0), 'False'], [(4,1), (2,4), (2.5,4.5), 'False'], 
                  [(1,2), (3,4), (2,2), 'True'], [(4,5), (1,1.5), (4.1,4.1), 'False'], [(2,2),(4,3),(3,3), 'True'], 
                 [(2,1),(-3,3),(1,1), 'True']] 
    header()
    for item in list_of_points:
    	args = item[:3]
    	print('{:<20}{:^14}{:^14}{:^9}'.format(str(item[:2]),
                                            str(item[2]),str(isIn4(*args)), item[3]))
    