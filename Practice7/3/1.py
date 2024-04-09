import graphviz


def draw(vertices, edges):
    dot = graphviz.Digraph()
    for v in vertices:
        dot.node(str(v[0]), v[1])
    for e in edges:
        dot.edge(str(e[0]), str(e[1]))
    dot.render('graph1', format='png', cleanup=True)


draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)])
