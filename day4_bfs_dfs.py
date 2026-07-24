"""
Day 4 - BFS ve DFS (Genislik ve Derinlik Oncelikli Arama)
-----------------------------------------------------------
Bir grafi (graph) dolasmanin iki temel yontemi:

* BFS (Breadth-First Search): Kaynaktan baslayip once tum komsulari,
  sonra komsularin komsularini gezer. Bir kuyruk (queue / collections.deque)
  kullanir. En kisa yol (en az kenar sayisi) garantisi verir -> agirliksiz
  graflarda "en kisa yol" sorusu icin idealdir.

* DFS (Depth-First Search): Bir dali sonuna kadar gidip sonra geri donup
  (backtrack) baska dali dener. Bir yigin (stack) ya da ozyineleme
  kullanir. Baglantili bilesenleri bulmak, dongu tespiti, topolojik
  siralama gibi problemlerde kullanilir.

Graf burada komsuluk listesi (adjacency list) olarak, yani
{dugum: [komsu1, komsu2, ...]} seklinde bir sozluk (dict) ile temsil edildi.
"""

from __future__ import annotations
from collections import deque


Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    """Ziyaret sirasini (traversal order) bir liste olarak dondurur."""
    visited = {start}
    order: list[str] = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph: Graph, start: str) -> list[str]:
    """Ozyinelemeli DFS. Ziyaret sirasini bir liste olarak dondurur."""
    visited: set[str] = set()
    order: list[str] = []

    def _visit(node: str) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _visit(neighbor)

    _visit(start)
    return order


def dfs_iterative(graph: Graph, start: str) -> list[str]:
    """Ozyinelemesiz (stack tabanli) DFS - derin graflarda recursion limitine
    takilmamak icin alternatif."""
    visited: set[str] = set()
    order: list[str] = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Komsulari ters sirada ekle ki soldan saga gezilsin (ozyinelemeli
        # versiyonla ayni sirayi versin)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def shortest_path_bfs(graph: Graph, start: str, target: str) -> list[str] | None:
    """BFS ile agirliksiz grafta en kisa yolu (dugum listesi) bulur."""
    if start == target:
        return [start]

    visited = {start}
    queue: deque[tuple[str, list[str]]] = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    # Ornek graf (yonsuz - undirected):
    #     A - B - D
    #      \ /   /
    #       C - E
    example_graph: Graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "E"],
        "D": ["B", "E"],
        "E": ["C", "D"],
    }

    print("BFS  (A'dan):", bfs(example_graph, "A"))
    print("DFS  (A'dan):", dfs(example_graph, "A"))
    print("DFS* (A'dan, iterative):", dfs_iterative(example_graph, "A"))
    print("A -> E en kisa yol:", shortest_path_bfs(example_graph, "A", "E"))
