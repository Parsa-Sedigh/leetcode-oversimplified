If we're gonna do backtracking, there are 2 rules we have to follow:
1. n open parentheses, n closing ones
2. This condition tells us when we're allowed to add a closing parentheses: We can only add a closing parentheses 
if the number of closing parentheses so far, is less(not even equal) than number of the open parentheses. So only if this is true, we're allowed to
add a closing parentheses(see a closing parentheses). Note: We can add or see as many open parentheses as we want as long as it's
under the limit of total(n).