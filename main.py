import itertools

sides_per_dice = 6 

data = []
for num_attack in [3,2,1]:  # the number of attack dice
    for num_defence in [2,1]:   # the number of defence dice
        outcomes_attack = list(itertools.product([1,2,3,4,5,6], repeat=num_attack)) # Make all state and possibilities for attack
        outcomes_defence = list(itertools.product([1,2,3,4,5,6], repeat=num_defence))   # Make all state and possibilities for defence
        total_possible_outcomes = sides_per_dice ** (num_attack + num_defence)
        
        outcomes = {}
        # Simulate rolling the dice and count the occurrences of each outcome
        state = {
            "Attack dice": num_attack,
            "Defence dice": num_defence,
            "Data": []
        }
        for attack in outcomes_attack:
            for defence in outcomes_defence:
                attack = list(attack)
                attack.sort(reverse=True)
                defence = list(defence)
                defence.sort(reverse=True)

                attack_damage = 0
                defence_damage = 0

                for i in [0, 1]:
                    try:
                        if attack[i] > defence[i]:
                            defence_damage -= 1
                        else: 
                            attack_damage -= 1
                    except:
                        pass

                key = (attack_damage, defence_damage)
                if key in outcomes:
                    outcomes[key] += 1
                else:
                    outcomes[key] = 1

        for outcome, count in outcomes.items():
            probability = count / total_possible_outcomes
            state['Data'].append(f" |    {outcome[0]:<5} |    {outcome[1]:<5} |   {probability:.4f}")
        data.append(state)
for a in data:
    print('---------------------------')
    print(f"Attack dice: {a['Attack dice']}")
    print(f"Defence dice: {a['Defence dice']}")
    print(f"States:")
    print("         | Attacker | defencer | Probability")
    print(' damage ' + '\n damage '.join(a['Data']))
    print('---------------------------')