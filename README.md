# isPointInRectangle
Rough ideas exploring different approaches to checking if a data point is inside a rectangle

## Introduction

We examine a string of functions which determine if a point is within a rectangle. In conducting this examination, we take different approaches to solving the problem. Each function returns a **boolean** output if the point is within a rectangle specified by two sets of coordinates. The output is `True` if the point is within a rectangle and `False` otherwise. Every function accepts three parameters:

- the first parameter is a set of coordinates which defines one of the corners of the rectangle,
- the second parameter is also a set of coordinates defining the second corner,
- the third set of coordinates define a single point which is being tested.

All of the parameters are tuples, and the first parameter does not always represent the left corner of the rectangle. Neither is the second corner always the right. The function should work correctly either way. The means the first or second parameters could be the top-right (left) corner or the bottom-left (right) corner. The edges of the rectangle are also assumed to be parallel to the coordinate axes. Lastly, if the point being tested is on the side of the rectangle, it is considered to be within the rectangle. 

The list of points and output result of their respective tests given in the variable `list_of_points` will serve as initial input into the derived functions, and will be used to get first taste of their functionalities.

```python
def header():
    print('-'*20+'-'*12*3)
    print('{:^20}|{:^12}|{:^12}|{:^12}'.format('rectangle','point','calculated','given'))
    print('-'*20+'-'*12*3)
    
list_of_points = [[(1,2), (3,4), (1.5, 3.2), 'True'], [(4,3.5), (2,1), (3, 2), 'True'],
                 [(-1,0), (5,5), (6,0), 'False'], [(4,1), (2,4), (2.5,4.5), 'False'], 
                  [(1,2), (3,4), (2,2), 'True'], [(4,5), (1,1.5), (4.1,4.1), 'False'], 
                  [(2,2),(4,3),(3,3), 'True'], [(2,1),(-3,3),(1,1), 'True']] 
```

This should produce the results below for each function.


   | rectangle      | point | calculated | given
| ------------- |-------------|---------|---------|
| `[(1, 2), (3, 4)]`      |`(1.5, 3.2)` | `True` | `True`
| `[(4, 3.5), (2, 1)]`     | `(3, 2)`      | `True` | `True`
| `[(-1, 0), (5, 5)]`      |`(6, 0)` | `False` | `False`
| `[(4, 1), (2, 4)]`     | `(2.5, 4.5)`      | `False` | `False`
| `[(1, 2), (3, 4)]`      |`(2, 2)` | `True` | `True`
| `[(4, 5), (1, 1.5)]`     | `(4.1, 4.1)`      | `False` | `False`
| `[(2, 2), (4, 3)]`      |`(3, 3)` | `True` | `True`
| `[(2, 1), (-3, 3)]`     | `(1, 1)`      | `True` | `True`


As a subsequent, more involved check, a stress test is probably required. The function below is used to conduct this check. The `isIn1` function is simple, robust and seems rather accurate in its output results. This means it can serve as the standard function to which the output of the other derived functions could be compared for extensive checks in a stress test.

```python
def stress_test(func1, func2):
    '''
    Takes two functions and checks if output is equal
    Tests if point is in rectangle using randomly generated integers
    Breaks if output of two functions is different
    
    Returns: None'''
    from random import randint
    
    i=0
    while True:
        a=(randint(-15,15),randint(-15,15))
        c=(randint(-15,15),randint(-15,15))  
        
        check1 = func1((a[0],a[1]),(c[0],c[1]),(e[0],e[1]))
        check2 = func2((a[0],a[1]),(c[0],c[1]),(e[0],e[1]))

        if (check1 is True) and (check2 is True):
            i+=1
        print("func1={}; func2={}; count={}".format(check1,check2, i))
        if check1!=check2:
            break
```

## Alternative 1

As a first and obvious alternative, we could examine if the point lies within a range of continuous values bordering the rectangle. These are number lines in 2 dimensions consisting of an infinite number of points between the bounds. By checking if the data point lies within the lines that bound the rectangle, we can establish if the point lies within rectangle or not. This bound check can be accomplished using a combination of logical and relational operators.

The `isIn1` function takes three input, the coordinates of the first corner of the rectangle, the coordinates of the second corner of the rectangle and the data point to check. The conditional expression in the function exclusively conducts the check required to determine if the data point is within the rectangle.


## Alternative 2

As an alternative approach to solving the same problem, we can make a proposal that a point inside a rectangle divides such rectangle into four triangles if we consider the coordinate of the point and of any two vertices of the rectangle as making up a triangle (a sort of envelope?). This means the areas of the four triangles should be the same as the area of the rectangle, provided the point is located on or inside the rectangle.

This approach uses the areas of the individual triangles obtained using the data point to arrive at the area of the rectangle. If the two areas are the same, then the point is present in the rectangle.

The `isIn2` function serves to conduct the required check. It uses two other functions `area of triangle` and `area_of_rectangle` with which the required area calculations are carried out.


## Alternative 3

A third alternative solution uses the images of the derived rectangle across both the x- and y-axes. Any given rectangle in 2-D space should have a replica at the same distance from the x- and y-axes across the origin. A point inside the rectangle located in the positive x-y plane, for example (that is, in the first quadrant of the Cartesian plane) should be at a distance across the y-axis no more than two times the rectangle's farthest x-coordinate and no less than two times the rectangle's closest x-coordinate. The same applies across the x-axis for a projection of the rectangle across this axis.

A simple distance function can be used in this case to assess the distance of the data point from the two rectangle images and determine if the data point is located inside or outside the rectangle. This third alternative is accomplished using the `isIn3` function.


## Alternative 4

In this fourth alternative to solving the same problem, we use the respective slopes of the lines drawn from the point inside a rectangle to the different corners of the rectangle. For such a point to be present in the rectangle, the slopes of the different lines must have particular values. The line drawn from the top-right corner to the point inside the rectangle will have a positive slope. That drawn from the bottom-right to any point inside the rectangle will have a negative slope. The reverse applies to the lines drawn from the left-corners (top and bottom) of the rectangle to the point inside the rectangle. Lines drawn from qny point located outside the rectangle will differ in the nature of their slope values when assessed in the same clockwise direction, from top-right to top-left.

The formula for the slope of a line is defined as:

m = (y2 - y1)/(x2 - x1)

This means there will be edge cases relating to points which lie on the rectangle, where the values of x2 = x1 or y2 = y1. These will cause `ZeroDivisionError` in the case of the former and zeros in the case of the latter. Another edge case will be when the data point lies exactly at one of the corners of the rectangle, in which case both situations are true. Considerations have to be taken to ensure these cases properly handled.

The `rect` function has to be created to ensure that regardless of how the rectangle is originally defined in the question, we use its bottom-right and top-left vertices in our slope calculations. This guarantees uniformity of result in later calculations. This is because the value of the slope of the line derived from extending the data point to the corners of the rectangle given changes with the corner to which this line is drawn. By working only with the bottom-right and top-left points of the rectangle, we can be sure that the slope values are always correctly defined.

This alternative is achieved using the `isIn4` function.


## Comparing functions

Comparing the different functions on the simple test point below showed that `isIn1` performed best, followed closely by `isIn3`. `isIn4` did worst and `isIn2` did better than `isIn4`, but no better than `isIn3`.

```python
((3, 12), (-8, -12), (-8, 2))
```

   | function      | output | 
| ------------- |-------------|
| `isIn1`      |`366 ns ± 8.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)` 
| `isIn2`      |`2.87 µs ± 53.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)` 
| `isIn3`      |`518 ns ± 13.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)` 
| `isIn4`      |`4.11 µs ± 92.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)` 

