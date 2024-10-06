from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import (ProductListView,
                           ProductDetailView,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView,
                        #    toggle_stock,
                           ContactTemplateView,
                           CategoryListView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # Главная страница
    path('', ProductListView.as_view(), name='home'),
    # Описание продукта
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    # Создание продукта
    path('create/', ProductCreateView.as_view(), name='create_product'),
    # Редактирование продукта
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    # Удаление продукта
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # Реализация наличия продукта
    # path('activity/<int:pk>/', toggle_stock, name='toggle_stock'),
    # Контакты
    path("contacts/", ContactTemplateView.as_view(template_name="contacts.html"), name='contacts'),
    # Список категорий
    path("categories/", CategoryListView.as_view(), name='categories'),
]
