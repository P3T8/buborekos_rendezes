
 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Bekéri az elemek számát
N = int(input("Adja meg az elemek számát: "))

# Létrehozza az adott elemszámú tömböt
T = []
for i in range(N):
    elem = int(input(f"Adja meg a(z) {i+1}. elemet: "))
    T.append(elem)

# Sorba rendezi a tömböt
bubble_sort(T)

# Kiírja a rendezett tömböt
print("A rendezett tömb:", T)
