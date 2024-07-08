import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
video = [[int(item) for item in input().strip()] for _ in range(N)]


def check(vertex):
    flag=video[vertex[0]][vertex[2]]
    is_same= True
    for row in range(vertex[0], vertex[1]):
        for col in range(vertex[2], vertex[3]):
            is_same &= (flag == video[row][col])
            if not is_same:
                return is_same
    return is_same

def split(vertex):
    r_s, r_e = vertex[0], vertex[1]
    c_s, c_e = vertex[2], vertex[3]
    
    tmp_n = (r_e-r_s) //2
    
    return [
        (r_s, r_s+tmp_n, c_s, c_s+tmp_n),
        (r_s, r_s+tmp_n, c_s+tmp_n, c_s+tmp_n*2),
        (r_s+tmp_n, r_s+tmp_n*2, c_s, c_s+tmp_n),
        (r_s+tmp_n, r_s+tmp_n*2, c_s+tmp_n, c_s+tmp_n*2),
    ]
    
def dfs(vertex):
    # print(vertex)
    # * 종료 조건 1
    if(check(vertex)):
        return str(video[vertex[0]][vertex[2]])
    
    # * 종료 조건 2
    if(vertex[1]-vertex[0] == 2):
        tmp_str = "("
        for row in range(vertex[0], vertex[1]):
            for col in range(vertex[2], vertex[3]):
                tmp_str += str(video[row][col])
        # print("종료 조건 2", tmp_str, vertex)
        tmp_str += ")"
        return tmp_str
    
    new_vertex_lst = split(vertex)
    compressed = "("
    
    for new_vertex in new_vertex_lst:
        compressed += dfs(new_vertex)
    compressed += ")"
    return compressed

print(dfs((0, N, 0, N)))