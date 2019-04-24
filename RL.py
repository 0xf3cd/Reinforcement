import numpy as np
import random
import time
import cmath
import csv

EPOCHS = 10000
TIMES = 20

EPSILON = 0.7
ALPHA = 0.1
GAMMA = 0.6

ROW_N = 6
COL_N = 10
POINT_N = ROW_N * COL_N
STATES_N = POINT_N * POINT_N
ACTIONS_N = 8

# DESK 2 * 1
# BED 2 * 3

Q = np.zeros([STATES_N, ACTIONS_N], dtype = np.float32)

def pos2RC(state_num):
    c = int(state_num % COL_N)
    r = int((state_num - c) / COL_N)
    return r, c

def RC2Pos(r, c):
    return r * COL_N + c


def pos2State(dpos, bpos):
    return POINT_N * dpos + bpos

def state2Pos(state):
    bpos = state % 60
    dpos = int((state - bpos) / 60)
    return dpos, bpos

def getValidAction(state):
    va = []
    dp, bp = state2Pos(state)
    dr, dc = pos2RC(dp)
    br, bc = pos2RC(bp)
    dr_ = dr + 2
    dc_ = dc + 1
    br_ = br + 3
    bc_ = bc + 2
    
    if dr >= 1:
        if not(dr == br_ and dc >= bc and dc <= bc+2):
            va.append(1)
    
    if dr <= 2:
        if not(dr_ == br and dc >= bc and dc <= bc+2):
            va.append(2)
    
    if dc >= 1:
        if not(dc == bc_ and dr >= br-1 and dr <= br+1):
            va.append(3)

    if dc <= 7:
        if not(dc_ == bc and dr >= br-1 and dr <= br+1):
            va.append(4)

    if br >= 1:
        if not(br == dr_ and dc >= bc and dc <= bc+2):
            va.append(5)
    
    if br <= 2:
        if not(br_ == dr and dc >= bc and dc <= bc+2):
            va.append(6)

    if bc >= 1:
        if not(bc == dc_ and dr >= br-1 and dr <= br+1):
            va.append(7)
    
    if bc <= 5:
        if not(bc_ == dc and dr >= br-1 and dr <= br+1):
            va.append(8)

    return va

def reward(state):
    dp, bp = state2Pos(state)
    dr, dc = pos2RC(dp)
    br, bc = pos2RC(bp)
    br_ = br + 3
    bc_ = bc + 2
    dr_ = dr + 2
    dc_ = dc + 1

    # desk_win1_dis = 5 / (cmath.sqrt(dr ** 2 + dc ** 2).real + 0.02)
    # desk_win2_dis =  20 / (cmath.sqrt(dr ** 2 + (dc-8) ** 2).real + 0.02)
    desk_win2_dis = 200 - 100 * (cmath.sqrt(dr ** 2 + (dc-8) ** 2).real + 0.02)
    # desk_door_dis = cmath.sqrt((dr-5) ** 2 + dc ** 2)
    # bed_door_dis = cmath.sqrt((br-5) ** 2 + bc ** 2)
    # bed_corner_dis = (cmath.sqrt(br ** 2 + (bc_-9) ** 2) + cmath.sqrt((br_-5) ** 2 + (bc_-9) ** 2)) / 2
    bed_corner_dis =  200 - 100 * (cmath.sqrt((br_-5) ** 2 + (bc_-9) ** 2).real + 0.02)

    value = 0
    # value += 5 * desk_win1_dis
    # value += 10 * desk_win2_dis
    # value += 20 * bed_corner_dis
    # value -= 20 * desk_door_dis
    # value -= 20 * bed_door_dis
    value = desk_win2_dis + bed_corner_dis
    return value

def getAction(now_state):
    va = getValidAction(now_state)

    if(np.random.uniform() > EPSILON): #取最大值
        a = -1
        a_val = -100000
        for each in va:
            if(Q[now_state, each-1] > a_val):
                a_val = Q[now_state, each-1]
                a = each
    else:
        a = va[random.randint(0, len(va)-1)]
    # a 是此时应当采取的动作
    return a

def getActionWithoutRandom(now_state):
    va = getValidAction(now_state)
    a = -1
    a_val = -100000
    for each in va:
        if(Q[now_state, each-1] > a_val):
            a_val = Q[now_state, each-1]
            a = each
    # a 是此时应当采取的动作
    return a

