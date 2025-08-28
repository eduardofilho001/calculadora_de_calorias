from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def resultado(request):
    if request.method == "POST":
        form = request.POST
        if form.is_valida():
            form.cleanned_data["comida"]
            
        #if form == ""
        
        Calorias = None
        Carboidratos = None
        Proteinas= None
        Gorduras= None
        Alcool= None
    
    #Calorias=(Carboidratos * 4)+(Proteinas * 4)+(Gorduras * 9)+(Alcool * 7)
    
        return render(request, "resultado.html")
    return render(request, "resultado.html")