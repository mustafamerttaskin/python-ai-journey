"""
Day 3 - Merge Sort (Birlestirme Siralamasi)
--------------------------------------------
Bolume-boluneme-fethet (divide and conquer) yaklasimiyla calisan, kararli
(stable) bir siralama algoritmasi. Dizi ortadan ikiye bolunur, her yari
kendi icinde ozyinelemeli (recursive) olarak siralanir, sonra iki sirali
yari tek gecişte (linear pass) birlestirilir (merge edilir).

Karmasiklik:
    Zaman:  O(n log n)  -> her seviyede n elemanlik birlestirme, log n seviye
    Bellek: O(n)        -> birlestirme icin yardimci diziler kullanilir

Neden onemli: quicksort'un aksine en kotu durumda da O(n log n) garanti eder
ve stable'dir (esit elemanlarin sirasi bozulmaz). Bu yuzden dis kaynakli
(external) siralama ve linked list siralamada tercih edilir.
"""

from __future__ import annotations


def merge_sort(arr: list[int]) -> list[int]:
    """Diziyi kucukten buyuge sirali yeni bir liste olarak dondurur."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Iki sirali diziyi tek sirali dizide birlestirir (O(n) gecis)."""
    merged: list[int] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def _is_sorted(arr: list[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    samples = [
        [5, 2, 9, 1, 5, 6],
        [],
        [1],
        [3, 3, 2, 1, 2],
        list(range(10, 0, -1)),
    ]

    for original in samples:
        sorted_arr = merge_sort(original)
        status = "OK" if _is_sorted(sorted_arr) else "HATA"
        print(f"{original!r:30} -> {sorted_arr!r:30} [{status}]")
