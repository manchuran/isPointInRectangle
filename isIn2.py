def area_of_triangle(first_vertix,second_vertix,third_vertix):
    '''
    Calculates area of triangle using three vertices
    Returns: area of triangle
    '''
    # Calculate area of triangle from three vertices
    x1, y1 = first_vertix[0], first_vertix[1]
    x2, y2 = second_vertix[0], second_vertix[1]
    x3, y3 = third_vertix[0], third_vertix[1]
    return abs(x1*(y2-y3) + x2*(y3-y1)+x3*(y1-y2))/2


def area_of_rectangle(first_vertix,second_vertix):
    '''
    Calculates area of rectangle using two corner vertices
    Returns: area of rectangle
    '''
    # Calculate area of rectangle from two vertices (parallel to axes)
    x1, y1 = first_vertix[0], first_vertix[1]
    x2, y2 = second_vertix[0], second_vertix[1]
    B = abs(x1 - x2)*abs(y1 - y2)
    return B
    

def isIn2(firstCorner=(0,0), secondCorner=(0,0), point=(0,0)):
    '''
    Checks if point is in rectangle
    
    Returns: True if point is in rectangle; False otherwise
    '''
    # Determine if point is inside rectangle

    x, y = point[0], point[1]
    a1, b1 = firstCorner[0], firstCorner[1]
    a3, b3 = secondCorner[0], secondCorner[1]
    
    # Establish four vertices of Rectangle
    a2, b2 = a1, b3
    a4, b4 = a3, b1
    
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
        
    # Calculate area of individual triangles
    A1 = area_of_triangle((a4,b4),(a1,b1),(x,y))
    A2 = area_of_triangle((a1,b1),(a2,b2),(x,y))
    A3 = area_of_triangle((a2,b2),(a3,b3),(x,y))
    A4 = area_of_triangle((a3,b3),(a4,b4),(x,y))
    
    area_of_4_triangles = abs(A1 + A2 + A3 + A4)
    area_rectangle = area_of_rectangle(firstCorner, secondCorner)
    
    if area_of_4_triangles == area_rectangle:
        return True
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
                                            str(item[2]),str(isIn2(*args)), item[3]))
    