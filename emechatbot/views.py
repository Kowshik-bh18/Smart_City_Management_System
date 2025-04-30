from django.shortcuts import render
from .forms import ChatForm
from django.conf import settings
from openai import OpenAI

# Initialize the OpenAI client with API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def chatbot_view(request):
    response = ""
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['message']

            # OpenAI API call using new SDK
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an emergency assistant for a smart city. Provide short, helpful responses."},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=100
            )

            response = completion.choices[0].message.content.strip()
    else:
        form = ChatForm()

    return render(request, 'emechatbot/chat.html', {'form': form, 'response': response})
