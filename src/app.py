import sys
import os


def prime(s):
    a = int(s)
    if a >= 1:  
        for n in range(2,a):  
            if (a % n) == 0:  
                return False
        return True
    else:
        return False

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
