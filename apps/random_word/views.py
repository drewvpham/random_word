from django.shortcuts import render, redirect
import string, random

# Create your views here.
def index(request):
    if "attempt_num" not in request.session or "word" not in request.session:
        request.session["attempt_num"] = 0
        request.session["word"] =''
        data={"attempt_num": request.session["attempt_num"], "word": request.session["word"]}
        print data
        return render(request, 'random_word/index.html', data)
    else:
        return render(request, 'random_word/index.html')


def generate(request):
    if request.method=='POST':
        new_word=''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(14))
        request.session["word"]='Your random word is: '+new_word
        request.session["attempt_num"] +=1
        return redirect("/")
    else:
        return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
