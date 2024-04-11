from django.shortcuts import render

from msngr.models import Conversation


def index(request):
    num_conversations = Conversation.objects.count()

    context = {
        "num_conversations": num_conversations,
    }
    return render(request, "msngr/index.html", context=context)
