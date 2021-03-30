"""
2021/CAU/CS/DATA STRUCTURE
20172674 신동녘
HW1
Polynomial2
"""


# 다항식 클래스 선언부
class polynomial():
    def __init__(self, coef):
        self.coef_deg = coef
        self.degree = len(coef)

    # 다항식 출력함수
    def print_poly(self):
        for i in range(self.degree):
            if i == self.degree - 1:
                print("%d" % (abs(self.coef_deg[i][0])))
            else:
                if self.coef_deg[i][0] != 0:
                    print("%d * x^%d" % (abs(self.coef_deg[i][0]), self.coef_deg[i][1]), end='')
                    if self.coef_deg[i+1][0] >= 0:
                        print(" + ", end='')
                    else:
                        print(" - ", end='')

    # 다항식에 계산 함수
    def calc_poly(self, num):
        result = 0
        for i in range(0, self.degree):
            result += self.coef_deg[i][0] * pow(num, self.coef_deg[i][1])
        return result


# 두 다항식을 더하는 함수
def poly_add(a, b):
    z = [] # 결과를 담을 다항식 선언
    apos = bpos = 0 # 배열(다항식)을 순차적으로 탐색하기 위한 인덱스
    degree_a = a.degree # 다항식 a의 차수
    degree_b = b.degree # 다항식 b의 차수

    while(apos < degree_a) and (bpos < degree_b):
        # a가 차수가 더 높다면
        if a.coef_deg[apos][1] > b.coef_deg[bpos][1]:
            z.append([a.coef_deg[apos][0], a.coef_deg[apos][1]])
            apos += 1
        # a와 b가 차수가 같다면
        elif a.coef_deg[apos][1] == b.coef_deg[bpos][1]:
            z.append([a.coef_deg[apos][0] + b.coef_deg[bpos][0], a.coef_deg[apos][1]])
            apos += 1
            bpos += 1
        # b가 차수가 높다면
        else:
            z.append([b.coef_deg[bpos][0], b.coef_deg[bpos][1]])
            bpos += 1
    return polynomial(z)

def poly_mult(a, b):
    z = []  # 곱셈 결과를 담을 리스트 z
    z_list = []  # z가 가지고 있는 차수를 담을 리스트
    degree_a = a.degree # a의 차수
    degree_b = b.degree # b의 차수

    for i in range(degree_a):
        for j in range(degree_b):
            # 임시로 곱셈 결과를 해당 다항식의 방식대로 저장
            temp = [a.coef_deg[i][0]*b.coef_deg[j][0], a.coef_deg[i][1]+b.coef_deg[j][1]]
            if temp[1] in z_list: # 같은 차수가 이미 있다면
                for k in range(len(z)):
                    # 해당 차수의 계수를 증가시켜준다.
                    if z[k][1] == temp[1]:
                        z[k][0] += temp[0]
            else: # 같은 차수가 없다면
                z.append(temp) # 임시 다항식을 z에 추가해주고
                z_list.append(temp[1]) # 해당 차수가 있음을 리스트에 추가하여 표기한다.

    return polynomial(z)


# 수식 1과 2를 입력받는 부분
print("수식 1을 입력하세요: ", end='')
exp1 = list(map(int, input().split()))
temp1 = []
for i in range(len(exp1)//2):
    temp1.append([exp1[i*2],exp1[i*2+1]])
a = polynomial(temp1)

print("수식 2를 입력하세요: ", end='')
exp2 = list(map(int, input().split()))
temp2 = []
for i in range(len(exp2)//2):
    temp2.append([exp2[i*2],exp2[i*2+1]])
b = polynomial(temp2)

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