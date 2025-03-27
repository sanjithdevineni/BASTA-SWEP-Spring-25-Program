class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # check if 1 works
        # generate numbers starting from 1 in lexicographic order
        # check if numbers are less than n
        # if yes, add to solution list
        # if no, go back and only add 1
        # recheck if number is less than n
        solution = []
        curr = 1
        for i in range(n):
            solution.append(curr)
            if curr * 10 <= n: # if multiplying curr by 10 is <= n, multiply by 10
                curr *= 10
            else:
                while curr >= n or str(curr)[-1] == '9': # while curr ends with a 9 or is >= n
                    curr //= 10 # divide by 10, get rid of last digit
                curr += 1
        return solution
