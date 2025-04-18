# import requests
# import mysql.connector
# import pandas as pd

# https://leetcode.com/problems/online-election/description/ 

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # instantiate data into data structure
        self.persons = persons
        self.times = times
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # iterate through both arrays checking the times
        # until the time is reached, keep track of votes(dictionary(person: votes))
        votes = {}
        winner = None
        for i in range(len(self.persons)):
            if t > self.times[i]:
                break
            if self.persons[i] in votes:
                votes[self.persons[i]] += 1
            else:
                votes[self.persons[i]] = 1
        winner = max(votes) # helper
        return winner
        
        # Returns the key with the maximum value
        def max(votes):
            
  
  # [(votes = {}, t = 0),
  #  (votes = {0: 1}, t= 2)]
  
  # q(3):
  # votes[3]
  
  
  
  # Time complexity: O(n * q)
  # Space complexity: O(n * q)
  
  
            
 # t = 3           
            
 # Input
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
# Output
# [null, 0, 1, 1, 0, 0, 1]           
                
                
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


# Input
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
# Output
# [null, 0, 1, 1, 0, 0, 1]

# Explanation
# TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
# topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
# topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
# topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# topVotedCandidate.q(15); // return 0
# topVotedCandidate.q(24); // return 0
# topVotedCandidate.q(8); // return 1
