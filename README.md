# Fuzzy-Search-Autocomplete-in-Django
A HTTP service that provides an endpoint for fuzzy search / autocomplete of English words.

A Django based Word Search WebApp This WebApp basically renders a search box on browser where the user can type in a word as an input to search that word in a dataset containing 333,333 English words and the frequency of their usage in some corpus.

Requirements 

1. django (Pip install django)

Frontend. A simple jQuery based HTML template of Search Box with a Search button.

# Running Tests

1.cd autocomplete.<br>
2.Python manage.py runserver

3.API Endpoints. GET http://localhost:8000 This endpoint renders a search box in the browser.


4.GET http://localhost:8000/search/?term=proc This endpoint finally returns a response which is of JSON array containing 25 results, 

Matches occurs anywhere in the string, not just at the beginning. For example, eryx matches archaeopteryx (among others). Matches at the start of a word ranks higher, For example, for the input pract, the result practical ranks higher than impractical. Common words (those with a higher usage count) ranks higher than rare words. Short words ranks higher than long words. For example, given the input environ, the result environment ranks higher than environmentalism. An exact match should always be ranked as the first result.

