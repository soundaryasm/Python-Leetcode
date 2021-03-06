# # # # -*- coding: utf-8 -*-
import collections

class Solution(object):
    def removeStones(self, points):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, j in points:
            rows[i].add(j)
            cols[j].add(i)

        def dfsRow(i):
            seenR.add(i)
            for j in rows[i]:
                if j not in seenC:
                    dfsCol(j)

        def dfsCol(j):
            seenC.add(j)
            for i in cols[j]:
                if i not in seenR:
                    dfsRow(i)

        seenR, seenC = set(), set()
        islands = 0
        for i, j in points:
            if i not in seenR:
                islands += 1
                dfsRow(i)
                dfsCol(j)
        return len(points) - islands

if __name__ == '__main__':
    s = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(s.removeStones(stones))
