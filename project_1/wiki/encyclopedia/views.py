from django.shortcuts import render
from django.http import Http404, HttpResponse
import markdown2

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
            "entry": markdown2.markdown(markdown2.markdown(content))
        })


def page_not_found_error_handler(request, exception=None):
    return HttpResponse(render(request, "encyclopedia/404.html"), status=404)
