
#Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

#However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

#You need to return the least number of intervals the CPU will take to finish all the given tasks.
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1# chunk is defined as each cycle that all different tasks have gone through one time
        idle = chunk * n # maximum number of idle intervals at worst case, after each chunk we have to wait n interval
        #now we need to figure out exact number of idle intervals

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])#reduce the idle intervals equivalent to the freq[i]

        return len(tasks) + idle if idle >= 0 else len(tasks)

tasks = ["A","A","A","B","B","B"]
#tasks=["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 50
n=2
so=Solution()
print(so.leastInterval(tasks,n))

#2025
