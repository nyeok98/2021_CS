"""
2021/CAU/CS/DATA STRUCTURE
20172674 신동녘
HW1
Polynomial1
"""


# 다항식 클래스 선언부
class polynomial():
    def __init__(self, coef):
        self.coef = coef
        self.degree = len(coef)

    # 다항식 출력함수
    def print_poly(self):
        for i in range(self.degree):
            if i == self.degree-1:
                print("%d" %(abs(self.coef[i])))
            else:
                if self.coef[i] != 0:
                    print("%d * x^%d" %(abs(self.coef[i]), self.degree-i-1), end='')
                    if self.coef[i+1] >= 0:
                        print(" + ", end='')
                    else:
                        print(" - ", end='')

    # 다항식에 계산 함수
    def calc_poly(self, num):
        result = 0
        for i in range(0, self.degree):
            result += self.coef[i]*pow(num, self.degree-i-1)
        return result

# 두 다항식을 더하는 함수
def poly_add(a, b):
    z = [] # 결과를 담을 다항식 선언
    apos = bpos = 0 # 배열(다항식)을 순차적으로 탐색하기 위한 인덱스
    degree_a = a.degree # 다항식 a의 차수
    degree_b = b.degree # 다항식 b의 차수

    while(degree_a > 0) and (degree_b > 0):
        # a가 차수가 더 높다면
        if degree_a > degree_b:
            z.append(a.coef[apos])
            apos += 1
            degree_a -= 1
        # a와 b가 차수가 같다면
        elif degree_a == degree_b:
            z.append(a.coef[apos] + b.coef[bpos])
            apos += 1
            bpos += 1
            degree_a -= 1
            degree_b -= 1
        # b가 차수가 높다면
        else:
            z.append(b.coef[bpos])
            bpos += 1
            degree_b -= 1
    return polynomial(z)

# 두 다항식을 곱하는 함수
def poly_mult(a, b):
    degree_a = a.degree
    degree_b = b.degree
    # 곱해서 생성되는 다항식은 polymonial class의 정의상 두 차수 합의 -1이다.
    z = [0]*(degree_a+degree_b-1)

    for i in range(degree_a):
        for j in range(degree_b):
            z[i+j] += a.coef[i]*b.coef[j]

    return polynomial(z)

# 수식 1과 2를 입력받는 부분
print("수식 1을 입력하세요: ", end='')
exp1 = list(map(int, input().split()))
a = polynomial(exp1)
print("수식 2를 입력하세요: ", end='')
exp2 = list(map(int, input().split()))
b = polynomial(exp2)

# 수식 1과 2에 대한 연산을 진행하는 부분
c = poly_add(a, b)
d = poly_mult(a, b)
print("수식 1+2 는 ", end='')
c.print_poly()
print("수식 1*2 는 ", end='')
d.print_poly()
print()

# 수식 출력 후 계산 부분
ploy_list = [a, b, c, d] # 다항식을 한 데에 묶어 효과적으로 관리하기 위한 리스트 생성
while (True):
    print("수식에 값을 넣으세요(ex: 1 1) ", end='')
    n, m = map(int, input().split())
    result = 0
    if n >= 1 and n <= 4:
        result = ploy_list[n-1].calc_poly(m)
        print("결과값은 %d" % (result))
    else:
        print("입력이 잘못되었습니다.")


