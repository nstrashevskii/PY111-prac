import networkx as nx


# посчитать самый дешевый путь, и вернуть то как мы шли(алгоритм дейкстры посмотреть в библиотеке nx)
# all_way = [[2A, 7B, 9C, 3D],
#            [12E, 4F, 1G, 9H],
#            [1I, 5J, 2K, 5L]]


def min_way(edge: list, node_1: str, node_2: str):
    graph = nx.Graph()
    graph.add_weighted_edges_from(edge)
    print(nx.shortest_path(graph, node_1, node_2, weight='weight'))


#  2. поиск в глубину(ищем компонент связанности) посмотреть что такое компонент связанности


def count_connected():
    G = nx.Graph()
    G.add_nodes_from("ABCDEFG")  # инициализация вершин
    G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('F', 'G')])  # ребра
    comps = nx.connected_components(G)
    l_comps = []
    i = 0
    for j in comps:
        i += 1
        l_comps.append(j)
        print(f'{i} комонента связности графа {j} равна {len(j)}')
    return l_comps


# 3. Вы – компания, дающая в аренду ракеты.
# Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца),
# (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X,
# то в этот же час ее уже можно взять в аренду снова
# (т.е. час_начала может начинаться с Х).

# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты,
# чтобы удовлетворить все заявки на этот день

# решение через граф
# граф мульти-направленный(больше чем одна связь), не можем удовлетворить заявку когда колличество
# исходящих связей из одной вершины больше чем одна(исходящая степень(degree) вершины больше 1)
# g1 = nx.MultiDiGraph()


def rocket(intervals: list) -> None:
    # G = nx.MultiDiGraph()
    # G.add_nodes_from(h)
    # G.add_edges_from(intervals)
    starts = []
    for j in intervals:
        starts.append(j[0])
    for i in range(len(starts) - 1):
        for j in range(i+1, len(starts)):
            if starts[i] == starts[j]:
                print('Аренда невозможна, расписание составлено некорректно')
                quit()
    print('Все хорошо, аренда возможна')


if __name__ == '__main__':
    print(f'Задача №1 построить самый дешевый путь')
    e = [('A', 'B', 9), ('B', 'C', 9), ('C', 'D', 3), ('A', 'E', 14), ('E', 'I', 1), ('B', 'F', 4), ('F', 'J', 5),
         ('C', 'G', 1), ('G', 'K', 2), ('D', 'H', 9), ('H', 'L', 5), ('E', 'F', 4), ('F', 'G', 1), ('G', 'H', 9),
         ('I', 'J', 5), ('J', 'K', 2), ('K', 'L', 5)]
    n_1 = 'A'
    n_2 = 'L'
    min_way(e, n_1, n_2)
    # можно так же воспользоваться методом nx.single_source_dijkstra() он посчитает вес автоматически
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in e:
        if i[0] == 'A' and i[1] == 'B':
            l1.append(i[2])
        elif i[0] == 'B' and i[1] == 'F':
            l2.append(i[2])
        elif i[0] == 'F' and i[1] == 'G':
            l3.append(i[2])
        elif i[0] == 'G' and i[1] == 'K':
            l4.append(i[2])
        elif i[0] == 'K' and i[1] == 'L':
            l5.append(i[2])
    weight = min(l1) + min(l2) + min(l3) + min(l4) + min(l5)
    print(weight)
    print(f'Задача №2 компоненты связности')
    count_connected()
    print(f'Задача №3 аренда ракеты')
    int_ = [(1, 2), (3, 4), (3, 7)]
    rocket(int_)
