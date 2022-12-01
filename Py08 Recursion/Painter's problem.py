def permuta(alist, step=0):
    if len(alist) == 1:
        return [alist]
    if len(alist) == 2 and step % 2 == 1:
        return [[alist[1], alist[0]], [alist[0], alist[1]]]
    if len(alist) == 2:
        return [[alist[0], alist[1]], [alist[1], alist[0]]]
    result_list = []
    step += 1
    for element_position, element in enumerate(alist):
        if element_position == len(alist) - 1:
            sub_permutations = permuta(alist[:element_position] + alist[element_position + 1:], step)
        else:
            sub_permutations = permuta(alist[:element_position] + alist[element_position + 1:])
        for i in range(len(sub_permutations)):
            result_list =  result_list + [[element] + list(sub_permutations)[i]]
    return result_list



        if element_position == len(alist) - 1:
            sub_permutations = permuta(alist[:element_position] + alist[element_position + 1:], step)
        else:
            sub_permutations = permuta(alist[:element_position] + alist[element_position + 1:])


def permuta(alist, step=0):
    if step == 0:
        step -= 1
    if len(alist) == 1:
        return [alist]
    if len(alist) == 2:
        return [[alist[0], alist[1]], [alist[1], alist[0]]]
    result_list = []
    step += 1
    for element_position, element in enumerate(alist):
        if element_position == len(alist) - 1:
            sub_permutations = permuta((alist[:element_position] + alist[element_position + 1:]).reverse())
        else:
            sub_permutations = permuta(alist[:element_position] + alist[element_position + 1:])
        for i in range(len(sub_permutations)):
            result_list =  result_list + [[element] + list(sub_permutations)[i]]
    return result_list


print(permuta(['A', 'B', 'C']))