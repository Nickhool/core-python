from django.shortcuts import render_to_response
from django.views.generic import RedirectView, TemplateView
from blog.models import BlogPost, BlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ExtraContextTemplateView(TemplateView):
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context

def archive(request):
    posts = BlogPost.objects.all()[:10]
    # return render_to_response('archive.html', {'posts': posts,
    #                             'form': BlogPostForm()})
    return TemplateView.as_view(template_name ='archive.html', extra_context = {'posts': posts,
                                'form': BlogPostForm()})(request)

@csrf_exempt # This skips csrf validation. Use csrf_protect to have validation
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')