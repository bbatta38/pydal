from random import randint

'''
class Matrix

Matrix representation class. Skeleton for basic operations are given. 
'''

class Matrix():
    def __init__(self, row, col):
	self.row = row
	self.col = col
	tmp = []
	for r in range(row):
	    tmp.append([])
	    for c in range(col):
		tmp[r].append(randint(-100,100))
	self.matrix = tmp

    def __repr__(self):
	res=""
	for i in range(self.row): 
	    for j in range(self.col):
		res += str(self.matrix[i][j])
		res += " " 
	    res += "\n"
	return res.rstrip("\n")

    #----------------------------------------------------------------
    # operation on a single matrix
    #----------------------------------------------------------------

    # return matrix instance that is transpose of the original matrix
    def T(self):
	return self

    # return determinant of the matrix
    def det(self):
	return self

    # return trace of the matrix
    def tr(self):
	return self

    # return inverse of the matrix
    def inv(self):
	return self

    # return gauss elimination
    def gaussElim(self):
	return self

    # return rank
    def rank(self):
	return self
    #----------------------------------------------------------------
    # perform row operations
    #----------------------------------------------------------------
    
    # refer to http://en.wikipedia.org/wiki/Gaussian_elimination
    # Following operations should not return new matrix. 
    # Following operations should operate on self and change it.

    # swap row src and row dst
    def rowSwap(self, src, dst):
	print self

    # multiply row rowind with scala num 
    def mulRow(self, rowind, num):
	print self

    # add row src * num to row dst
    def rowAdd(self, src, dst, num):
	print self



    #----------------------------------------------------------------
    # operations on two matrices
    #----------------------------------------------------------------

    # addition
    def __add__(self, other):
	return self

    # subtraction
    def __sub__(self, other):
	return self
    
    # multiplication
    # if other is number, should return scalar multiplication result.
    # else, perform matrix multiplication
    def __mul__(self, other): 
	return self

	
