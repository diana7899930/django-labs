from django.shortcuts import render


def home(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Це головна сторінка сайту. Тут є посилання на всі інші сторінки.',
        'is_home': True,
    }
    return render(request, 'main/page.html', context)


def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Це сторінка про нас. Контент змінюється через context.',
        'is_home': False,
    }
    return render(request, 'main/page.html', context)


def contacts(request):
    context = {
        'title': 'Контакти',
        'content': 'Це сторінка контактів. Вона також використовує render і context.',
        'is_home': False,
    }
    return render(request, 'main/page.html', context)