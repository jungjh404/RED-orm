from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Context, Comment, Context_info, Comment_info, Context_free, Comment_free, Context_trade, Comment_trade, Comment_copur, Context_copur
from django.utils import timezone
from .forms import ContextForm, CommentForm, ContextInfoForm, CommentInfoForm, ContextFreeForm, CommentFreeForm, CommentTradeForm, ContextTradeForm, ContextCopurForm, CommentCopurForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required(login_url='common:login')
def comment_create (request, context_id) :
    context = get_object_or_404(Context, pk=context_id)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.context = context
            comment.writer = request.user
            comment.create_date = timezone.now()
            comment.save()
            return redirect('dorms:detail', context.id)
    comment_list = Comment.objects.filter(context=context)
    con = {'content' : context, 'comment_list' : comment_list, 'form' : comment_form}
    return render(request, 'dorms/context_detail.html', con)

@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
def context_modify(request, context_id) :
    context = get_object_or_404(Context, pk=context_id)
    if request.user != context.writer :
        messages.error(request, '삭제권한이 없습니다')
        return redirect('dorms:detail', context_id = context.id)
    if request.method == "POST" :
        form = ContextForm(request.POST, instance=context)
        if form.is_valid() :
            context = form.save(commit=False)
            context.modify_date = timezone.now()
            context.save()
            return redirect('dorms:detail', context_id = context.id)
    else :
        form = ContextForm(instance=context)
    content = {'form' : form}
    return render(request, 'dorms/context_form.html', content)

@login_required(login_url='common:login')
def context_delete(request, context_id) :
    context = get_object_or_404(Context, pk=context_id)
    if request.user != context.writer :
        messages.error(request, "수정권한이 없습니다")
        return redirect('dorms:detail', context_id=context.id)

    context.delete()
    return redirect('dorms:index')

@login_required(login_url='common:login')
def comment_modify (request, comment_id) :
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.writer :
        messages.error(request, "수정권한이 없습니다.")
        return redirect ('dorms:detail', context_id = comment.context.id)
    if request.method == 'POST' :
        comment_form = CommentForm(request.POST, instance = comment)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('dorms:detail', context_id = comment.context.id)
    else :
        comment_form = CommentForm(instance = comment)
    context = {'comment' : comment, 'form' : comment_form}
    return render (request, 'dorms/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.user != comment.writer :
        messages.error(request, "삭제권한이 없습니다.")
    else :
        comment.delete()
    return redirect('dorms:detail', context_id = comment.context.id)

def info_index (request) :
    context_list = Context_info.objects.all()
    context = {
        'context_list': context_list
    }
    return render(request, 'dorms/info_context_list.html', context)

def info_detail (request, context_id) :
    content = get_object_or_404(Context_info, pk=context_id)
    comment_list = Comment_info.objects.filter(context=content)
    context = {
        'content': content,
        'comment_list': comment_list
    }
    return render(request, 'dorms/info_context_detail.html', context)

@login_required(login_url='common:login')
def info_comment_create(request, context_id) :
    context = get_object_or_404(Context_info, pk=context_id)
    if request.user.is_authenticated:
        comment_form = CommentInfoForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.context = context
            comment.writer = request.user
            comment.create_date = timezone.now()
            comment.save()
            return redirect('dorms:info_detail', context.id)
    comment_list = Comment_info.objects.filter(context=context)
    con = {'content': context, 'comment_list': comment_list, 'form': comment_form}
    return render(request, 'dorms/info_context_detail.html', con)

@login_required(login_url='common:login')
def info_context_create(request) :
    if request.method == 'POST' :
        form = ContextInfoForm(request.POST)
        if form.is_valid() :
            context = form.save(commit=False)
            context.date = timezone.now()
            context.writer = request.user
            context.save()
            return redirect('dorms:info_index')
    else :
        form = ContextInfoForm()
    context = {'form' : form}
    return render (request, 'dorms/info_context_form.html', context)

@login_required(login_url='common:login')
def info_context_modify(request, context_id) :
    context = get_object_or_404(Context_info, pk=context_id)
    if request.user != context.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dorms:info_detail', context_id=context.id)
    if request.method == "POST":
        form = ContextInfoForm(request.POST, instance=context)
        if form.is_valid():
            context = form.save(commit=False)
            context.modify_date = timezone.now()
            context.save()
            return redirect('dorms:info_detail', context_id=context.id)
    else:
        form = ContextInfoForm(instance=context)
    content = {'form': form}
    return render(request, 'dorms/info_context_form.html', content)

@login_required(login_url='common:login')
def info_context_delete(request, context_id) :
    context = get_object_or_404(Context_info, pk=context_id)
    if request.user != context.writer :
        messages.error(request, "수정권한이 없습니다")
        return redirect('dorms:info_detail', context_id=context.id)

    context.delete()
    return redirect('dorms:info_index')

@login_required(login_url='common:login')
def info_comment_modify (request, comment_id) :
    comment = get_object_or_404(Comment_info, pk=comment_id)
    if request.user != comment.writer :
        messages.error(request, "수정권한이 없습니다.")
        return redirect ('dorms:info_detail', context_id = comment.context.id)
    if request.method == 'POST' :
        comment_form = CommentInfoForm(request.POST, instance = comment)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('dorms:info_detail', context_id = comment.context.id)
    else :
        comment_form = CommentInfoForm(instance = comment)
    context = {'comment' : comment, 'form' : comment_form}
    return render (request, 'dorms/info_comment_form.html', context)

@login_required(login_url='common:login')
def info_comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment_info, pk = comment_id)
    if request.user != comment.writer :
        messages.error(request, "삭제권한이 없습니다.")
    else :
        comment.delete()
    return redirect('dorms:info_detail', context_id = comment.context.id)

