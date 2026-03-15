"""
**Chatbot**
"""

# Install if needed
!pip install openai gradio

import os
from openai import OpenAI
import gradio as gr


os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
client = OpenAI()

# 💬 Function to get model response
def get_completion(messages, model="gpt-4.1-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,  # Good for conversational tone
    )
    return response.choices[0].message.content


#  System Role (Chatbot Brain)
context = [
    {
        'role': 'system',
        'content': """
You are MobileWellBot, a digital wellbeing assistant.

Your role:
- Help users understand their mobile usage habits.
- Analyze screen time and app usage if provided.
- Identify productivity vs distraction patterns.
- Provide practical advice to reduce excessive phone use.
- Be supportive, professional, and encouraging.
- Keep answers clear and concise.
"""
    }
]

# Chat Function
def collect_messages(user_input, history):
    context.append({'role': 'user', 'content': user_input})
    response = get_completion(context)
    context.append({'role': 'assistant', 'content': response})
    return response


#  Gradio Interface
demo = gr.ChatInterface(
    fn=collect_messages,
    examples=[
        "I spend 6 hours daily on Instagram. Is that unhealthy?",
        "How can I reduce my screen time?",
        "Here is my usage: Instagram 3h, TikTok 2h, Notes 1h. What does this say about me?"
    ],
    title="📱 Mobile Usage Digital Wellbeing Chatbot",
    description="Ask questions about your mobile usage and get personalized digital wellbeing advice."
)

demo.launch()



"""
**HTML**
"""

from openai import OpenAI
from IPython.display import display, HTML
import os

# Use your existing API key
client = OpenAI()

#  Sample mobile usage data
usage_data = """
Total Screen Time: 7 hours
Instagram: 3 hours
TikTok: 2 hours
YouTube: 1 hour
Notes: 0.5 hours
Calendar: 0.5 hours
"""

#HTML Generation Prompt
prompt = f"""
You are a web designer.

Generate a clean and modern HTML dashboard to display the following mobile usage statistics.

Requirements:
- Use only HTML and inline CSS.
- Include a title: "Mobile Usage Dashboard"
- Display total screen time clearly.
- Show app usage in a styled table.
- Use Dark Bleu colors and simple Grey layout.
- Output HTML code only. No explanations.

Mobile Usage Data:
{usage_data}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    temperature=0.3,   # Lower temperature for structured output
    max_output_tokens=800
)

# Render the HTML in Colab
display(HTML(response.output_text))



"""
**Prompt Chaining**
"""

import gradio as gr
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def chained_demo(user_input_data):
    # -------------------------------
    # Step 1: User Behavior Analysis
    # -------------------------------
    prompt1 = f"""
Analyze the mobile usage data below.
Classify the user as either:
- Productivity-focused (uses apps mostly for work, learning, planning)
- Entertainment-focused (uses apps mostly for social media, games, or videos)

Consider the amount of time spent on each app.
Provide ONLY the classification and a short reason.

Examples:
- Instagram: 1h, Notes: 3h → Productivity-focused (focus on productive apps)
- TikTok: 3h, YouTube: 2h → Entertainment-focused (mostly social media/video)

User Data:
{user_input_data}
"""

    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt1}],
        temperature=0.6,  # Slightly higher for variety
        max_tokens=120
    )
    classification = response1.choices[0].message.content.strip()

    # -------------------------------
    # Step 2: Personalized Recommendations
    # -------------------------------
    prompt2 = f"""
The user has been classified as: {classification}

Based on this classification, provide 3 actionable recommendations to improve digital wellbeing.
Format the recommendations as a numbered list. Do not include any other text.
"""

    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt2}],
        temperature=0.7,
        max_tokens=200
    )
    recommendations = response2.choices[0].message.content.strip()

    # -------------------------------
    # Return combined result
    # -------------------------------
    return f"User Classification:\n{classification}\n\nRecommendations:\n{recommendations}"

# -------------------------------
# Gradio Interface
# -------------------------------
demo = gr.Interface(
    fn=chained_demo,
    inputs=gr.Textbox(
        lines=8,
        placeholder="Enter mobile usage data here...\nExample:\nInstagram: 3 hours\nTikTok: 2 hours\nNotes: 0.5 hours"
    ),
    outputs=gr.Textbox(
        lines=10
    ),
    title="Prompt Chaining Demo: Personalized Mobile Usage"
)

demo.launch()



"""
**Few-Shot Prompting**. Emotional Response to Screen Time Feedback
"""

# Example user comment
user_comment = "I feel stressed when I see how much time I spend on social media."

# Few-Shot Prompt
prompt = f"""
You are a sentiment classifier specialized in mobile usage behavior.

Classify the emotional tone of the user's reflection as:
Positive
Neutral
Negative

Only output one word: Positive, Neutral, or Negative.

Examples:

Comment: "I reduced my screen time this week and I feel more productive."
Sentiment: Positive

Comment: "My screen time stayed the same as usual."
Sentiment: Neutral

Comment: "I feel stressed when I see how much time I spend on social media."
Sentiment: Negative

Now classify the following comment:

Comment: "{user_comment}"
Sentiment:
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    temperature=0.2,  # Low temperature for consistent classification
    max_output_tokens=16 # Changed from 10 to 16 to meet the minimum requirement
)

print("User Comment:", user_comment)
print("Predicted Sentiment:", response.output_text.strip())


