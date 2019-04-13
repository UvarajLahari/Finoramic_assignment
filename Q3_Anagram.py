
class Solution:
    def anagrams(self, A):
        Anagram_grp = []
        visited = [0]*len(A)
        freq = []
        for each in A:
            Dict ={}
            for char in each:
                
                if char not in Dict.keys():
                    Dict[char] = 1
                else:
                    Dict[char] = Dict[char] +1
            freq.append(Dict)
        for each in range(0,len(A)):
            if(visited[each] == 0):
                Grp = []
                Grp.append(each+1)
                for other in range(each+1,len(A)):
                    if (cmp(freq[each],freq[other])==0):
                        Grp.append(other+1)
                        visited[other] = 1
                if len(Grp) >= 1:
                    Anagram_grp.append(Grp)
        
        return Anagram_grp
#__ Main Function __
"""
A = raw_input() 	#input A format eg : cat dog god tca
A = A.split(" ")
Obj = Solution()
Out_list = []
Out_list = Obj.anagrams(A)
print Out_list
"""