# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    s = sorted([a, b, c])
    print(s[0] * s[0] + s[1] * s[1] == s[2] * s[2])
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()