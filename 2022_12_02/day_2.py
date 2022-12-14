import pandas as pd 


play_df = pd.DataFrame({

    'opp': ['A','B','C'],
    'you': ['X','Y','Z'],
    'value': [1, 2, 3]
})

win_df = pd.DataFrame({
    'opp': ['C','B','A','A','B','C','B','C','A'],
    'you': ['X','X','X','Y','Y','Y','Z','Z','Z'],
    'value': [6, 0, 3, 6, 3, 0, 6, 3, 0]
})

total_score = 0

file = open('input.txt', 'r') # read lines
lines = file.readlines()
for line in lines:
    opp_play = line.split(' ')[0]
    your_play = line.split(' ')[1][:-1]
    win_score = win_df.loc[(win_df['opp'] == opp_play) & (win_df['you'] == your_play)].reset_index().at[0, 'value']
    play_score = play_df.loc[play_df['you'] == your_play].reset_index().at[0, 'value']
    total_score += play_score
    total_score += win_score

print('Original Total Score: ' + str(total_score))

# A = rock
# B = paper
# C = scissors

strategy_df = pd.DataFrame({
    'opp': ['C','B','A','A','B','C','B','C','A'],
    'outcome': ['X','X','X','Y','Y','Y','Z','Z','Z'],
    'you': ['B','A','C','A','B','C','C','A','B']
})

win_df_2 = pd.DataFrame({
    'outcome': ['X','Y','Z'],
    'score': [0,3,6]
})

play_df_2 = pd.DataFrame({
    'you': ['A','B','C'],
    'value': [1, 2, 3]
})

new_total_score = 0 

for line in lines:
    opp_play = line.split(' ')[0]
    strategy = line.split(' ')[1][:-1]
    your_play = strategy_df.loc[(strategy_df['opp'] == opp_play) & (strategy_df['outcome'] == strategy)].reset_index().at[0, 'you']
    win_score_2 = win_df_2.loc[(win_df_2['outcome'] == strategy)].reset_index().at[0, 'score']
    play_score_2 = play_df_2.loc[play_df_2['you'] == your_play].reset_index().at[0, 'value']
    new_total_score += play_score_2
    new_total_score += win_score_2

print('New Total Score: ' + str(new_total_score))