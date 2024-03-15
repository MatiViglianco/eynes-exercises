import random

def simple_list():
    list = []
    for i in range(10):
        dicts = {
            "id": i,
            "age": random.randint(1, 100)
        }
        list.append(dicts)
    return list

def sort_list(dicts):
    return sorted(dicts, key=lambda d: d['age'])