def calculate_sum(numbers):
    """Fungsi ini menerima list angka dan mengembalikan jumlah semua angka dalam list"""
    return sum(numbers)

def calculate_product(numbers):
    """Fungsi ini menerima list angka dan mengembalikan hasil perkalian semua angka dalam list"""
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    """Fungsi ini akan meminta input dari user untuk sebuah list angka, kemudian mencetak hasil penjumlahan dan perkalian angka-angka tersebut"""
    numbers = input("Masukkan beberapa angka, dipisahkan dengan spasi: ").split()
    numbers = [int(num) for num in numbers]
    sum_of_numbers = calculate_sum(numbers)
    product_of_numbers = calculate_product(numbers)
    print("Jumlah angka dalam list adalah:", sum_of_numbers)
    print("Hasil perkalian angka dalam list adalah:", product_of_numbers)

if __name__ == '__main__':
    main()
