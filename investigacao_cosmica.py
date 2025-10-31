
def get_distance_between_stars(star1, star2):

    if star1[0] == star2[0]:
        return abs(star1[1] - star2[1])

    if star1[1] == star2[1]:
        return abs(star1[0] - star2[0])

    return -1


def solve():

    n = int(input())

    estrelas = []
    for _ in range(n):
        estrelas.append(tuple(map(int, input().split())))

    dists = []
    for i in range(n - 1):
        d = get_distance_between_stars(estrelas[i], estrelas[i + 1])
        dists.append(d)

    min_r0 = 1
    max_r0 = dists[0]
    s = 0

    for j in range(n - 1):
        s = dists[j] - s

        if (j + 1) % 2 == 1:
            max_r0 = min(max_r0, s - 1)
        else:
            min_r0 = max(min_r0, 1 - s)

    if min_r0 > max_r0:
        return -1

    return max_r0


print(solve())


'''
3
0 0
4 0
4 4

5
0 0
4 0
4 2
4 6
6 6


4
0 0
4 0
4 4
4 7


'''