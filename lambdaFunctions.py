list1= [2,4,6,8,10,12,14, 16]
#using map to print the square of all the numbers in list)
mapResult= list(map(lambda x: x*x, list1))
print("The mapperd result: ", mapResult)
print()

#using filter to filter the sqaures less than or equals to 100
filterResult = list(filter(lambda x: x<=100, mapResult))
print("The filtered result: ", filterResult)
print()

#using reduce to find the product of the filteredResult when initial value 2 is given and when initial value is not given

from functools import reduce
#When initial value is not  given
reduceResult= reduce(lambda x, y: x*y, filterResult)
print("The reduced result when no initial is given: ", reduceResult)

#When initial value is given
reduceResult1= reduce(lambda x, y: x*y, filterResult, 2)
print("The reduced result when no initial is given: ", reduceResult1)
