from django.shortcuts import render


def home(request):
    return render(request, 'krestikiNolikiApp/home.html', {})


def game(request):
    size = int(request.GET.get('size', '3'))
    matrix = [[0 for x in range(size)] for y in range(size)]

    if request.GET.get('started') == '1':
        for i in range(size):
            for j in range(size):
                matrix[i][j] = int(request.GET.get(str(i)+str(j)))

    return render(request, 'krestikiNolikiApp/game.html', {
            'icon': 'X',
            'size': size,
            'range': range(size),
            'matrix': matrix
        })
