list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    list_1.sort(key=lambda x: x["id"])
    list_2.sort(key=lambda x: x["id"])
    
    merged_list = []
    i = j = 0
    
    while i < len(list_1) and j < len(list_2):
        if list_1[i]["id"] == list_2[j]["id"]:
            merged_item = list_1[i].copy()
            merged_item.update(list_2[j])
            merged_list.append(merged_item)
            i += 1
            j += 1
        elif list_1[i]["id"] < list_2[j]["id"]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1
    
    merged_list.extend(list_1[i:])
    merged_list.extend(list_2[j:])
    
    return merged_list



list_3 = merge_lists(list_1, list_2)
