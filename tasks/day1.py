from .utils import get_file

def load_data():
    lines = get_file("inputs/day1.txt")
    list0 = []
    list1 = []
    for line in lines:
        data = line.strip().split('   ')
        print(data)
        list0.append(int(data[0]))
        list1.append(int(data[1]))

    return sorted(list0), sorted(list1)

def compare_lists():
    list0, list1 = load_data()
    print(len(list0), len(list1))
    result = 0
    similarity = 0
    for idx, val in enumerate(list0):
        result += abs(val - list1[idx])
        similarity += val * list1.count(val)
    
    
    return(result, similarity)