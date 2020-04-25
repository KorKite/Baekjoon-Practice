def check(color):
    visited = [[False for i in range(6)] for i in range(12)]
    count = 0
    answer_queue = []
    for k in range(12):
        for i in range(6):
            if puyo[k][i] == color and not visited[k][i]:
                queue = [[k,i]]
                one_shot = []
                while len(queue) != 0:
                    a = queue.pop(0)
                    if visited[a[0]][a[1]] == True:
                        continue
                    if puyo[a[0]][a[1]] != color:
                        continue
                    visited[a[0]][a[1]] = True
                    garo = a[0]
                    sero = a[1]
                    count += 1
                    one_shot.append(a)

                    if sero+1 < 6 and puyo[garo][sero+1] == color and not visited[garo][sero+1]:
                        queue.append([garo, sero+1])

                    if garo+1 < 12 and puyo[garo+1][sero] == color and not visited[garo+1][sero]:
                        queue.append([garo+1, sero])

                    if sero-1 >= 0 and puyo[garo][sero-1] == color and not visited[garo][sero-1]:
                        queue.append([garo, sero-1])

                    if garo-1 >=0 and puyo[garo-1][i] == color and not visited[garo-1][sero]:
                        queue.append([garo-1, sero])

                if count >=4:
                    answer_queue.append(one_shot)
                count = 0

    return answer_queue

def clearing(vis):
    if len(vis) == 0:
        return

    for i in vis:
        for k in i:
            puyo[k[0]][k[1]] = "."

def all_clear():
    for i in range(6):
        tmp = []
        for k in range(12):
            if puyo[k][i] != ".":
                tmp.append(puyo[k][i])
        if len(tmp) == 0:
            continue
        else:
            for m in range(len(tmp)):
                puyo[m][i] = tmp[m]
            for n in range(len(tmp), 12):
                puyo[n][i] = "."




puyo = [[None for i in range(6)] for i in range(12)]
for i in range(12):
    a = input()
    for k in range(6):
        puyo[11-i][k] = a[k]


output = 0
while True:
    r_vis = check("R")
    p_vis = check("P")
    g_vis = check("G")
    b_vis = check("B")
    y_vis = check("Y")
    total = len(r_vis) + len(p_vis) + len(g_vis) + len(b_vis) + len(y_vis)

    if total == 0:
        break

    else:
        output += 1
        clearing(r_vis)
        clearing(p_vis)
        clearing(g_vis)
        clearing(b_vis)
        clearing(y_vis)
        all_clear()
print(output)




