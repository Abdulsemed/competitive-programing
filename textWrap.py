import textwrap

def wrap(string, max_width):
    right = max_width
    left = 0
    sizeOfString = len(string)
    wraps = ""
    while right <= sizeOfString:
        wraps += string[left:right] +"\n"
        if right +max_width > sizeOfString:
            wraps += string[right:]
        left += max_width
        right += max_width
    return wraps

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
