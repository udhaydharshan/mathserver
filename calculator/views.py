from django.shortcuts import render


def calculate_power(request):
    result = None

    if request.method == "POST":
        intensity = float(request.POST.get("intensity"))
        resistance = float(request.POST.get("resistance"))

        result = (intensity ** 2) * resistance  # P = I²R

    return render(request, 'power.html', {"result": result})
