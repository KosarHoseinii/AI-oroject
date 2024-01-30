#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq



def h(state, goal):
    # تابع هیوریستیک: تعداد عناصری که در جای صحیح نیستند
    return sum([1 for i, j in zip(state, goal) if i != j])

def a_star(start, goal):
    open_set = [(h(start, goal), start)]
    closed_set = set()
    
    
    # انتخاب حالت با کمترین مقدار h
    while open_set:
        _, current_state = heapq.heappop(open_set)
        
        if current_state == goal:
            return current_state
        
        closed_set.add(current_state)
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_set:
                heapq.heappush(open_set, (h(neighbor, goal), neighbor))
    
    return None


def get_neighbors(state):
    # تابعی که حالتهای مجاور را تولید میکند (با جا به جایی دو عنصر)
    blank_index = state.index(0)
    neighbors = []
    
    if blank_index // 3 > 0:
        neighbors.append(swap(state, blank_index, blank_index - 3))
    if blank_index // 3 < 2:
        neighbors.append(swap(state, blank_index, blank_index + 3))
    if blank_index % 3 > 0:
        neighbors.append(swap(state, blank_index, blank_index - 1))
    if blank_index % 3 < 2:
        neighbors.append(swap(state, blank_index, blank_index + 1))
    
    return neighbors

def swap(state, i, j):
    # تابع جا به جایی دو عنصر در حالت
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_user_input():
    print("Please enter initial state:")
    
    while True:
        user_input_str = input()
        user_input_list = user_input_str.split()
        
        if len(user_input_list) == 9 and all(num.isdigit() for num in user_input_list):
            user_input = tuple(map(int, user_input_list))
            if all(0 <= num <= 8 for num in user_input):
                return user_input
            else:
                print("invalied entry! Please retry.")
                
        elif user_input_str == 'exit':
            break
        
        else:
            print("invalid entry! Please retry.")

#receive initial state from user
custom_start_state = get_user_input()

# using A* algorithm by using new initial state
result = a_star(custom_start_state, goal_state)
print("Final state:", result)

