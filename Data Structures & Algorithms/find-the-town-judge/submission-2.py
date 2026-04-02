class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {}
        outgoing = {}

        for src, dst in trust:
            incoming[dst] = 1 + incoming.get(dst, 0) 
            outgoing[src] = 1 + outgoing.get(src, 0)

        for i in range(1, n+1):
            if i not in outgoing and i in incoming:
                if incoming[i] == n-1:
                    return i
        return -1