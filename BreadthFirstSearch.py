# https://informatics.msk.ru/mod/statements/view.php?id=26332&chapterid=111649#1
# В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

# Входные данные
# Первым на вход поступает число N –– количество вершин в графе ( 1 ≤ N ≤ 100 ).
# Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 –– наличие ребра). 
# Далее задаются номера двух вершин –– начальной и конечной.

# Выходные данные
# Выведите L –– длину кратчайшего пути (количество ребер, которые нужно пройти). 
# Если пути не существует, выведите одно число - 1 .
import queue

# N = int(input())

# MS = [[] for i in range(N)]
# for i in range(N):
#   MS[i] = [int(el) for el in input().split()]

# S, F = map(int, input().split())


def BFS(s, q, G, dist,prev):        # s - стартовая вершина, q - очередь, G - списки смежности,  dist[i] - расстояние до точки i, prev[i] - предыдущая вершина i
  q.put(s)                                

  while not q.empty():              # пока очередь не пуста, достаем вершины и пересчитываем расстояние
    u = q.get()
    for v in G[u]:
      if dist[v] > dist[u] + 1:
        dist[v] = dist[u] + 1       # расстояние до текущей вершины = расстояние до предыдущей вершины + 1
        prev[v] = u
        q.put(v)

N = 5
MS = [[0, 1, 0, 0, 1],
      [1, 0, 1, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],]
S,F = 3, 5
S-=1
F-=1

G = [[] for i in range(N)]
for i in range(N):
  for j in range(N):
    if MS[i][j]: G[i].append(j)

INF = 1e9
dist = [INF for i in range(N)]
prev = [-1 for i in range(N)]

dist[S] = 0

q = queue.Queue()

BFS(S,q,G,dist,prev)

if dist[F] == INF:
  print(-1)
else:
  print(dist[F])


