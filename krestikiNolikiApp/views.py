from django.shortcuts import render


def home(request):
    range_size = range(3, 10)
    # size = int(request.GET.get('size', '3'))
    # range_win = range(3, size+1)
    return render(request, 'krestikiNolikiApp/home.html', {
        'range_size': range_size,
        # 'range_win': range_win
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

    if counter % 3 == 0:
        icon = "X"
        icon_int = 2
    else:
        icon = "O"
        icon_int = 1

    diagonal = request.GET.get('diagonal')
    row = int(request.GET.get('row'))

    winner = check_win(icon_int, matrix, size, diagonal, row)

    return render(request, 'krestikiNolikiApp/game.html', {
        'icon': icon,
        'size': size,
        'range': range(size),
        'matrix': matrix,
        'diagonal': diagonal,
        'row': row
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
        win.append(one_win)  # выиграши по горизонтали
    for i in range(0, n):
        lst = range(0, n ** 2 - n + 1, n)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по вертикали
    if diagonal == 'on':
        for i in range(0, n, n):
            lst = range(0, n ** 2, n + 1)
            one_win = []
            all(b[i] == b[i + j] for j in lst)
            for k in lst:
                one_win.append(b[i + k])
            win.append(one_win)  # диагональ слева направо
        for i in range(n - 1, n):
            lst = list(range(0, n ** 2 - n, n - 1))
            one_win = []
            all(b[i] == b[i + j] for j in lst)
            for k in lst:
                one_win.append(b[i + k])
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
