def bin_search(lst, element):
    start = 0
    middle = 0
    steps = 0
    end = len(lst) -1
    while(start <= end):
        print("Step", steps , ": ", lst)
        steps = steps + 1
        middle = (start + end) // 2
        
        if  element == lst[middle]:
            return middle
        if  element < lst[middle]:
            end = middle -1
        else:
            start = middle +1
    return -1

collection = input("Provide elements separated by commas:")
lst = [int(i) for i in collection.split(",")]
element = int(input("Which number do you want to find: ")) 
result = bin_search(lst, element)
print(result)