def calcNextState(now_state, action):
    dp, bp = state2Pos(now_state)
    dr, dc = pos2RC(dp)
    br, bc = pos2RC(bp)

    if action == 1:
        dr -= 1
    elif action == 2:
        dr += 1
    elif action == 3:
        dc -= 1
    elif action == 4:
        dc += 1
    elif action == 5:
        br -= 1
    elif action == 6:
        br += 1
    elif action == 7:
        bc -= 1
    else: # elif action == 8:
        bc += 1
    
    dp = RC2Pos(dr, dc)
    bp = RC2Pos(br, bc)
    return pos2State(dp, bp)

def moveOneStep(now_state):
    a = getAction(now_state)
    next_state = calcNextState(now_state, a)

    nva = getValidAction(next_state)
    max_val = -100000
    for na in nva:
        if(Q[next_state, na-1] > max_val):
            max_val = Q[next_state, na-1]

    new_val = 0
    new_val += (1 - ALPHA) * Q[now_state, a-1]
    new_val += ALPHA * (reward(next_state) + GAMMA * max_val)
    Q[now_state, a-1] = new_val

    return next_state

def train(times=EPOCHS):
    for i in range(1, times+1):
        ini_d_pos = RC2Pos(1, 5)
        ini_b_pos = RC2Pos(3, 2)
        now_state = pos2State(ini_d_pos, ini_b_pos)
        for j in range(0, TIMES):
            next_state = moveOneStep(now_state)
            now_state = next_state
        pr, test_state = test()
        print('epoch: %d, reward: %f' % (i, reward(test_state)))

def test(times=TIMES):
    ini_d_pos = RC2Pos(1, 5)
    ini_b_pos = RC2Pos(3, 2)
    now_state = pos2State(ini_d_pos, ini_b_pos)
    process = []
    for i in range(1, times+1):
        a = getActionWithoutRandom(now_state)
        next_state = moveOneStep(now_state)
        now_state = next_state
        x = 'step %d, reward %f' % (i, reward(now_state))
        process.append(x)
    # print(now_state)

    # dp, bp = state2Pos(now_state)
    # print(pos2RC(dp))
    # print(pos2RC(bp))
    # print(reward(now_state))
    return process, now_state

def getCSV(times=TIMES):
    datab = []
    datad = []
    ini_d_pos = RC2Pos(0, 0)
    ini_b_pos = RC2Pos(0, 1)
    now_state = pos2State(ini_d_pos, ini_b_pos)

    dp, bp = state2Pos(now_state)
    dr, dc = pos2RC(dp)
    br, bc = pos2RC(bp)
    datad.append((dr, dc))
    datab.append((br, bc))
    for i in range(0, times):
        a = getActionWithoutRandom(now_state)
        next_state = moveOneStep(now_state)
        now_state = next_state

        dp, bp = state2Pos(now_state)
        dr, dc = pos2RC(dp)
        br, bc = pos2RC(bp)
        datad.append((dr, dc))
        datab.append((br, bc))
        
    return datad, datab, now_state

# print(state2Pos(3599))
# print(pos2State(0, 33))
train(EPOCHS)
# np.set_printoptions(threshold=np.inf)
# print(Q)
print()
print('finished')
max_s = 0
max_r = -10000
datad = []
datab = []
prcs = []
for i in range(0, 10):
    # dd, db, temp = getCSV(TIMES) 
    prcs_, temp = test(TIMES)
    temp_r = reward(temp)
    if(temp_r > max_r):
        max_r = temp_r
        max_s = temp
        prcs = prcs_
        # datad = dd
        # datab = db

dp, bp = state2Pos(max_s)
print(pos2RC(dp))
print(pos2RC(bp))
print(reward(max_s))

print()
# print(prcs)
for each in prcs:
    print(each)

# csvfiled = open('d.csv', 'w')
# csvfileb = open('b.csv', 'w')
# writerd = csv.writer(csvfiled)
# writerb = csv.writer(csvfileb)
# # datad, datab = getCSV(TIMES)
# writerd.writerows(datad)
# writerb.writerows(datab)
# csvfiled.close()
# csvfileb.close()