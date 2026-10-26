def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]
    rata_rata = sum(nilai) / len(nilai)
    jumlah_lulus = sum(1 for angka in nilai if angka >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI\n")
        file.write(f"Jumlah data valid: {len(nilai)}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {min(nilai):.2f}\n")
        file.write(f"Nilai maksimum: {max(nilai):.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}")


data = baca_data("data/nilai.txt")
tulis_rekap("data/hasil_rekap.txt", data)