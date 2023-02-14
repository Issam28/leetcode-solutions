class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
                
        def backtrack(i, path, curr_sum, curr_len):
            
            if curr_len > k or curr_sum > n:
                return
            if curr_len == k and curr_sum == n:
                res.append(path)
                return
            for j in range(i,10):
                backtrack(j+1,path+[j],curr_sum+j,curr_len+1)

        res = []
        backtrack(1,[],0,0)
        return res
