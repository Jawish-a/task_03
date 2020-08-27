from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
            {"restaurant_name": "Riyadh Yummt resturant", "food_type": "Greek food"},
            {"restaurant_name": "Jeddah Yummt resturant", "food_type": "Arabian Food"},
            {"restaurant_name": "Dammam Yummt resturant", "food_type": "Italian Food"},
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {"restaurant_name": "Riyadh Yummt resturant", "food_type": "Greek food"},
    }
    return render(request, 'detail.html', context)
