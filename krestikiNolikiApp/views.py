from django.shortcuts import render


def home(request):
    range_size = range(3, 10)
    return render(request, 'krestikiNolikiApp/home.html', {
        'range_size': range_size
    })


def game(request):
    size = int(request.GET.get('size', '3'))
    matrix = [[0 for x in range(size)] for y in range(size)]

    if request.GET.get('started') == '1':
        for i in range(size):
            for j in range(size):
                matrix[i][j] = int(request.GET.get(str(i) + str(j)))

    counter = 0
    for i in range(size):
        for j in range(size):
            counter += matrix[i][j]

    if request.GET.get('stroke') == 'X':
        icon = "0"
        icon_int = 1
    else:
        icon = "X"
        icon_int = 2

    diagonal = request.GET.get('diagonal')
    row = int(request.GET.get('row'))

    winner = check_win(icon_int, matrix, size, diagonal, row)

    matrix_one_row = []
    for i in matrix:
        for j in i:
            matrix_one_row.append(j)
    matrix_str = str(matrix_one_row)

    if winner > 0:
        handle = open('F:/file.txt', 'a+')
        handle.write(matrix_str + "\n")
        handle.close()

    return render(request, 'krestikiNolikiApp/game.html', {
        'icon': icon,
        'size': size,
        'range': range(size),
        'matrix': matrix,
        'diagonal': diagonal,
        'row': row,
        'winner': winner
    })


def check_win(pl, m, n, diagonal, num):  # проверка на выиграшные комбинации
    win = []
    b = []
    for i in m:
        for j in i:
            b.append(j)
    for i in range(n):
        lst = range(n)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по вертикали
    for i in range(0, n):
        lst = range(0, n ** 2 - n + 1, n)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по горизнтали
    if diagonal == 'on':
        di1 = list(range(0, n * (n - 2), n)) + list(range(1, n - 2))
        for i in di1:
            lst = range(i, n ** 2, n + 1)
            one_win = []
            all(b[i] == b[j] for j in lst)
            for k in lst:
                one_win.append(b[k])
            win.append(one_win)  # диагональ слева направо
        di2 = list(range(n - 1, n * (n - 2), n)) + list(range(2, n - 1))
        for i in di2:
            if i < n:
                lst = range(i, n * i + 1, n - 1)
            else:
                lst = range(i, n ** 2, n - 1)
            one_win = []
            all(b[i] == b[j] for j in lst)
            for k in lst:
                one_win.append(b[k])
            win.append(one_win)  # диагональ справа налево
    for i in win:
        count = 0
        for j in i:
            if j == pl:
                count += 1
            else:
                count = 0
            if count >= num:
                return pl
    return False