def free_index (request) :
    context_list = Context_free.objects.all()
    context = {
        'context_list': context_list
    }
    return render(request, 'dorms/free_context_list.html', context)

def free_detail (request, context_id) :
    content = get_object_or_404(Context_free, pk=context_id)
    comment_list = Comment_free.objects.filter(context=content)
    context = {
        'content': content,
        'comment_list': comment_list
    }
    return render(request, 'dorms/free_context_detail.html', context)

@login_required(login_url='common:login')
def free_comment_create(request, context_id) :
    context = get_object_or_404(Context_free, pk=context_id)
    if request.user.is_authenticated:
        comment_form = CommentFreeForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.context = context
            comment.writer = request.user
            comment.create_date = timezone.now()
            comment.save()
            return redirect('dorms:free_detail', context.id)
    comment_list = Comment_free.objects.filter(context=context)
    con = {'content': context, 'comment_list': comment_list, 'form': comment_form}
    return render(request, 'dorms/free_context_detail.html', con)

@login_required(login_url='common:login')
def free_context_create(request) :
    if request.method == 'POST' :
        form = ContextFreeForm(request.POST)
        if form.is_valid() :
            context = form.save(commit=False)
            context.date = timezone.now()
            context.writer = request.user
            context.save()
            return redirect('dorms:free_index')
    else :
        form = ContextFreeForm()
    context = {'form' : form}
    return render (request, 'dorms/free_context_form.html', context)

@login_required(login_url='common:login')
def free_context_modify(request, context_id) :
    context = get_object_or_404(Context_free, pk=context_id)
    if request.user != context.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dorms:free_detail', context_id=context.id)
    if request.method == "POST":
        form = ContextFreeForm(request.POST, instance=context)
        if form.is_valid():
            context = form.save(commit=False)
            context.modify_date = timezone.now()
            context.save()
            return redirect('dorms:free_detail', context_id=context.id)
    else:
        form = ContextFreeForm(instance=context)
    content = {'form': form}
    return render(request, 'dorms/free_context_form.html', content)

@login_required(login_url='common:login')
def free_context_delete(request, context_id) :
    context = get_object_or_404(Context_free, pk=context_id)
    if request.user != context.writer :
        messages.error(request, "수정권한이 없습니다")
        return redirect('dorms:free_detail', context_id=context.id)

    context.delete()
    return redirect('dorms:free_index')

