class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[0])
        n, arrows = len(points), 1
        i = 1
        intersect = points[0]
        while i < n:
            if points[i][0] <= intersect[1]:
                intersect = [points[i][0], min(points[i][1], intersect[1])]
            else:
                arrows += 1
                intersect = points[i]
            i += 1
        return arrows


class Solution2:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        prev_end = points[0][1]
        arrows = 1
        for start, end in points[1:]:
            if start > prev_end:
                arrows += 1
                prev_end = end
        return arrows


s = Solution()
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(s.findMinArrowShots(points))
