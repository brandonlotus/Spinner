def counterClockwise(List_awal):      # membuat function dengan nama "counterClockwise" dengan parameter "List_awal"
    a = List_awal[0][0]               # buat variable a untuk menampung angka-1 (dengan indexing)
    b = List_awal[0][1]               # buat variable b untuk menampung angka-2
    c = List_awal[1][0]               # buat variable c untuk menampung angka-4
    d = List_awal[2][0]               # buat variable d untuk menampung angka-7
    List_awal[0][0] = List_awal[0][2] # ganti posisi angka-3 ke posisi angka-1
    List_awal[0][1] = List_awal[1][2] # ganti posisi angka-6 ke posisi angka-2
    List_awal[0][2] = List_awal[2][2] # ganti posisi angka-9 ke posisi angka-3
    List_awal[1][0] = b               # ganti posisi angka-2 (variabel b) ke posisi angka-4
    List_awal[1][2] = List_awal[2][1] # ganti posisi angka-8 ke posisi angka-6
    List_awal[2][0] = a               # ganti posisi angka-1 (variabel a) ke posisi angka-7
    List_awal[2][1] = c               # ganti posisi angka-4 (variabel c) ke posisi angka-8
    List_awal[2][2] = d               # ganti posisi angka-7 (variabel d) ke posisi angka-9
    return List_awal                  # return akhirnya menampilkan list dengan elemen yang sudah berubah posisi
    
List_awal = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(counterClockwise(List_awal))