from django.shortcuts import render
from datetime import datetime

# Create your views here.

posts = [
    {
        'tittle': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
]

def list_posts(request):
    return render(request, 'feed.html', { 'posts': posts })
