# Time Complexity : O(V+E)
# space complexity : O(V+E)

# Approach :

# since one subject can have more than one dependancy, it is a graph problem
# create a indegree array, which stores the number of dependancies each course has
# create a hashmap which stores the key as the independent subject and values as list of subjects dependant on it
# iterate over the indegree array to check if there are any courses with value 0 ( indicates independant course) and keep a count of it and append it to a queue
# traverse the queue, and pop the independant course
# check the hashmap for the independant course, and iterate over the list of values and deduct 1 from each of them in the indegree array
# check again if any indegree array has 0 and keep appending it in the queue.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not numCourses:
            return False

        if not prerequisites:
            return True

        indegree = [0]*numCourses
        self.hashMap = dict()
        count = 0

        for i in range(len(prerequisites)):

            indegree[prerequisites[i][0]] = indegree[prerequisites[i][0]]+1
            if prerequisites[i][1] not in self.hashMap:
                self.hashMap[prerequisites[i][1]] = []
            self.hashMap[prerequisites[i][1]].append(prerequisites[i][0])

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                count = count+1

        while q:

            poppedVal = q.popleft()
            if poppedVal in self.hashMap:
                for items in self.hashMap[poppedVal]:
                    indegree[items] = indegree[items]-1
                    if indegree[items] == 0:
                        q.append(items)
                        count = count+1

        return count == numCourses
