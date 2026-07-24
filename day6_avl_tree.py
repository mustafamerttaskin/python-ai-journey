"""
Day 6 - AVL Agaci (Kendini Dengeleyen Ikili Arama Agaci)
--------------------------------------------------------------
SIradan bir ikili arama agacinda (BST) elemanlar sirali eklenirse agac bir
linked list'e donusur ve arama O(n) olur. AVL agaci, her ekleme/silmeden
sonra her dugumun "denge faktorunu" (sol alt agac yuksekligi - sag alt
agac yuksekligi) kontrol edip -1, 0, +1 disina cikarsa rotasyon yaparak
agaci otomatik dengede tutar.

Bu sayede arama / ekleme / silme her zaman O(log n) garantisi verir
(dengesiz bir BST'de en kotu durum O(n)'dir).

Bu dosyada sadece ekleme (insert) ve gerekli rotasyonlar (LL, RR, LR, RL)
uygulanmistir; agacin dogru sekilde dengede kaldigini gostermek icin
in-order gezinme (sirali cikti verir) ve yukseklik/denge kontrolleri
eklendi.
"""

from __future__ import annotations


class Node:
    __slots__ = ("value", "left", "right", "height")

    def __init__(self, value: int):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.height = 1  # yaprak dugum yuksekligi 1


def _height(node: Node | None) -> int:
    return node.height if node else 0


def _balance_factor(node: Node | None) -> int:
    return _height(node.left) - _height(node.right) if node else 0


def _update_height(node: Node) -> None:
    node.height = 1 + max(_height(node.left), _height(node.right))


def _rotate_right(y: Node) -> Node:
    """
          y                x
         / \\             / \\
        x   T3   -->    T1   y
       / \\                  / \\
      T1  T2               T2  T3
    """
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x: Node) -> Node:
    """Simetrik: _rotate_right'in aynasi."""
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    _update_height(x)
    _update_height(y)
    return y


def insert(node: Node | None, value: int) -> Node:
    """Degeri agaca ekler ve dengelenmis yeni kok dugumu dondurur."""
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    else:
        return node  # yinelenen (duplicate) deger - agaci degistirme

    _update_height(node)
    balance = _balance_factor(node)

    # Sol-Sol durumu
    if balance > 1 and value < node.left.value:
        return _rotate_right(node)

    # Sag-Sag durumu
    if balance < -1 and value > node.right.value:
        return _rotate_left(node)

    # Sol-Sag durumu
    if balance > 1 and value > node.left.value:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)

    # Sag-Sol durumu
    if balance < -1 and value < node.right.value:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


def inorder(node: Node | None) -> list[int]:
    """Sirali (in-order) gezinme -> her zaman kucukten buyuge sirali cikti verir."""
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def is_balanced(node: Node | None) -> bool:
    """Agacin her dugumunde AVL kosulunun (|balance| <= 1) saglandigini dogrular."""
    if node is None:
        return True
    if abs(_balance_factor(node)) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


class AVLTree:
    """Kucuk bir sarmalayici (wrapper) sinif - kok dugumu kullaniciya saklar."""

    def __init__(self):
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        self.root = insert(self.root, value)

    def inorder(self) -> list[int]:
        return inorder(self.root)

    def height(self) -> int:
        return _height(self.root)

    def is_balanced(self) -> bool:
        return is_balanced(self.root)


if __name__ == "__main__":
    tree = AVLTree()

    # Kasitli olarak sirali (artan) degerler ekleniyor - sıradan bir BST'de
    # bu durum agaci duz bir linked list'e cevirirdi (yukseklik = n).
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        tree.insert(v)
        print(f"{v} eklendi -> yukseklik={tree.height()}, dengeli mi={tree.is_balanced()}")

    print("\nSirali (in-order) gezinme:", tree.inorder())
    print("Beklenen: kucukten buyuge sirali liste ->", sorted(values))
    print(f"Son agac yuksekligi: {tree.height()} "
          f"(dengesiz BST olsaydi {len(values)} olurdu)")
