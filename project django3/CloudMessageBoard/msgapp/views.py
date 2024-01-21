from django.shortcuts import render
from .models import Message

def submit_message(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        recipient_name = request.POST.get('recipient_name')
        content = request.POST.get('content')

        Message.objects.create(
            sender_name=sender_name,
            recipient_name=recipient_name,
            content=content
        )

    return render(request, 'msgapp/submit_message.html')

def get_messages(request, sender_name):
    messages = Message.objects.filter(sender_name=sender_name).order_by('-timestamp')[:20]
    return render(request, 'msgapp/get_messages.html', {'messages': messages})
