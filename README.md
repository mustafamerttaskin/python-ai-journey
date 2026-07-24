<div align="center">

# 🧠 Python & Algoritma Yolculuğu

**Temellerden algoritmalara: günlük Python pratik günlüğü**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Durum-Aktif-success)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

## Bu repo ne işe yarıyor

Python öğrenme sürecimi gün gün belgelediğim bir günlük. Her dosya bağımsız,
kendi kendine yeten (self-contained) bir alıştırma; önceki günler silinmiyor,
değiştirilmiyor — böylece ilerleme (dosya I/O'dan algoritmalara doğru artan
kapsam) baştan sona görünür kalıyor.

İlk günler temel dosya işlemleri ve veri işlemeyi kapsıyordu. Sonraki günlerde
teknik mülakatlarda ve COE216 dersinde de karşıma çıkan klasik algoritma ve
veri yapılarını (arama, sıralama, graf algoritmaları, dengelenmiş ağaçlar,
basit bir makine öğrenmesi algoritması) sıfırdan, harici kütüphane
kullanmadan implemente ettim.

## İçerik

| Dosya | Konu | Karmaşıklık |
|---|---|---|
| `day1.py` | İlk script — temel `print` çıktısı. | — |
| `day2.py` | `grades.txt`'ten öğrenci notlarını okuyup sınıf ortalamasını hesaplar, her öğrenciyi çalışma zamanında girilen bir eşiğe göre geçti/kaldı olarak sınıflandırır ve sonuçları `result.txt`'e yazar. Dosya I/O, fonksiyonlar, temel veri işleme. | — |
| `day3_merge_sort.py` | **Merge Sort** — böl-fethet yaklaşımıyla kararlı (stable) sıralama. | O(n log n) |
| `day4_bfs_dfs.py` | **BFS & DFS** — komşuluk listesiyle temsil edilen bir grafta genişlik/derinlik öncelikli arama; BFS ile ağırlıksız grafta en kısa yol. | O(V + E) |
| `day5_dijkstra.py` | **Dijkstra** — ağırlıklı grafta `heapq` tabanlı en kısa yol algoritması; hem tüm mesafeler hem de tek bir hedefe olan yol/maliyet döndürülüyor. | O((V+E) log V) |
| `day6_avl_tree.py` | **AVL Ağacı** — kendini dengeleyen ikili arama ağacı; LL/RR/LR/RL rotasyonları, denge kontrolü ve in-order gezinme dahil. | O(log n) |
| `day7_knn.py` | **K-En Yakın Komşu (KNN)** — sıfırdan (scikit-learn'süz) yazılmış, Öklid mesafesi ve çoğunluk oyuyla çalışan basit bir sınıflandırıcı. | O(n) / tahmin |

## Çalıştırma

Harici bağımlılık yok — sadece Python 3.11+ standart kütüphanesi.

```bash
git clone https://github.com/mustafamerttaskin/python-ai-journey.git
cd python-ai-journey

python day3_merge_sort.py
python day4_bfs_dfs.py
python day5_dijkstra.py
python day6_avl_tree.py
python day7_knn.py

# day2 için önce grades.txt ile aynı klasörde çalıştırın:
python day2.py
```

Her dosya `if __name__ == "__main__":` bloğunda kendi örnek verisiyle
çalışır ve sonucu doğrudan terminale yazdırır — ayrı bir test dosyasına
gerek kalmadan algoritmanın doğru çalıştığı gözle görülebilir.

## Neden sıfırdan yazıldı

Amaç `sorted()` çağırmak ya da `scikit-learn.KNeighborsClassifier`
kullanmak değil — algoritmanın *neden* öyle çalıştığını, karmaşıklığını ve
sınırlarını gerçekten anlamaktı. Bu yaklaşım
[`drone-audio-detection`](https://github.com/mustafamerttaskin/drone-audio-detection)
projesindeki SVM/CNN karşılaştırmasında da aynı: önce klasik yöntemi
kavrayıp sonra daha karmaşık araçlara geçmek.

## Yol haritası

- [x] Dosya I/O ve temel veri işleme
- [x] Klasik sıralama algoritması (Merge Sort)
- [x] Graf arama algoritmaları (BFS, DFS)
- [x] Ağırlıklı en kısa yol (Dijkstra)
- [x] Dengelenmiş ikili arama ağacı (AVL)
- [x] Basit bir ML algoritması sıfırdan (KNN)
- [ ] Hash table sıfırdan implementasyonu
- [ ] Dinamik programlama serisi (knapsack, LCS, edit distance)

## Lisans

MIT
