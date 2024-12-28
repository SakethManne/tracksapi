from django.urls import path, include

urlpatterns = [
    # path('', include('masters.api.urls')),
    path('', include('entities.api.urls')),
    path('', include('uaa.api.urls')),
    # path('', include('products.api.urls')),
    # path('', include('production.api.urls')),
    # path('', include('indents.api.urls')),
    # path('', include('transactions.api.urls')),
    # path('', include('heals.api.urls')),
    # path('', include('inventory.api.urls')),
    # path('', include('reports.urls')),
]
