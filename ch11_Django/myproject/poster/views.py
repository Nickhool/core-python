from django.shortcuts import render, get_object_or_404
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from myproject import settings
from .models import Tweet

# Create your views here.

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'author_email')
        widgets = {
            'text': forms.Textarea(attrs={'clos': 50, 'rows': 3}),
        }

def post_tweet(request, tweet_id=None):
    tweet = None
    if tweet_id:
        tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.state = 'pending'
            new_tweet.save()
            send_review_email()
            return HttpResponseRedirect('/post/thankyou')
    else:
        form = TweetForm(instance=tweet)
    return TemplateView.as_view(template_name ='post_tweet.html',
                                extra_context = {'form': form})(request)

def send_review_email():
    subject = 'Action require: review tweet'
    body = ('A new tweet has been submitted for aooroval. '
            'Please review  it as soon as possible.')
    send_mail(subject, body, settings.EMAIL_FROM, [settings.TWEET_APPROVER_EMAIL])
def thankyou(request):
    tweets_in_queue = Tweet.objects.filter(
        state='pending').aggregate(Count('id'))['id__count']
    return TemplateView.as_view(template_name ='thank_you.html',
                                extra_context = {'tweets_in_queue': tweets_in_queue})(request)


def test(request):
    # t = Tweet.objects.filter(state='pending')
    # print('1---:'+t+'\n')
    # c = t.aggregate(Count('id'))
    # print('2---:' + c + '\n')
    # q = c.values()[0]
    # print('3---:' + q + '\n')
    tweets_in_queue = Tweet.objects.filter(
        state='pending').aggregate(Count('id'))['id__count']
    return render(request, 'thank_you.html', {'tweets_in_queue': tweets_in_queue})