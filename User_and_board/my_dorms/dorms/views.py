from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from .models import Context, Comment
from django.utils import timezone
from .forms import ContextForm, CommentForm

# Create your views here.
def index (request) :
    context_list = Context.objects.all()
    context = {
        'context_list' : context_list
    }
    return render (request, 'dorms/context_list.html', context)

def detail (request, context_id) :
    content = get_object_or_404(Context, pk=context_id)
    comment_list = Comment.objects.filter (context = content)
    context = {
        'content' : content,
        'comment_list' : comment_list
    }
    return render (request, 'dorms/context_detail.html', context)

def comment_create (request, context_id) :
    context = get_object_or_404(Context, pk = context_id)
    comment = Comment(context = context, content = request.POST.get('comment'), writer=request.user, create_date = timezone.now())
    comment.save()
    return redirect("dorms:detail", context_id = context.id)
    # comment_list = Comment.objects.filter(context=context)
    # if request.method == "POST" :
    #     form = CommentForm(request.POST)
    #     if form.is_valid() :
    #         comment = form.save(commit=False)
    #         comment.context = context
    #         comment.writer = 0
    #         comment.create_date = timezone.now()
    #         comment.save()
    #         return redirect('dorms:detail', context_id = context.id)
    # else :
    #     return HttpResponseNotAllowed("only POST is possible")
    # con = {'context' : context, 'comment_list' : comment_list, 'form' : form}
    # return render(request, 'dorms/context_detail.html', con)

def context_create (request) :
    if request.method == 'POST' :
        form = ContextForm(request.POST)
        if form.is_valid() :
            context = form.save(commit=False)
            context.date = timezone.now()
            context.writer = request.user
            context.save()
            return redirect('dorms:index')
    else :
        form = ContextForm()
    context = {'form' : form}
    return render (request, 'dorms/context_form.html', context)