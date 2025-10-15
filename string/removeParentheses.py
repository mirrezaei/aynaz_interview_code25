#Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

#Note: The input string may contain letters other than the parentheses ( and ).


#points: BFS, huristic to remove strings that are wrong for further processing , no stack, counter is enogh
#idea: we start by removing one paranthesis at a time
# if the string has len of m, we first remove one char from that and check its validity, if it is valid we add it to the output and if not we try to remove another char
#at each step that we remove one char, we check if its open paranthesis is greater than close paranthesis or not, if it is not we don't continue trying that string anymore
#at each step that we remove one char, we also keep track of reducted string and number of open and close paranthesis

import sys
import collections
from collections import deque
class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(expr):
            count = 0
            for ch in expr:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        visited = set()
        queue = deque([s])# af first queue only has one element, which is the entire string
        found = False
        result = []

        while queue:
            level_size = len(queue)# nu of elems in the queue defines how many string in that level we need to validate
            level_seen = set()
            for _ in range(level_size):
                expr = queue.popleft()
                if expr in visited:
                    continue
                visited.add(expr)

                if is_valid(expr):
                    result.append(expr)
                    found = True

                if not found:
                    for i in range(len(expr)):# remove each char of the string and add it to the queue and
                        if expr[i] not in ('(', ')'):
                            continue
                        new_expr = expr[:i] + expr[i + 1:]
                        if new_expr not in visited and new_expr not in level_seen:
                            queue.append(new_expr)
                            level_seen.add(new_expr)

            if found:
                break

        return result

so=Solution()
ss=")((())((())(((f)()("
so.removeInvalidParentheses(ss)


