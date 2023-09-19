from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Blog, ContactModel, CommentModel
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect


class CommentView(CreateView):
    model = CommentModel
    template_name = 'blog-single.html'
    fields = ['name', 'email', 'website', 'message']

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data()
    #     comments = CommentModel.objects.filter(post__slug=self.kwargs.get('slug'))
    # comments = CommentModel.objects.all()
    # data['comments'] = comments
    # print(comments)
    # return data

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Blog, slug=self.kwargs.get('slug'))
        return super(CommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.kwargs.get('slug')})

    # def form_valid(self, form):
    #     blog_slug = self.kwargs['slug']
    #     blog = Blog.objects.get(slug=blog_slug)
    #     form.instance.blog = blog
    #     form.save()
    #     return redirect('detail', slug=blog_slug)


class ContactView(CreateView):
    model = ContactModel
    template_name = 'contact.html'
    fields = ['full_name', 'email', 'subject', 'message']
    success_url = reverse_lazy('home')


class HomeView(ListView):
    model = Blog
    template_name = 'index.html'

    def get_queryset(self):
        qr = super().get_queryset()
        qr = qr.filter(is_published=True)

        return qr


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_queryset(self):
        qr = super().get_queryset()
        qr = qr.filter(is_published=True)

        return qr


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-single.html'
