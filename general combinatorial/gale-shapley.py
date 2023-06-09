def gale_shapley_algorithm(men_preferences, women_preferences):
    num_men = len(men_preferences)
    num_women = len(women_preferences)

    # Initialize all men and women as free
    free_men = list(range(num_men))
    engaged_women = [-1] * num_women
    proposals = [[0] * num_women for _ in range(num_men)]

    # Main algorithm loop
    while free_men:
        man = free_men[0]
        for woman in men_preferences[man]:
            woman_pref_list = women_preferences[woman]
            current_partner = engaged_women[woman]
            if current_partner == -1:  # Woman is free
                engaged_women[woman] = man
                free_men.pop(0)
                break
            else:
                # Check preferences of the woman
                current_partner_index = woman_pref_list.index(current_partner)
                proposed_man_index = woman_pref_list.index(man)
                if proposed_man_index < current_partner_index:
                    # Engage the new man, add the current partner back to the list of free men
                    engaged_women[woman] = man
                    free_men.append(current_partner)
                    free_men.pop(0)
                    break
        else:
            # No woman accepted the proposal, remove the man from the free list
            free_men.pop(0)

    return engaged_women
