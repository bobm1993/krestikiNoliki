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

    matrix_str = str(mat_to_str(matrix))

    if winner > 0:
        handle = open('file.txt', 'a+')
        handle.write(str(matrix_str).strip('[]') + "\n")
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


def history(request):
    handle = open('file.txt', 'r')
    hist_str = handle.read()
    hist_arr = hist_str.split('\n')
    hist_rev = hist_arr[::-1]
    hist_num = [game.split(', ') for game in hist_rev[1:11]]
    hist = []
    for i in hist_num:
        hist_temp = []
        for j in i:
            if j == '0':
                hist_temp.append('')
            elif j == '1':
                hist_temp.append('X')
            else:
                hist_temp.append('O')
        hist.append(hist_temp)

    return render(request, 'krestikiNolikiApp/history.html', {
        'hist': hist
    })


def check_win(pl, m, n, diagonal, num):  # проверка на выиграшные комбинации
    win = []
    b = mat_to_str(m)
    for i in range(0, n ** 2, n):
        lst = range(n)
        one_win = []
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по горизонтали
    for i in range(n):
        lst = range(0, n ** 2 - n + 1, n)
        one_win = []
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по вертикали
    if diagonal == 'on':
        di1 = list(range(0, n * (n - 2), n)) + list(range(1, n - 2))
        for i in di1:
            lst = range(i, n ** 2, n + 1)
            one_win = []
            for k in lst:
                one_win.append(b[k])
            win.append(one_win)  # диагонали слева направо
        di2 = list(range(n - 1, n * (n - 2), n)) + list(range(2, n - 1))
        for i in di2:
            if i < n:
                lst = range(i, n * i + 1, n - 1)
            else:
                lst = range(i, n ** 2, n - 1)
            one_win = []
            for k in lst:
                one_win.append(b[k])
            win.append(one_win)  # диагонали справа налево
    for i in win:
        count = 0
        for j in i:
            if j == pl:
                count += 1
            else:
                count = 0
            if count >= num:
                return pl
    if 0 not in b:
        return 3
    return False


def mat_to_str(mat):
    mat_str = []
    for i in mat:
        for j in i:
            mat_str.append(j)
    return mat_str
