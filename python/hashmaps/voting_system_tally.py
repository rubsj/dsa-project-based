"""
You are given a list of strings votes representing candidate names. 
Return the name of the candidate with the most votes. If there is a tie, return the one that appears first in the list.

"""

def voting_system_tally(votes):
    vote_map = {}
    first_seen = {}
    most_votes = 0
    most_voted = None
    for i, vote in enumerate(votes):
        if vote not in vote_map:
            vote_map[vote] = 0
            first_seen[vote] = i
        vote_map[vote] += 1
        count = vote_map[vote] 

        if count > most_votes or (count == most_votes and first_seen[vote] < first_seen[most_voted]):
            most_votes = count
            most_voted = vote
        
    return most_voted

votes = ["alice", "bob", "alice", "eve", "bob", "alice"]
# Output: "alice"

result = voting_system_tally(votes)
print(result)

votes = ["alice", "bob", "bob", "alice"]
# output alice
result = voting_system_tally(votes)
print(result)