@login_required(login_url='common:login')
def free_comment_modify (request, comment_id) :
    comment = get_object_or_404(Comment_free, pk=comment_id)
    if request.user != comment.writer :
        messages.error(request, "수정권한이 없습니다.")
        return redirect ('dorms:free_detail', context_id = comment.context.id)
    if request.method == 'POST' :
        comment_form = CommentFreeForm(request.POST, instance = comment)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('dorms:free_detail', context_id = comment.context.id)
    else :
        comment_form = CommentFreeForm(instance = comment)
    context = {'comment' : comment, 'form' : comment_form}
    return render (request, 'dorms/free_comment_form.html', context)

@login_required(login_url='common:login')
def free_comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment_free, pk = comment_id)
    if request.user != comment.writer :
        messages.error(request, "삭제권한이 없습니다.")
    else :
        comment.delete()
    return redirect('dorms:free_detail', context_id = comment.context.id)

def trade_index (request) :
    context_list = Context_trade.objects.all()
    context = {
        'context_list': context_list
    }
    return render(request, 'dorms/trade_context_list.html', context)

def trade_detail (request, context_id) :
    content = get_object_or_404(Context_trade, pk=context_id)
    comment_list = Comment_trade.objects.filter(context=content)
    context = {
        'content': content,
        'comment_list': comment_list
    }
    return render(request, 'dorms/trade_context_detail.html', context)

@login_required(login_url='common:login')
def trade_comment_create(request, context_id) :
    context = get_object_or_404(Context_trade, pk=context_id)
    if request.user.is_authenticated:
        comment_form = CommentTradeForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.context = context
            comment.writer = request.user
            comment.create_date = timezone.now()
            comment.save()
            return redirect('dorms:trade_detail', context.id)
    comment_list = Comment_trade.objects.filter(context=context)
    con = {'content': context, 'comment_list': comment_list, 'form': comment_form}
    return render(request, 'dorms/trade_context_detail.html', con)

@login_required(login_url='common:login')
def trade_context_create(request) :
    if request.method == 'POST' :
        form = ContextTradeForm(request.POST)
        if form.is_valid() :
            context = form.save(commit=False)
            context.date = timezone.now()
            context.writer = request.user
            context.save()
            return redirect('dorms:trade_index')
    else :
        form = ContextTradeForm()
    context = {'form' : form}
    return render (request, 'dorms/trade_context_form.html', context)

@login_required(login_url='common:login')
def trade_context_modify(request, context_id) :
    context = get_object_or_404(Context_trade, pk=context_id)
    if request.user != context.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dorms:trade_detail', context_id=context.id)
    if request.method == "POST":
        form = ContextTradeForm(request.POST, instance=context)
        if form.is_valid():
            context = form.save(commit=False)
            context.modify_date = timezone.now()
            context.save()
            return redirect('dorms:trade_detail', context_id=context.id)
    else:
        form = ContextTradeForm(instance=context)
    content = {'form': form}
    return render(request, 'dorms/trade_context_form.html', content)

@login_required(login_url='common:login')
def trade_context_delete(request, context_id) :
    context = get_object_or_404(Context_trade, pk=context_id)
    if request.user != context.writer :
        messages.error(request, "수정권한이 없습니다")
        return redirect('dorms:trade_detail', context_id=context.id)

    context.delete()
    return redirect('dorms:trade_index')

@login_required(login_url='common:login')
def trade_comment_modify (request, comment_id) :
    comment = get_object_or_404(Comment_trade, pk=comment_id)
    if request.user != comment.writer :
        messages.error(request, "수정권한이 없습니다.")
        return redirect ('dorms:trade_detail', context_id = comment.context.id)
    if request.method == 'POST' :
        comment_form = CommentTradeForm(request.POST, instance = comment)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('dorms:trade_detail', context_id = comment.context.id)
    else :
        comment_form = CommentTradeForm(instance = comment)
    context = {'comment' : comment, 'form' : comment_form}
    return render (request, 'dorms/trade_comment_form.html', context)

