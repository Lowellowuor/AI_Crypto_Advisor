# import necessary libraries
# pip install textblob
# pip install pipenv
# pip install
# pip install python-dotenv
# import necessary libraries

from textblob import TextBlob

def process_natural_language(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    
    intent = 'general'
    risk_tolerance = 'medium'
    horizon = 'medium'

    if 'invest' in user_input.lower():
        intent = 'investing'
    elif 'learn' in user_input.lower() or 'information' in user_input.lower():
        intent = 'learning'

    lowered = user_input.lower()
    if 'low risk' in lowered or 'conservative' in lowered:
        risk_tolerance = 'low'
    elif 'high risk' in lowered or 'aggressive' in lowered:
        risk_tolerance = 'high'

    if 'long-term' in lowered or 'long term' in lowered:
        horizon = 'long'
    elif 'short-term' in lowered or 'short term' in lowered:
        horizon = 'short'

    return {
        'sentiment': sentiment,
        'intent': intent,
        'risk_tolerance': risk_tolerance,
        'investment_horizon': horizon
    }


# Test examples
# --------------------------

examples = [
    "I'm looking to invest in a high-risk coin for short-term gain.",
    "I want to learn more about low-risk sustainable crypto.",
    "Give me information on long-term investment in Ethereum.",
    "Tell me which crypto to choose with conservative strategy."
]

for i, text in enumerate(examples, 1):
    print(f"\nExample {i}: {text}")
    result = process_natural_language(text)
    print("Analysis:", result)


