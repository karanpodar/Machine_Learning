def tournamentWinner(competitions, results):
    # Write your code here.
    win_tab = {'N' : 0}
    win_team = 'N'
    for i in range(len(competitions)):
        if results[i] == 0:
            if competitions[i][1] in win_tab:
                win_tab[competitions[i][1]] += 3
                if win_tab[win_team] < win_tab[competitions[i][1]]:
                    win_team = competitions[i][1]
            else:
                win_tab[competitions[i][1]] = 3
                if win_tab[win_team] < win_tab[competitions[i][1]]:
                    win_team = competitions[i][1]
        else:
            if competitions[i][0] in win_tab:
                win_tab[competitions[i][0]] += 3
                if win_tab[win_team] < win_tab[competitions[i][0]]:
                    win_team = competitions[i][0]
            else:
                win_tab[competitions[i][0]] = 3
                if win_tab[win_team] < win_tab[competitions[i][0]]:
                    win_team = competitions[i][0]
        
    return win_team
