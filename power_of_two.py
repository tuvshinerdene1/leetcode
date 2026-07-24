# def isPowerOfTwo(n:int) -> bool:
#     current = n
#     while current > 0:
#         if current == 1:
#             return True
#         if current % 2 == 1:
#             return False
#         current = current / 2
#     return True
def isPowerOfTwo(n:int) -> bool:
    if n<=0:
        return False
    while n % 2 == 0:
        n //=2

    return n == 1

def main():
    print(isPowerOfTwo(32))
    print(isPowerOfTwo(1))
    print(isPowerOfTwo(3))

if __name__ == "__main__":
    main()