from django.shortcuts import render

# Create your views here.
def index_view(request):
    page_name = 'Ana Sayfa'
    return render(request, 'site/pages_site/index.html', locals())


def blog_grid_view(request):
    page_name = 'Blog Grid Page'
    return render(request, 'site/pages_site/blog-grid.html', locals())

def blog_single_view(request):
    page_name = 'Blog Single Page'
    return render(request,'site/pages_site/blog-single.html', locals())