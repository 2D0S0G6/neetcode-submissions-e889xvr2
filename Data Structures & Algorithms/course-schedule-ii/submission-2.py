class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)  
        indegree = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course]-=1
                if indegree[next_course] == 0:
                    q.append(next_course)
             
        return order if len(order) == numCourses else []
