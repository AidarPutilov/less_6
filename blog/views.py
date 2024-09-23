from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogArchiveListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=False)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'picture')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'slug', 'picture')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


def toggle_published(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    blog_item.is_published = not blog_item.is_published
    blog_item.save()
    return redirect(reverse('blog:blog_list'))
