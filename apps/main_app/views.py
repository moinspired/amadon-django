from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#Gobal variable
class A:
    subtotal = 0

def index(request):
    return render(request, "main_app/index.html")

def calculate(request):
    print "Calculating---------------------------------------"
    if request.method == "POST":
        print "in post"
        if request.POST["product_id"] == "1015":
            productValue = 19.99
            A.subtotal = float(request.POST['quantity']) * productValue
            if "total" in request.session and "count" in request.session:
                request.session["total"] += A.subtotal
                request.session["count"] += 1
            else:
                request.session["total"] = A.subtotal
                request.session["count"] = 1
            print A.subtotal
            return redirect("/amadon/buy")
        if request.POST["product_id"] == "1016":
            productValue = 29.99
            A.subtotal = float(request.POST['quantity']) * productValue
            print A.subtotal
            if "total" in request.session and "count" in request.session:
                request.session["total"] += A.subtotal
                request.session["count"] += 1
            else:
                request.session["total"] = A.subtotal
                request.session["count"] = 1
            return redirect("/amadon/buy")
        if request.POST["product_id"] == "1017":
            productValue = 4.99
            A.subtotal = float(request.POST['quantity']) * productValue
            if "total" in request.session and "count" in request.session:
                request.session["total"] += A.subtotal
                request.session["count"] += 1
            else:
                request.session["total"] = A.subtotal
                request.session["count"] = 1
        if request.POST["product_id"] == "1018":
            productValue = 49.99
            A.subtotal = float(request.POST['quantity']) * productValue
            if "total" in request.session and "count" in request.session:
                request.session["total"] += A.subtotal
                request.session["count"] += 1
            else:
                request.session["total"] = A.subtotal
                request.session["count"] = 1
            return redirect("/amadon/buy")
    else:
        return render(request, "main_app/info.html", {"subtotal" : A.subtotal})
    return redirect("/amadon/buy")

def summary(request):
    return render(request, "main_app/info.html", {"subtotal" : A.subtotal})