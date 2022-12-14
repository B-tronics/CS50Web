from django.shortcuts import render
from django.http import Http404, HttpResponse
import markdown2
from random import choice

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)

    if content is None:
        raise Http404()
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(markdown2.markdown(content)),
            "title": title
        })

def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        if util.get_entry(query):
            return entry(request, query)
        else:
            all_entry = util.list_entries()
            sub_entries = util.filter_query(all_entry, query)
            return render(request, "encyclopedia/search.html", {
                'entries': sub_entries
            })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == 'POST':
        return save_page(request, False)
    else:
        return render(request, "encyclopedia/newpage.html")

def edit(request, entry):
    content = util.get_entry(entry)
    if request.method == 'POST':
       return save_page(request, True)
    return render(request, "encyclopedia/edit.html", {
        "content": content,
        "title": entry
    })

def random(request):
    all_entry = util.list_entries()
    return entry(request, choice(all_entry))

def save_page(request: object, edit: bool):
    all_entry = util.list_entries()
    title = request.POST["title"]
    if (title in all_entry) and not edit:
        return render(request, "encyclopedia/newpage.html", {
            "name_exists": True
        })
    else:
        content = request.POST["content"]
        util.save_entry(title, content)
        return entry(request, title)


def page_not_found_error_handler(request, exception=None):
    return HttpResponse(render(request, "encyclopedia/404.html"), status=404)
