f = open('input.txt', "r")
win = 6
loss = 0
draw = 3
total_score = 0
play_dict = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}
score_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
score_dict_1 = {
    'A': 1,
    'B': 2,
    'C': 3
}
result_dict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
output_dict = {
    'A': {'win': 'B', 'lose': 'C'},
    'B': {'win': 'C', 'lose': 'A'},
    'C': {'win': 'A', 'lose': 'B'}
}
# Part 1
# for line in f.readlines():
#   line = line.replace("\n", "")
#   numbers = line.split(" ")
#   opponent, you = numbers[0], numbers[1]
#   score = score_dict[you]
#   play = play_dict[you]
#   total_score += score
#   if opponent == play:
#     total_score += draw
#   elif (play == 'B' and opponent == 'A') or (play == 'C' and opponent == 'B') or (play == 'A' and opponent == 'C'):
#     total_score += win
#   else:
#     total_score += loss

# Part 2
for line in f.readlines():
  line = line.replace("\n", "")
  numbers = line.split(" ")
  opponent, you = numbers[0], numbers[1]
  score = result_dict[you]
  total_score += score
  if score == 0:
    play = output_dict[opponent]['lose']
    total_score += score_dict_1[play]
  elif score == 3:
    total_score += score_dict_1[opponent]
  else:
    play = output_dict[opponent]['win']
    total_score += score_dict_1[play]

print(total_score)
