from django.shortcuts import render

# Create your views here.

# 브라우저 요청 정보를 request 담아 전달
def index(request):
    return render(request, "blog/index.html")

def calc_ui(request):
    return render(request, "blog/calc_ui.html")

def calc_action(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]
    opr = request.GET["opr"]
    result = eval(num1 + opr + num2)
    return render(request, "blog/calc_action.html",
                  {
                      'n1': num1,
                      'n2': num2,
                      'opr': opr,
                      'result': result
                  })