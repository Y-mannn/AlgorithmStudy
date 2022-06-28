sugar = int(input())
# 3KG만 사용해서 만들 수 있는 반복 횟수
for i in range(sugar // 3 + 1):
    m = sugar
    # 입력값에서 3KG만 사용해서 만들 수 있는 반복 횟수를 빼 준다
    m -= 3 * i
    # 뺀 값이 5로 나누어 떨어진다면
    if m % 5 == 0:
        # 뺀 값을 5로 나눈 몫이랑 반복횟수를 더해준다.
        print(i + m // 5)
        break
else:
    print(-1)

# 5로 나누어 떨어지지 않으면 계속해서 3을 빼주고 3을 뺏을 때
# 5로 나누어 떨어지는지 확인하고
# 나누어 떨어지지 않을 때 -1을 출력한다.
