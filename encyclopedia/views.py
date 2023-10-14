from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util
import random

class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'name':'title', 'style': 'display: block;'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'name':'body', 'style': 'display: block; height: 80px; width: 500px;'}))
    
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):    
    content = util.get_entry(name)
    if content is not None:
        content = util.convert_markdown_to_html(content)
        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "content": content
        })
    return render(request, "encyclopedia/error.html", {
        "error_message": f"The requested page '{name}' was not found."
    })


def search(request):
    query = request.POST['query']
      
    return render(request, "encyclopedia/search_result.html", {
        "query": query,
        "results": [entry for entry in util.list_entries() if query.lower() in entry.lower()] 
    })
 
    
def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                return render(request, "encyclopedia/error.html", {
                    "error_message": f"Page with entry title '{title}' already exist."
                })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })       
    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })


def edit_page(request, name):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(name,)))
    content = util.get_entry(name)
    return render(request, "encyclopedia/edit_page.html", {
        "title": name,
        "content": content
    })
 
 
def random_page(request):
    return HttpResponseRedirect(reverse("encyclopedia:entry", args=(random.choice(util.list_entries()),)))