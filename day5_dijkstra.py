"""
Day 5 - Dijkstra Algoritmasi (En Kisa Yol - Agirlikli Graf)
--------------------------------------------------------------
BFS agirliksiz graflarda en kisa yolu bulur ama kenarlarin bir "maliyeti"
(agirligi) varsa (ör. yol uzunlugu, gecikme, fiyat) BFS yanlis sonuc verir.
Dijkstra bu durumda calisir (negatif agirlik OLMADIGI surece).

Fikir: Baslangic dugumunden itibaren, her adimda "su ana kadar en ucuza
ulasilan ama henuz kesinlesmemis" dugumu isleme al, komsularina olan
mesafeyi guncelle (relaxation), ve bunu bir oncelik kuyrugu (min-heap)
ile verimli yap.

Karmasiklik: O((V + E) log V)  -- heapq ile binary heap kullanildiginda.

Graf burada {dugum: [(komsu, agirlik), ...]} seklinde temsil edildi.
"""

from __future__ import annotations
import heapq
import math


WeightedGraph = dict[str, list[tuple[str, float]]]


def dijkstra(graph: WeightedGraph, start: str) -> dict[str, float]:
    """Baslangic dugumunden tum diger dugumlere olan en kisa mesafeleri
    dondurur. Ulasilamayan dugumler icin mesafe sonsuz (inf) kalir."""
    distances: dict[str, float] = {node: math.inf for node in graph}
    distances[start] = 0

    # (mesafe, dugum) ciftlerini tutan min-heap
    pq: list[tuple[float, str]] = [(0, start)]
    visited: set[str] = set()

    while pq:
        current_dist, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            distance = current_dist + weight
            if distance < distances.get(neighbor, math.inf):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def shortest_path(graph: WeightedGraph, start: str, target: str) -> tuple[list[str], float] | None:
    """En kisa yolun kendisini (dugum listesi) ve toplam maliyetini dondurur."""
    distances: dict[str, float] = {node: math.inf for node in graph}
    previous: dict[str, str | None] = {node: None for node in graph}
    distances[start] = 0

    pq: list[tuple[float, str]] = [(0, start)]
    visited: set[str] = set()

    while pq:
        current_dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == target:
            break

        for neighbor, weight in graph.get(node, []):
            distance = current_dist + weight
            if distance < distances.get(neighbor, math.inf):
                distances[neighbor] = distance
                previous[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))

    if distances.get(target, math.inf) == math.inf:
        return None

    path = [target]
    while previous[path[-1]] is not None:
        path.append(previous[path[-1]])
    path.reverse()

    return path, distances[target]


if __name__ == "__main__":
    # Ornek agirlikli graf (sehirler arasi mesafe gibi dusunulebilir)
    example_graph: WeightedGraph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("D", 1)],
        "C": [("A", 1), ("B", 2), ("D", 5)],
        "D": [("B", 1), ("C", 5), ("E", 3)],
        "E": [("D", 3)],
    }

    all_distances = dijkstra(example_graph, "A")
    print("A'dan tum dugumlere en kisa mesafeler:")
    for node, dist in sorted(all_distances.items()):
        print(f"  A -> {node}: {dist}")

    result = shortest_path(example_graph, "A", "E")
    if result:
        path, cost = result
        print(f"\nA -> E en kisa yol: {' -> '.join(path)} (toplam maliyet: {cost})")
