class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # check if 1 works
        # generate numbers starting from 1 in lexicographic order
        # check if numbers are less than n
        # if yes, add to solution list
        # if no, go back and only add 1
        # recheck if number is less than n
        solution = []
        for i in range(1, 10):
            self.generateNumbers(i, n, solution)
        return solution

    def generateNumbers(self, start: int, n: int, solution: List[int]):
        # pre order traversal
        # visit node first
        if start > n: # check base case
            return 
        solution.append(start)

        # traverse through all the children
        for i in range(10):
            nextnum = start * 10 + i
            if nextnum <= n:
                self.generateNumbers(nextnum, n, solution)
            else:
                break
