from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'ask.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question_detail', pk=answer.question.pk)
