class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [0, 1], [-1,0 ], [0,-1]]
        rows, cols = len(heights), len(heights[0])
        visited = set()
        res = []

        def dfs(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in directions:    
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue

                if 0 <= nr < rows and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc)




        for i in range(rows):
            for j in range(cols):
                visited = set()
                dfs(i, j)
                pac = False
                atl = False
                for r, c in visited:
                    if r == 0 or c == 0:
                        pac = True
                    if r == rows - 1 or c == cols - 1:
                        atl = True
                if pac and atl:
                    res.append([i, j])
                    

        return res
        