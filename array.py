def kadane_algorithm(arr):
    # Inisialisasi nilai max_sum dan current_sum dengan elemen pertama
    max_sum = current_sum = arr[0]
    
    # Mulai iterasi dari elemen kedua hingga akhir
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Contoh penggunaan
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadane_algorithm(array)
print("Jumlah terbesar dari subarray yang berdekatan adalah:", result)
