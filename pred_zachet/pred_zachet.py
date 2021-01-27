import networkx as nx
from Tasks.a0_my_stack import peek


def min_way(edge: list, node_1: str, node_2: str):
    graph = nx.Graph()
    graph.add_weighted_edges_from(edge)
    print(nx.shortest_path(graph, node_1, node_2, weight='weight'))


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
    print(f'Всего компонент связности {i}')
    return l_comps


def schitalka(n: int, k: int) -> int:
    list_people = [i for i in range(1, n + 1)]
    list_slog = [j for j in range(1, k + 1)]
    m = 0
    while True:
        for v in range(1, k + 1):
            if len(list_people) <= len(list_slog):
                return list_people[0]
            if v == list_slog[k - 1]:
                del list_people[m]
                m = 0
            m += 1


if __name__ == '__main__':
    print(f'Задача №2 считалка')
    print('-------------')
    print(schitalka(10, 5))
    print(f'Задача №4 построить самый дешевый путь')
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
    print('-------------')
    print(f'Задача №3 компоненты связности')
    count_connected()
    print('-------------')
    print(f'Задача №6 аренда ракеты')
    int_ = [(1, 2), (3, 4), (3, 7)]
    rocket(int_)

