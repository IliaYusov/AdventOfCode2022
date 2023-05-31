def crates_to_stacks(crates, num_of_stacks, width_of_stack):
    stk = []
    for layer in crates:
        stk.append([layer[i] for i in range(1, width_of_stack * num_of_stacks, width_of_stack)])
    return [[stk[j][i] for j in range(len(stk) - 2, -1, -1) if stk[j][i] != ' '] for i in range(num_of_stacks)]
        

with open('input.txt') as f:
    crates = []
    for line in f:
        if line.isspace():
            break
        crates.append(line)
    
    stacks = crates_to_stacks(crates, 9, 4)

    for line in f:
        line = line.split()
        num, from_, to = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
        
##        for _ in range(num):
##            stacks[to].append(stacks[from_].pop())
        
        stacks[from_], crane = stacks[from_][:-num], stacks[from_][-num:]
        stacks[to].extend(crane)

print(''.join(i[-1] for i in stacks))
