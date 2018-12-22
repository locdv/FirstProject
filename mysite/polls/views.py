""" Các view hiển thị cơ bản cho polls
    index: hiển thị 5 question gần nhất
    detail: hiển thị nội dung question cho phép người dùng lựa chọn câu trả lời
    results: hiển thị kết quả vote của question
    vote: xử lý hành động vote của người dùng đối với một question
"""
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def results(request, question_id):
    """
    get question đối tượng bởi id
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        """
        kiểm tra choice người dùng đã lựa chọn
        nếu người dùng không lựa chọn sẽ hiển thị thông báo
        hiển thị màn hình detail
        """
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        # lưu xuống database
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))