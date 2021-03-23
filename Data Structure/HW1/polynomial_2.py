# 다항식 클래스 선언부
class polynomial():
    def __init__(self, coef):
        self.coef_deg = coef
        self.degree = len(coef)

    # 다항식 출력함수
    def print_poly(self):
        for i in range(self.degree):
            print(self.coef_deg[i][0], self.coef_deg[i][1],end=' ')
        print()

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

def poly_mult(a,b):
    z = []

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

