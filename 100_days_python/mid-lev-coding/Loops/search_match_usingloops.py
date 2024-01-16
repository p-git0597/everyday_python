def search_match(list1, target_value):
    for element in list1:
        if element == target_value:
            print(f"we have found the match {target_value}")
            break
    else:
        print(f"{target_value} is not present")


list1 = [1, 2, 4, 6, 7, 13, 45, 34, 29]
target_value = 7

search_match(list1, target_value)
