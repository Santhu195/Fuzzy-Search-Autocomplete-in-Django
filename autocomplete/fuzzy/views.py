from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search, sort 
import json

#renders the search page.
def search_view(request):
    return render(request, 'search.html', {})

#autocompletes results while the user types in a letter.(ui update is done in simple jquery)
def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sort(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)

# Returns a json response having the search results(25 words) containing the searched word(partial)
def SearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')         # for example, query = 'say'
        if query:
            search_result= search(query.lower())
            searchResult_final = sort(search_result, query.lower())
            if len(searchResult_final) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchResult_final})
        else:
            return redirect('/')
