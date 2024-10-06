from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from catalog.forms import ProductForm, ProductModeratorForm, VersionForm
from catalog.models import Category, Product, Version
from django.urls import reverse, reverse_lazy

from catalog.services import get_categories_from_cash


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        """Информация по актуальной версии товара"""
        context_data = super().get_context_data(**kwargs)
        version_dict = {}
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.is_current:
                    if version.product_id == int(product.pk):
                        version_dict[version.product_id] = version.name
        context_data["versions"] = version_dict
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """Привязка пользователя к продукту"""
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:view_product", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self) -> type[BaseModelForm]:
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif (
            user.has_perm("catalog.can_edit_in_stock")
            and user.has_perm("catalog.can_edit_description")
            and user.has_perm("catalog.can_edit_category")
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactTemplateView(TemplateView):
    pass


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cash()


# @login_required
# @permission_required('catalog.can_edit_in_stock')
# def toggle_stock(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     product_item.in_stock = not product_item.in_stock
#     product_item.save()
#     return redirect(reverse("catalog:home"))
