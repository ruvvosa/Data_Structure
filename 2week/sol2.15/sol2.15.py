from random import randrange

answer = randrange(100)
min = 0
max = 99

for i in range(10):
    guess = int(input("수를 입력하세요(범위:%d ~ %d): " % (min, max)))
    if answer == guess:
        print("정답입니다!", i + 1, "번만에 맞추셨습니다.")
        break
    elif guess < answer:
        min = guess
        print("더 큰 숫자입니다.")
    else:
        max = guess
        print("더 작은 숫자입니다.")

print("게임이 종료됩니다.")
