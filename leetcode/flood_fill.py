# https://leetcode.com/problems/flood-fill/


class Solution(object):

    def __init__(self):
        self.neighbor = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.visited = []
        self.image = []

    def validpoint(self, sr, sc):
        print(sr,sc)
        isvalid = (not (sr < 0 or sr == self.maxr or sc < 0 or sc == self.maxc)) and\
            (self.image[sr][sc] == self.base_color) and\
            (not self.visited[sr][sc])
        # print(sr,sc, isvalid)
        return(isvalid)

    # to decide upon dfs/bfs

    def dfs(self, sr, sc):
        self.visited[sr][sc] = True
        for n in self.neighbor:
            if (self.validpoint(sr+n[0], sc+n[1])):
                self.dfs(sr+n[0], sc+n[1])

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.maxc = len(image[0])
        self.maxr = len(image)
        self.base_color = image[sr][sc]
        self.image = image
        self.visited = [[False for _ in range(self.maxr)] for _ in range(self.maxc)]
        # ([[False]*self.maxc]*self.maxr)

        # self.visited[sr][sc] = True
        
        self.dfs(sr, sc)
        # print(self.visited)

        for i in range(self.maxr):
            for j in range(self.maxc):
                if(self.visited[i][j]):
                    self.image[i][j] = color 
        return (self.image)
