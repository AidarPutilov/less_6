from django.urls import path
from catalog.views import (ProductListView,
                           ProductDetailView,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView,
                           toggle_stock,
                           ContactTemplateView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # Главная страница
    path('', ProductListView.as_view(), name='home'),
    # Описание продукта
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    # Создание продукта
    path('create/', ProductCreateView.as_view(), name='create_product'),
    # Редактирование продукта
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    # Удаление продукта
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # Реализация наличия продукта
    path('activity/<int:pk>/', toggle_stock, name='toggle_stock'),
    # Контакты
    path("contacts/", ContactTemplateView.as_view(template_name="contacts.html"), name='contacts'),
]
