competition = [['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']]
results = [0, 0, 1]


# Time O(N) | Space O(N + 1) --> O(N)  | Intutive Approach|

def tournmentWinner(competition, results):
  scores = {}
  # first find the winner teams from current teams
  for idx, currentCompetitors in enumerate(competition):
    loserTeam = results[idx]
    if loserTeam == 1:
      currentWinnerTeam = currentCompetitors[0]
    else:
      currentWinnerTeam = currentCompetitors[1]
  # then store them in hashtable and give points
    if currentWinnerTeam not in scores:
      scores[currentWinnerTeam] = 1
    else:
      scores[currentWinnerTeam] += 1
  # find the best team from dictionary
    finalWinner = ""
    temp = 0
    for score in scores:
      if scores[score] > temp:
        finalWinner = score
        temp = scores[score]

  print(finalWinner, temp)

# tournmentWinner(competition, results)


# Time O(N) | Space O(N + 1) --> O(N)  | Bit Optimized |

def tournmentWinner(competition, results):
  overallBest = ""
  scores = {overallBest: 0}
  for idx, currentCompetitors in enumerate(competition):
    loserTeam = results[idx]
    if loserTeam == 1:
      currentWinnerTeam = currentCompetitors[0]
    else:
      currentWinnerTeam = currentCompetitors[1]

    if currentWinnerTeam not in scores:
      scores[currentWinnerTeam] = 1
    else:
      scores[currentWinnerTeam] += 1

    if scores[currentWinnerTeam] > scores[overallBest]:
      overallBest = currentWinnerTeam
      scores[overallBest] = scores[currentWinnerTeam]

  return overallBest

print(tournmentWinner(competition, results))