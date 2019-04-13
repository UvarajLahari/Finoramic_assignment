
class Solution:
    def braces(self, A):
        Stack_list = []
        for char in range(0,len(A)):
            if (A[char] != ")"):
                Stack_list.append(A[char])
        
            elif (A[char] == ")"):
                count = 0
                for i in range(len(Stack_list)-1,-1,-1):
                    if (Stack_list[i] != "("):
                        Stack_list=Stack_list[:-1]
                        count = count + 1
        
                    else:
                        Stack_list=Stack_list[:-1]
                        if (count <= 1):
                            return 1
                        break
        
        return 0

#__ Main Function __
"""
A = raw_input() Input A format eg : ((a+b))
Obj = Solution()
Out = Obj.braces(A)
print Out
"""