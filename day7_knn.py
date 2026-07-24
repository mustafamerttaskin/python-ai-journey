"""
Day 7 - K-En Yakin Komsu (K-Nearest Neighbors / KNN) - Sifirdan Implementasyon
--------------------------------------------------------------------------------
KNN, "denetimli" (supervised) bir siniflandirma algoritmasi ama gercek
anlamda bir "egitim" (training) asamasi yoktur (lazy learning): tum egitim
verisi oldugu gibi saklanir. Yeni bir nokta geldiginde:

  1. O noktanin egitim setindeki her noktaya olan uzakligi hesaplanir
     (burada Oklid / Euclidean mesafesi kullanildi).
  2. En yakin k tanesi secilir.
  3. Bu k komsu arasinda en sik gorulen sinif (coğunluk oyu / majority vote)
     tahmin olarak donduruluz.

Bu dosya harici kutuphane (scikit-learn, numpy vs.) kullanmadan, sadece
Python'un standart kutuphanesiyle (math, collections) yazildi -- amac
algoritmanin nasil calistigini gercekten anlamak. drone-audio-detection
projesindeki SVM/CNN karsilastirmasinda oldugu gibi, "kutuphaneyi cagirmak"
ile "algoritmayi anlamak" arasindaki farki gormek icin.
"""

from __future__ import annotations
import math
from collections import Counter


Point = tuple[float, ...]


def euclidean_distance(a: Point, b: Point) -> float:
    """Iki nokta arasindaki Oklid (duz cizgi) mesafesi."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


class KNNClassifier:
    """Basit, sifirdan yazilmis bir KNN siniflandirici.

    fit()    -> egitim verisini oldugu gibi saklar (gercek egitim yapmaz)
    predict()-> her yeni nokta icin en yakin k komsuya bakip oy coklugu ile
                sinif tahmini yapar
    """

    def __init__(self, k: int = 3):
        if k < 1:
            raise ValueError("k en az 1 olmalidir")
        self.k = k
        self._points: list[Point] = []
        self._labels: list[str] = []

    def fit(self, points: list[Point], labels: list[str]) -> None:
        if len(points) != len(labels):
            raise ValueError("points ve labels ayni uzunlukta olmali")
        if len(points) < self.k:
            raise ValueError(f"en az k={self.k} egitim ornegi gerekli, {len(points)} verildi")
        self._points = points
        self._labels = labels

    def predict_one(self, point: Point) -> str:
        distances = [
            (euclidean_distance(point, p), label)
            for p, label in zip(self._points, self._labels)
        ]
        distances.sort(key=lambda pair: pair[0])
        nearest_labels = [label for _, label in distances[: self.k]]

        vote_counts = Counter(nearest_labels)
        return vote_counts.most_common(1)[0][0]

    def predict(self, points: list[Point]) -> list[str]:
        return [self.predict_one(p) for p in points]

    def accuracy(self, points: list[Point], true_labels: list[str]) -> float:
        predictions = self.predict(points)
        correct = sum(p == t for p, t in zip(predictions, true_labels))
        return correct / len(true_labels)


if __name__ == "__main__":
    # Basit 2 boyutlu, 2 sinifli oyuncak (toy) veri seti:
    # "kirmizi" noktalar sol-alt bolgede, "mavi" noktalar sag-ust bolgede
    train_points: list[Point] = [
        (1.0, 1.0), (1.5, 2.0), (1.2, 0.8), (2.0, 1.5),   # kirmizi
        (7.0, 7.5), (8.0, 8.0), (7.5, 6.5), (8.5, 7.0),   # mavi
    ]
    train_labels = ["kirmizi", "kirmizi", "kirmizi", "kirmizi",
                     "mavi", "mavi", "mavi", "mavi"]

    knn = KNNClassifier(k=3)
    knn.fit(train_points, train_labels)

    test_points: list[Point] = [(1.3, 1.4), (7.8, 7.2), (4.5, 4.5)]
    predictions = knn.predict(test_points)

    for point, pred in zip(test_points, predictions):
        print(f"{point} -> tahmin: {pred}")

    # Egitim verisinin kendisi uzerinde dogruluk (sanity check - k>1 icin
    # %100 olmasi sart degildir ama bu ayrik toy datasette oyle cikar)
    acc = knn.accuracy(train_points, train_labels)
    print(f"\nEgitim verisi uzerinde dogruluk: %{acc * 100:.1f}")
