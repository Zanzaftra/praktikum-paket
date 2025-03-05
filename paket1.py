# mengimpor modul geometri2D yang berada di dalam paket Matematika
import MATEMATIKA_FEB_2025.Geometri2D

def main():
    # bujursangkar
    sisi = 5

    luas = MATEMATIKA_FEB_2025.Geometri2D.LBujursangkar(sisi)

    print("BUJURSANGKAR")
    print("Panjang sisi\t: ", sisi)
    print("Luas\t: ", luas)

if __name__ == "__main__":
    main()