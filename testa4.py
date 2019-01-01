#Vidit Jain
#2017370
#A2
import unittest
from a4 import Row_Transformation
from a4 import swapRows
from a4 import MatrixRank
from a4 import Transpose

# TEST cases should cover the different boundary cases.

mat1=[[10,20,10],[-20,-30,10],[30,50,0]]
mat2=[[1,2,3,4],[0,0,0,0]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]
mat4=[[2,-1,3],[1,0,1],[0,2,-1],[1,1,4]]
mat5=[[1,2],[2,4],[3,6]]
mat6=[[1,4,7],[2,5,8],[3,6,9]]
mat7=[[1,4,5,9],[4,8,2,9],[3,9,5,8],[1,5,2,7]]
mat8=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat9=[[1,1,1],[1,1,1],[1,1,1]]
mat10=[[3],[2],[6],[5]]
mat11=[[1,-3,-5,0],[0,1,1,3]]
mat12=[[1,2,3,4],[4,5,6,7],[6,7,8,9]]
mat13=[[0,0,0],[0,0,0],[0,0,0]]
mat14=[[1,2,7],[-2,5,4],[-5,6,-3]]
mat15=[[5],[-4],[-7]]
mat16=[[3,4,5],[6,7,8]]
mat17=[[1],[2],[3]]
mat18=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
mat19=[[0,0,0],[0,0,0]]
mat20=[[1,2,3,4],[0,0,0,0]]
mat21=[[0,0,0,0],[1,2,3,4],[0,0,0,0],[1,2,3,4]]
mat22=[[1,2,3],[4,5,6],[0,0,0],[10,11,11]]

class testpoint(unittest.TestCase):
	def test_MatrixRank(self):
		self.assertEqual(MatrixRank(mat1),2)
		self.assertEqual(MatrixRank(mat2),1)
		self.assertEqual(MatrixRank(mat3),0)
		self.assertEqual(MatrixRank(mat4),3)
		self.assertEqual(MatrixRank(mat5),1)
		self.assertEqual(MatrixRank(mat21),1)
		self.assertEqual(MatrixRank(mat22),3)
	
	def test_swapRows(self):
		self.assertEqual(swapRows(mat6,0,2),[[3,6,9],[2,5,8],[1,4,7]])
		self.assertEqual(swapRows(mat7,1,3),[[1,4,5,9],[1,5,2,7],[3,9,5,8],[4,8,2,9]])
		self.assertEqual(swapRows(mat8,1,2),[[1,2,3,4],[9,10,11,12],[5,6,7,8]])
		self.assertEqual(swapRows(mat9,0,2),[[1,1,1],[1,1,1],[1,1,1]])
		self.assertEqual(swapRows(mat10,0,3),[[5],[2],[6],[3]])
	
	def test_Row_Transformation(self):
		self.assertEqual(Row_Transformation(mat11,3,0,1),[[1,-3,-5,0],[3,-8,-14,3]])
		self.assertEqual(Row_Transformation(mat12,-1,0,2),[[1,2,3,4],[4,5,6,7],[5,5,5,5]])
		self.assertEqual(Row_Transformation(mat13,3,1,2),[[0,0,0],[0,0,0],[0,0,0]])
		self.assertEqual(Row_Transformation(mat14,-2,2,0),[[11,-10,13],[-2,5,4],[-5,6,-3]])
		self.assertEqual(Row_Transformation(mat15,1,1,0),[[1],[-4],[-7]])

	def test_Transpose(self):
		self.assertEqual(Transpose(mat16),[[3,6],[4,7],[5,8]])
		self.assertEqual(Transpose(mat17),[[1,2,3]])
		self.assertEqual(Transpose(mat18),[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
		self.assertEqual(Transpose(mat19),[[0,0],[0,0],[0,0]])
		self.assertEqual(Transpose(mat20),[[1,0],[2,0],[3,0],[4,0]])
		
if __name__=='__main__':
    unittest.main()
