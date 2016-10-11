from django.shortcuts import render


def drop_down(num_input, num_input2, choice):
        if choice == "Add":
            return int(num_input) + int(num_input2)
        elif choice == "Subtract":
            return int(num_input) - int(num_input2)
        elif choice == "Multiply":
            return int(num_input) * int(num_input2)
        elif choice == "Divide":
            return int(num_input) / int(num_input2)


def index_view(request):
    # print(request.POST)
    if request.GET:
        num_input = request.GET["num_input"]
        num_input2 = request.GET["num_input2"]
        operator = request.GET["operator"]
        print(request.GET)
    else:
        num_input = 1
        num_input2 = 1
        operator = "Add"
    context = {
        "output": drop_down(num_input, num_input2, operator)
    }
    return render(request, "index.html", context)
