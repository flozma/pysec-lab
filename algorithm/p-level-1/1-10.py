def solution(s):
    answer = True
    
    new_list = list(s.lower())
    new_dict = {
        'p': 0,
        'y': 0
    }
    
    for char in new_list:
        if char == 'p':
            new_dict['p'] += 1
        elif char == 'y':
            new_dict['y'] += 1
        else:
            continue
    
    return new_dict['p'] == new_dict['y']


from collections import Counter

def solution2(s):
    lower_char_counter = Counter(list(s.lower()))

    return lower_char_counter['p'] == lower_char_counter['y']



def solution3(s):
  new_list = list(s.lower())
  return new_list.count('p') == new_list.count('y')