class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        prereq_for = {}
        for i in range(numCourses):
            prereq_for[i] = set()

        for course, prereq in prerequisites:
            prereq_for[course].add(prereq)

        q = []
        for course in range(numCourses):
            if not prereq_for[course]:
                q.append(course)
                del(prereq_for[course])

        while q:
            curr_course = q.pop(0)
            for course, prereq in prereq_for.items():
                if curr_course in prereq:
                    prereq.remove(curr_course)
                    if not prereq:
                        q.append(course)
                        del(prereq_for[course])

        return not prereq_for
