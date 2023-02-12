def row_weights(array):
    team_1, team_2 = 0, 0
    for i in range(len(array)):
        if i % 2 == 1:
            team_2 += array[i]
        else: 
            team_1 += array[i]
    return (team_1, team_2)
