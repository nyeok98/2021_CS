"""
2021/CAU/CS/DATA STRUCTURE
20172674 신동녘
HW1
Matrix
"""


# 데이터를 입력받아 2차원 배열로 행렬로 만드는 함수
def normal_matrix(lst, n):
    index = 0
    z = []
    # 정해진 행렬 규격에 맞게 한 행을 각각의 리스트로 만든다.
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(lst[index])
            index += 1
        z.append(temp)

    return z

# 2차원 배열 행렬을 출력하는 함수
def print_normal(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
    print()

# 2차원 배열 행렬 덧셈 함수
def add_normal(a, b, n):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

# 2차원 배열 행렬 곱셈 함수
def multiply_normal(a, b, n):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

print("행렬의 규격을 입력하세요.", end=' ')
n = int(input())
print("행렬 1의 데이터를 입력하세요.", end=' ')
temp1 = list(map(int, input().split()))
mat1 = normal_matrix(temp1, n)
print("행렬 2의 데이터를 입력하세요.", end=' ')
temp2 = list(map(int, input().split()))
mat2 = normal_matrix(temp2, n)


print("\n\n방식1\n")
print("행렬1(%d)" %(n*n))
print_normal(mat1)
print("행렬2(%d)" %(n*n))
print_normal(mat2)

print("행렬 1+2(%d)" %(n*n))
c = add_normal(mat1, mat2, n)
print_normal(c)
print("행렬 1*2(%d)" %(n*n))
d = multiply_normal(mat1, mat2, n)
print_normal(d)
print("******")

# 2차원 배열 행렬을 희소행렬로 바꾸는 함수
def sparse_matrix(matrix, n):
    z = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                z.append([i, j, matrix[i][j]])
    return z

# 희소행렬을 출력하는 함수
def print_sparse(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    print()

# 서로 다른 두 희소행렬을 더하는 함수
def add_sparse(a, b):
    z = []
    apos = bpos = 0 # a,b 행렬 각각 현재 처리되고 있는 위치를 가리키는 변수

    while (apos < len(a)) and (bpos < len(b)):
        # 겹치지 않은 부분은 차례대로 옮겨주고
        if a[apos][0] < b[bpos][0]:
            z.append([a[apos][0], a[apos][1], a[apos][2]])
            apos += 1
        elif a[apos][0] == b[bpos][0]:
            if a[apos][1] < b[bpos][1]:
                z.append([a[apos][0], a[apos][1], a[apos][2]])
                apos += 1
            elif a[apos][1] == b[bpos][1]: # 완벽하게 행렬의 위치가 같은 경우 더한 값을 z에 추가해준다.
                z.append([a[apos][0], a[apos][1], a[apos][2] + b[bpos][2]])
                apos += 1
                bpos += 1
            else:
                z.append([b[bpos][0], b[bpos][1], b[bpos][2]])
                bpos += 1
        else:
            z.append([b[bpos][0], b[bpos][1], b[bpos][2]])
            bpos += 1

    # 상대적으로 행렬이 다른 행렬에 비해 길어 처리되지 못한 나머지 부분을 처리하는 부분
    while apos < len(a):
        z.append([a[apos][0], a[apos][1], a[apos][2]])
        apos += 1
    while bpos < len(b):
        z.append([b[bpos][0], b[bpos][1], b[bpos][2]])
        bpos += 1

    return z

# 서로 다른 두 희소행렬을 곱하는 함수
def multiply_sparse(a, b):
    z = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][1] == b[j][0]: # 위치가 같아야만 곱셈이 가능
                isAppended = False
                for k in range(len(z)):
                    if z[k][0] == a[i][0] and z[k][1] == b[j][1]: # 해당 인덱스가 존재하야 존재하는 인덱스에 곱셈 결과 누적
                        z[k][2] += a[i][2]*b[j][2]
                        isAppended = True
                if not isAppended:
                    z.append([a[i][0], b[j][1], a[i][2]*b[j][2]]) # 해당 인덱스가 존재하지 않아 새로 추가
    return z

print("\n\n방식2\n")

mat3 = sparse_matrix(mat1, n)
print("행렬3(%d)" %(3*len(mat3)))
print_sparse(mat3)
mat4 = sparse_matrix(mat2, n)
print("행렬4(%d)" %(3*len(mat3)))
print_sparse(mat4)

e = add_sparse(mat3, mat4)
print("행렬 3+4(%d)" %(3*len(e)))
print_sparse(e)
f = multiply_sparse(mat3, mat4)
print("행렬 3*4(%d)" %(3*len(f)))
print_sparse(f)
print("******")


"""
input_ex
3
1 0 3 0 0 0 2 0 0
2 0 1 0 2 0 0 1 0
"""