def countSwaps(a):
    # Write your code here
    counter = 0
    for elt in a:
        for index in range(len(a)-1):
            if a[index] > a[index+1]:
                counter += 1
                holder = a[index]
                a[index] = a[index+1]
                a[index+1] = holder

    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
