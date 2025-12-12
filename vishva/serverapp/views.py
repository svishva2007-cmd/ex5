from django.shortcuts import render
def rectarea(request):
    context = {'area': 0, 'l': 0, 'b': 0}
    if request.method == 'POST':
        print("POST method is used")
        length_str = request.POST.get('length', '0')
        breadth_str = request.POST.get('breadth', '0')
        print("Request:", request)
        print("Length:", length_str)
        print("Breadth:", breadth_str)
        try:
            length = int(length_str)
            breadth = int(breadth_str)
            area = length * breadth
            context['area'] = area
            context['l'] = length
            context['b'] = breadth
            print("Area:", area)
        except ValueError:
            print("Invalid input for length or breadth")
            context['area'] = "Invalid input"
    return render(request, 'serverapp/server.html', context)