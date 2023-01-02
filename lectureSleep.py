
def lecture(size, duration, lectures, sleep):
    window = []
    total = 0
    vals = 0
    maximum = 0
    for index in range(size):
        if sleep[index] == 0:
            total += lectures[index]
            window.append(lectures[index])
        else:
            vals += lectures[index]
            window.append(0)
        if len(window) > duration:
            total -= window.pop(0)
        maximum = max(maximum, total) 
    print(vals+maximum)
    
size = list(map(int, input().split(" ")))
lectures = list(map(int, input().split(" ")))
sleep = list(map(int, input().split(" ")))
lecture(size[0], size[1], lectures, sleep)
