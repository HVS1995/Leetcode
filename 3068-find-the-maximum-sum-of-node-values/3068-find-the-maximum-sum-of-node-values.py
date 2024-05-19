class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        def dfs(node, parent):
            total_not, total_yes = nums[node], nums[node]^k
            for chaild in graph[node]:
                if chaild != parent:
                    xor_not, xor_yes = dfs(chaild, node)
                    total_not, total_yes = (max(xor_not+total_not, xor_yes+total_yes), 
                                            max(xor_yes+total_not, xor_not+total_yes))
            return total_not, total_yes

        graph = [[] for _ in range(len(nums))]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return dfs(0, -1)[0]