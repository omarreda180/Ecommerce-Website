from .models import Category


def categories_function(request):
    return{
        'categories': Category.objects.all()
    }
