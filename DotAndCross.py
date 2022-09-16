import numpy

n=int(input())

mat1 = numpy.array([input().split() for x in range(n)],int)
mat2 = numpy.array([input().split() for x in range(n)],int)

res = numpy.dot(mat1,mat2)

print (res)