@login_required(login_url='common:login')
def trade_comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment_trade, pk = comment_id)
    if request.user != comment.writer :
        messages.error(request, "삭제권한이 없습니다.")
    else :
        comment.delete()
    return redirect('dorms:trade_detail', context_id = comment.context.id)

def copurchase_index (request) :
    context_list = Context_copur.objects.all()
    context = {
        'context_list': context_list
    }
    return render(request, 'dorms/copurchase_context_list.html', context)

def copurchase_detail (request, context_id) :
    content = get_object_or_404(Context_copur, pk=context_id)
    comment_list = Comment_copur.objects.filter(context=content)
    context = {
        'content': content,
        'comment_list': comment_list
    }
    return render(request, 'dorms/copurchase_context_detail.html', context)

@login_required(login_url='common:login')
def copurchase_comment_create(request, context_id) :
    context = get_object_or_404(Context_copur, pk=context_id)
    if request.user.is_authenticated:
        comment_form = CommentCopurForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.context = context
            comment.writer = request.user
            comment.create_date = timezone.now()
            comment.save()
            return redirect('dorms:copurchase_detail', context.id)
    comment_list = Comment_copur.objects.filter(context=context)
    con = {'content': context, 'comment_list': comment_list, 'form': comment_form}
    return render(request, 'dorms/copurchase_context_detail.html', con)

@login_required(login_url='common:login')
def copurchase_context_create(request) :
    if request.method == 'POST' :
        form = ContextCopurForm(request.POST)
        if form.is_valid() :
            context = form.save(commit=False)
            context.date = timezone.now()
            context.writer = request.user
            context.save()
            return redirect('dorms:copurchase_index')
    else :
        form = ContextCopurForm()
    context = {'form' : form}
    return render (request, 'dorms/copurchase_context_form.html', context)

@login_required(login_url='common:login')
def copurchase_context_modify(request, context_id) :
    context = get_object_or_404(Context_copur, pk=context_id)
    if request.user != context.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dorms:copurchase_detail', context_id=context.id)
    if request.method == "POST":
        form = ContextCopurForm(request.POST, instance=context)
        if form.is_valid():
            context = form.save(commit=False)
            context.modify_date = timezone.now()
            context.save()
            return redirect('dorms:copurchase_detail', context_id=context.id)
    else:
        form = ContextCopurForm(instance=context)
    content = {'form': form}
    return render(request, 'dorms/copurchase_context_form.html', content)

@login_required(login_url='common:login')
def copurchase_context_delete(request, context_id) :
    context = get_object_or_404(Context_copur, pk=context_id)
    if request.user != context.writer :
        messages.error(request, "수정권한이 없습니다")
        return redirect('dorms:copurchase_detail', context_id=context.id)

    context.delete()
    return redirect('dorms:copurchase_index')

@login_required(login_url='common:login')
def copurchase_comment_modify (request, comment_id) :
    comment = get_object_or_404(Comment_copur, pk=comment_id)
    if request.user != comment.writer :
        messages.error(request, "수정권한이 없습니다.")
        return redirect ('dorms:copurchase_detail', context_id = comment.context.id)
    if request.method == 'POST' :
        comment_form = CommentCopurForm(request.POST, instance = comment)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('dorms:copurchase_detail', context_id = comment.context.id)
    else :
        comment_form = CommentCopurForm(instance = comment)
    context = {'comment' : comment, 'form' : comment_form}
    return render (request, 'dorms/copur_comment_form.html', context)

@login_required(login_url='common:login')
def copurchase_comment_delete(request, comment_id) :
    comment = get_object_or_404(Comment_copur, pk = comment_id)
    if request.user != comment.writer :
        messages.error(request, "삭제권한이 없습니다.")
    else :
        comment.delete()
    return redirect('dorms:copurchase_detail', context_id = comment.context.id)