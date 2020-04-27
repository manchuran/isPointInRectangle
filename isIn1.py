def isIn1(firstCorner=(0,0), secondCorner=(0,0), point=(0,0)):
    '''
    Checks if point is in rectangle
    
    Returns: True if point is in rectangle; False otherwise
    '''

    x, y = point[0], point[1]
    x1, y1 = firstCorner[0], firstCorner[1]
    x2, y2 = secondCorner[0], secondCorner[1]
    
    if ((x1 >= x >= x2) and (y1 <= y <= y2)) or \
    ((x1 <= x <= x2) and (y1 <= y <= y2)) or \
    ((x1 <= x <= x2) and (y1 >= y >= y2)) or \
    ((x1 >= x >= x2) and (y1 >= y >= y2)):
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
                                            str(item[2]),str(isIn1(*args)), item[3]))
    