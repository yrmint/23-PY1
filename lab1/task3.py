disc = 1.44     # Информационный объем дискеты
book = 100      # Количество страниц в книге
page = 50       # Число строк на странице
line = 25       # Количество символов в строке
symb = 4        # Байт для хранения кода одного символа

kb = 1024       # Байт в Кб
mb = 1024 * kb  # Байт в Мб

print("Количество книг, помещающихся на дискету:", int(disc / ((symb * line * page * book) / mb)))
