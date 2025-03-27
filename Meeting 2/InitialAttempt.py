class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # check if 1 works
        # generate numbers starting from 1 in lexicographic order
        # check if numbers are less than n
        # if yes, add to solution list
        # if no, go back and only add 1
        # recheck if number is less than n
        solution = []
        if 1 < n:
            solution.append(1)
        else:
            return solution
        i = 1
        start = 1
        while i <= n:
            num = i * 10
            if num < n:
                solution.append(num)
            else:
                num = i + 1
                
                if num < n:
                    solution.append(num)
                else:
                    num = num.split()
                    num = num[0]
                    num += 1
                    if num < n:
                        # fix the generation of numbers in lexicographic order
                        # find a place to return the solution
            i = num
            
        
solution = [1, 10, 11, 12, 13]
i = 2
num = 2
