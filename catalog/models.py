from django.db import models


# Категории продуктов
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="наименование"
    )
    description = models.TextField(
        verbose_name="описание",
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


# Продукты
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="наименование"
    )
    description = models.TextField(
        verbose_name="описание",
        null=True, blank=True
    )
    preview = models.ImageField(
        upload_to="previews/",
        verbose_name="изображение",
        null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        null=True, blank=True
    )
    price = models.IntegerField(verbose_name="цена")
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="дата создания",
        null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="дата изменения",
        null=True, blank=True
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name="в наличии"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name",)


# Версии
class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='version',
        on_delete=models.SET_NULL,
        verbose_name='продукт',
        null=True, blank=True
    )
    number = models.CharField(
        max_length=10,
        verbose_name='номер версии'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='название версии'
    )
    is_current = models.BooleanField(
        default=False,
        verbose_name='текущая версия'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product',)
