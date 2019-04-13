class Solution:
	def threeSumClosest(self, A, B):
	    A.sort() 
	    Dict = {}
	    Dict[0] = float("inf")
	    for i in range(0, len(A)-2): 
	        l = i + 1
	        r = len(A)-1
	        while (l < r): 
	            Exp_Sum = A[i] + A[l] + A[r]
	            Min_diff = abs(Exp_Sum-B)
	            
	            if( Exp_Sum  == B):  
	                return Exp_Sum
	            
	            elif (A[i] + A[l] + A[r] < B):
	                if Dict.values()[0]>=Min_diff:  
	                    Dict = {}
	                    Dict[Exp_Sum] = Min_diff

	                l += 1
	            else: 
	                if Dict.values()[0]>=Min_diff:
	                    Dict = {}
	                    Dict[Exp_Sum] = Min_diff
	                r -= 1

	    return Dict.keys()[0]
#__ Main Function __
"""
inp = raw_input() 			# input A format eg: -1 2 1 4
inp = inp.split(" ")
A=[]
for i in range(0,len(inp)):
	A.append(int(inp[i]))

B = input()
k = Solution()
Out = k.threeSumClosest(A,B)
print Out
"""

