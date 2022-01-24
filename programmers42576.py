# participant = ["leo","kiki","eden"]
# completion = ["eden","kiki"]

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution():
    if len(participant)-len(completion) == 1:
        for player in completion:
            for i in participant:
                if player == i:
                    participant.remove(player)
        return participant[0]
    else:
        return

print(solution())