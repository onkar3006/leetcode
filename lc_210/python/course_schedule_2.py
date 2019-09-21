class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        dep_on = {}
        req_for = {}
        for i in range(numCourses):
            dep_on[i] = set()
            req_for[i] = set()

        for i, j in prerequisites:
            dep_on[j].add(i)
            req_for[i].add(j)

        q = []

        for i in req_for:
            if not req_for[i]:
                q.append(i)

        while q:
            c = q.pop(0)
            res.append(c)
            for i in dep_on[c]:
                req_for[i].remove(c)
                if not req_for[i]:
                    q.append(i)
            del(dep_on[c])

        return res if not dep_on else []
