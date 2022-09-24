with open("C:/Users/cdakk/Desktop/STUDIA/skryptowejezyki/Projekt_SO/Algorytmy zastepowania stron/data_pages.txt") as f:
    pages = [int(x) for x in f.read().split(", ")]


#pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0] 
capacity = 4  # Available space for pages
cache_block = []  
page_faults = 0  # Counter

# Algorithm Least Recently Used, calculating page_faults
for p in pages:
    print("Finding", p, ": ", end="")
    if p not in cache_block:
        print("Miss\t Cache: ", end=" ")
        page_faults += 1
        if len(cache_block) < capacity:
            cache_block.insert(0, p)
        else:
            cache_block.pop()
            cache_block.insert(0, p)
    else:
        cache_block.remove(p)
        cache_block.insert(0, p)
        print ("Hit \t Cache: ", end=" ")

    for q in cache_block:
        print(q, end="\t")
    print("")

print("Number of Page Faults:", page_faults)

