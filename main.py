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
    merged_list = []
    id_set = set()

    for item in list_1:
        if item["id"] not in id_set:
            merged_list.append(item)
            id_set.add(item["id"])
        else:
            for merged_item in merged_list:
                if merged_item["id"] == item["id"]:
                    merged_item.update(item)
                    break
    
    for item in list_2:
        if item["id"] not in id_set:
            merged_list.append(item)
            id_set.add(item["id"])
        else:
            for merged_item in merged_list:
                if merged_item["id"] == item["id"]:
                    merged_item.update(item)
                    break
    
    return merged_list


list_3 = merge_lists(list_1, list_2)
