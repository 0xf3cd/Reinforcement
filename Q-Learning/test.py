'''
房间问题
'''

import numpy as np
import random
import time

STATES = 6
EPSILON = 0.9
ALPHA = 0.1
GAMMA = 0.6

R = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100],
])

Q = np.zeros([STATES, STATES], dtype = np.float32)

# for step in range(0, 100000):
#     state = random.randint(0, 5) # get random state
#     # if state == 5:
#     #     continue  
    
#     ac_state = []
#     for i in range(0, 6):
#         if(R[state, i] != -1):
#             ac_state.append(i)
    
#     next_state = ac_state[random.randint(0, len(ac_state) - 1)]
#     Q[state, next_state] = R[state, next_state] + GAMMA * np.max(Q[next_state])

# print(Q)

def get_valid_action(state):
    ac_state = []
    for i in range(0, STATES):
        if(R[state, i] != -1):
            ac_state.append(i)   
    return ac_state

def get_next_action(now_state):
    if(now_state == STATES - 1):
        # 如果已经到达终态，则直接退出
        return now_state
    valid_action = get_valid_action(now_state)

    if(np.random.uniform() > EPSILON): #取最大值
        next_state = -1
        next_state_val = -100000
        for ns in valid_action:
            if(Q[now_state, ns] > next_state_val):
                next_state_val = Q[now_state, ns]
                next_state = ns
    else:
        next_state = valid_action[random.randint(0, len(valid_action)-1)]
    
    return next_state

def update_Q(now_state, next_state):
    if(now_state == STATES - 1):
        return
    
    next_valid_action = get_valid_action(next_state)
    max_val_state = -1
    max_val = -100000
    for ns in next_valid_action:
        if(Q[next_state, ns] > max_val):
            max_val = Q[next_state, ns]
            max_val_state = ns

    new_val = 0
    new_val += (1 - ALPHA) * Q[now_state, next_state]
    new_val += ALPHA * (R[now_state, next_state] + GAMMA * max_val)
    Q[now_state, next_state] = new_val
    # if(next_state != STATES - 1):
    #     print(max_val)

def train():
    for times in range(0, 100):
        now_state = random.randint(0, STATES - 1)
        while True:
            if(now_state == STATES - 1):
                # print('\n\n')
                break
            else:
                next_state = get_next_action(now_state)
                # print(now_state, next_state)
                update_Q(now_state, next_state)
                now_state = next_state
                
    print(Q)

def play():
    now_state = int(input())
    while True:
        if(now_state == STATES - 1):
            print('Move to terminal!\n')
            break
        else:
            valid_state = get_valid_action(now_state)
            next_state = -1
            max_val = -10000
            for ns in valid_state:
                if(Q[now_state][ns] > max_val):
                    max_val = Q[now_state][ns]
                    next_state = ns
            now_state = next_state
            print('Move to %d' % (next_state))

train()
play()