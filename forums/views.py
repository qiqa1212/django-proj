from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect





def index(request):
     return render(request, 'forums/index.html')

def rules(request):
    return render(request, 'forums/rules.html')


def topics(request):
     topics = Topic.objects.order_by('date_added')
     context = {'topics': topics}
     return render(request, 'forums/topics.html', context)   

def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = topic.comments.all()
    context = {'topic': topic, 'comments': comments}
    return render(request, 'forums/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner = request.user # установка текущего пользователя как владельца
            topic.save()
            return redirect('forums:topics')
    context = {'form': form}
    return render(request, 'forums/new_topic.html', context)


@login_required
def new_comment(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.approved_comment = True # установить флаг approved_comment в True
            comment.save()
            return HttpResponseRedirect(reverse('forums:topic', args=[topic_id]))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'forums/new_comment.html', context)
