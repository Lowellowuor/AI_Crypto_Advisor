# crypto_advisor.py

import requests
import time
from textblob import TextBlob
import re # Regular expressions for basic pattern matching
import random # For random choice if multiple options

# --- Configuration & Mock Data (Replace with API calls in real deployment) ---

# Your CoinGecko Pro API Key (placeholder - GET YOUR OWN!)
# You would need to sign up for a CoinGecko Pro API key for real-time, robust data.
# For demonstration, we'll use a mock API response.
COINGECKO_PRO_API_KEY = "YOUR_COINGECKO_PRO_API_KEY_HERE" # Get this from CoinGecko Developer Dashboard

# --- MOCK Cryptocurrency Intelligence Database ---
# In a real system, this data would be dynamically updated from various sources
# including your ML models for price trends and sustainability research.
crypto_intelligence_db = {
    "bitcoin": {
        "full_name": "Bitcoin (BTC)",
        "price_trend": "bullish", # Derived from ML models analyzing historical data, market sentiment etc.
        "market_capitalization": "large_cap",
        "energy_consumption_footprint": "high_intensity", # e.g., kWh per transaction/block. Based on research.
        "sustainability_index": 0.30, # Quantified metric (0-1) based on research into PoW vs PoS, energy sources.
        "volatility_rating": "medium", # Derived from historical price fluctuations.
        "adoption_score": 0.95, # Based on network activity, institutional adoption, user base.
        "description": "The original cryptocurrency, often seen as digital gold."
    },
    "ethereum": {
        "full_name": "Ethereum (ETH)",
        "price_trend": "stable_growth", # Post-merge trend.
        "market_capitalization": "large_cap",
        "energy_consumption_footprint": "low_intensity", # Significantly reduced after 'The Merge' (PoS).
        "sustainability_index": 0.75, # Improved due to PoS.
        "volatility_rating": "medium",
        "adoption_score": 0.85,
        "description": "A decentralized platform for smart contracts and decentralized applications."
    },
    
"cardano": {
    "full_name": "Cardano (ADA)",
    "price_trend": "emerging_growth",
    "market_capitalization": "mid_cap",
    "energy_consumption_footprint": "minimal_intensity", # Designed with PoS from the start.
    "sustainability_index": 0.90, # High due to design philosophy and energy efficiency.
    "volatility_rating": "high",
    "adoption_score": 0.45,
    "description": "A blockchain platform for changemakers, innovators, and visionaries, built on peer-reviewed research."
},
    "solana": {
        "full_name": "Solana (SOL)",
        "price_trend": "bullish",
        "market_capitalization": "large_cap",
        "energy_consumption_footprint": "low_intensity",
        "sustainability_index": 0.65,
        "volatility_rating": "high",
        "adoption_score": 0.60,
        "description": "A high-performance blockchain supporting thousands of transactions per second."
    },
    "polkadot": {
        "full_name": "Polkadot (DOT)",
        "price_trend": "stable_growth",
        "market_capitalization": "mid_cap",
        "energy_consumption_footprint": "low_intensity",
        "sustainability_index": 0.80,
        "volatility_rating": "medium",
        "adoption_score": 0.40,
        "description": "A multi-chain framework that allows different blockchains to transfer messages and value in a trust-free fashion."
    }
}

# --- Real-Time Market Data Simulation ---
# In a real system, this would come from a live API.
# For this example, we'll return fixed or slightly varied mock data.
def get_realtime_market_data(crypto_id):
    """
    Simulates fetching real-time market data.
    In a real application, this would use the CoinGecko Pro API.
    """
    print(f" (Fetching live data for {crypto_id}...)") # Simulate API call delay
    # Example API call structure (you'd replace with actual requests.get())
    # url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd&x_cg_pro_api_key={COINGECKO_PRO_API_KEY}"
    # response = requests.get(url).json()
    # current_price = response.get(crypto_id, {}).get('usd')

    # Mock data for demonstration
    mock_prices = {
        "bitcoin": 68000 + random.randint(-500, 500),
        "ethereum": 3500 + random.randint(-50, 50),
        "cardano": 0.45 + random.uniform(-0.01, 0.01),
        "solana": 160 + random.randint(-5, 5),
        "polkadot": 7 + random.uniform(-0.1, 0.1)
    }
    
    return {"current_price_usd": mock_prices.get(crypto_id, 0.0)}

# --- NLP & Intent Recognition (Simplified) ---

def process_natural_language(user_input):
    """
    Analyzes user input for sentiment and investment intent.
    """
    blob = TextBlob(user_input.lower())
    
    intent = "unknown"
    risk_tolerance = "medium" # Default
    investment_horizon = "short_term" # Default

    # Detect primary intent
    if any(keyword in blob.words for keyword in ["sustainable", "green", "eco"]):
        intent = "sustainable_investment"
    elif any(keyword in blob.words for keyword in ["profit", "grow", "returns", "money"]):
        intent = "profit_driven"
    elif any(keyword in blob.words for keyword in ["safe", "low risk", "stable"]):
        intent = "low_risk"
    elif any(keyword in blob.words for keyword in ["best", "recommend", "advice"]):
        intent = "general_recommendation"
        
    # Detect risk tolerance
    if any(keyword in blob.words for keyword in ["low risk", "safe"]):
        risk_tolerance = "low"
    elif any(keyword in blob.words for keyword in ["high risk", "aggressive"]):
        risk_tolerance = "high"
    # Else remains "medium"

    # Detect investment horizon
    if any(keyword in blob.words for keyword in ["long-term", "long term", "years"]):
        investment_horizon = "long_term"
    elif any(keyword in blob.words for keyword in ["short-term", "short term", "weeks", "quick"]):
        investment_horizon = "short_term"
    # Else remains "short_term"
        
    return {"sentiment": blob.sentiment.polarity, "intent": intent, "risk_tolerance": risk_tolerance, "investment_horizon": investment_horizon}

# --- Intelligent Decision Logic Framework ---

def optimize_for_sustainability(cryptos, risk_tolerance, investment_horizon):
    """
    Ranks cryptocurrencies for sustainability, then filters by risk/horizon.
    """
    sustainable_options = []
    for crypto_id, data in cryptos.items():
        if data["energy_consumption_footprint"] == "low_intensity" or data["energy_consumption_footprint"] == "minimal_intensity":
            if data["sustainability_index"] > 0.60: # Threshold for 'good' sustainability
                sustainable_options.append((crypto_id, data["sustainability_index"], data))
    
    # Sort by sustainability (descending)
    sustainable_options.sort(key=lambda x: x[1], reverse=True)

    # Filter based on risk tolerance (simplified)
    filtered_options = []
    for crypto_id, _, data in sustainable_options:
        if risk_tolerance == "low" and data["volatility_rating"] in ["medium", "high"]:
            continue # Skip high volatility for low risk
        if investment_horizon == "short_term" and data["price_trend"] not in ["bullish", "stable_growth"]:
            continue # Skip if not quick growth for short term
        filtered_options.append(data)
        
    return filtered_options[0] if filtered_options else None # Return the best option

def optimize_for_returns(cryptos, risk_tolerance, investment_horizon):
    """
    Ranks cryptocurrencies for profitability, then filters by risk/horizon.
    """
    profit_options = []
    for crypto_id, data in cryptos.items():
        # Simple scoring based on trends and market cap for profitability
        score = 0
        if data["price_trend"] == "bullish":
            score += 3
        elif data["price_trend"] == "stable_growth":
            score += 2
        
        if data["market_capitalization"] == "large_cap":
            score += 2
        elif data["market_capitalization"] == "mid_cap":
            score += 1
        
        profit_options.append((crypto_id, score, data))
        
    # Sort by profit score (descending)
    profit_options.sort(key=lambda x: x[1], reverse=True)

    # Filter based on risk tolerance (simplified)
    filtered_options = []
    for crypto_id, _, data in profit_options:
        if risk_tolerance == "low" and data["volatility_rating"] == "high":
            continue # Skip high volatility for low risk
        if investment_horizon == "long_term" and data["price_trend"] == "emerging_growth":
            continue # Prioritize more established for long term
        filtered_options.append(data)
        
    return filtered_options[0] if filtered_options else None

def balance_all_metrics(cryptos, risk_tolerance, investment_horizon):
    """
    Composite scoring to balance profitability, sustainability, and risk.
    """
    balanced_options = []
    for crypto_id, data in cryptos.items():
        score = 0
        
        # Profitability
        if data["price_trend"] == "bullish": score += 3
        elif data["price_trend"] == "stable_growth": score += 2
        if data["market_capitalization"] == "large_cap": score += 2
        
        # Sustainability
        if data["energy_consumption_footprint"] == "minimal_intensity": score += 3
        elif data["energy_consumption_footprint"] == "low_intensity": score += 2
        score += data["sustainability_index"] * 3 # Weigh sustainability index
        
        # Risk (inverse proportionality - higher volatility reduces score for balanced)
        if risk_tolerance == "low":
            if data["volatility_rating"] == "high": score -= 3
            elif data["volatility_rating"] == "medium": score -= 1
        elif risk_tolerance == "high": # High risk users might get bonus for high volatility
            if data["volatility_rating"] == "high": score += 1

        balanced_options.append((crypto_id, score, data))
        
    balanced_options.sort(key=lambda x: x[1], reverse=True)
    
    return balanced_options[0][2] if balanced_options else None

def generate_investment_recommendation(user_input, risk_tolerance, investment_horizon):
    """
    Main recommendation engine.
    """
    intent_data = process_natural_language(user_input)
    intent = intent_data['intent']
    
    # Use user-specified risk/horizon if provided, else default to detected intent
    if risk_tolerance is None:
        risk_tolerance = intent_data['risk_tolerance']
    if investment_horizon is None:
        investment_horizon = intent_data['investment_horizon']

    recommendation = None
    confidence_score = random.randint(80, 95) # Mock confidence score

    if intent == "sustainable_investment":
        recommendation = optimize_for_sustainability(crypto_intelligence_db, risk_tolerance, investment_horizon)
        if recommendation:
            current_price = get_realtime_market_data(recommendation['full_name'].split(' ')[0].lower())
            return (
                f"Based on comprehensive analysis of market trends and sustainability metrics, "
                f"{recommendation['full_name']} presents an optimal balance:\n\n"
                f"📈 Growth Potential: {recommendation['price_trend'].replace('_', ' ').capitalize()} trend with strong technological fundamentals.\n"
                f"🌿 Sustainability Score: {int(recommendation['sustainability_index']*100)}/100 - Industry-leading energy efficiency.\n"
                f"⚖️ Risk Profile: {recommendation['volatility_rating'].capitalize()} volatility with substantial long-term potential.\n"
                f"💰 Current Price: ${current_price.get('current_price_usd', 'N/A'):,.4f}\n\n"
                f"Recommendation Confidence: {confidence_score}%\n"
                f"*This analysis is for informational purposes only - please conduct additional research before making investment decisions*"
            )
    elif intent == "profit_driven" or intent == "general_recommendation" or intent == "low_risk": # Low risk often implies stable returns
        recommendation = optimize_for_returns(crypto_intelligence_db, risk_tolerance, investment_horizon)
        if recommendation:
            current_price = get_realtime_market_data(recommendation['full_name'].split(' ')[0].lower())
            return (
                f"For strategic profitability and long-term growth, consider {recommendation['full_name']}:\n\n"
                f"📈 Growth Potential: {recommendation['price_trend'].replace('_', ' ').capitalize()} trend, ideal for {investment_horizon} strategy.\n"
                f"🔗 Adoption Score: {int(recommendation['adoption_score']*100)}/100 - High market acceptance.\n"
                f"⚖️ Risk Profile: {recommendation['volatility_rating'].capitalize()} volatility, balanced with strong market position.\n"
                f"💰 Current Price: ${current_price.get('current_price_usd', 'N/A'):,.4f}\n\n"
                f"Recommendation Confidence: {confidence_score}%\n"
                f"*Strategic choice: Historical data indicates strong profitability trends. This analysis is for informational purposes only - please conduct additional research before making investment decisions*"
            )
    
    # Fallback to balanced if specific intent not strongly matched or no optimal option found
    if recommendation is None:
        recommendation = balance_all_metrics(crypto_intelligence_db, risk_tolerance, investment_horizon)
        if recommendation:
            current_price = get_realtime_market_data(recommendation['full_name'].split(' ')[0].lower())
            return (
                f"For a balanced approach combining growth potential, sustainability, and manageable risk, "
                f"consider {recommendation['full_name']}:\n\n"
                f"📈 Growth Potential: {recommendation['price_trend'].replace('_', ' ').capitalize()} trend.\n"
                f"🌿 Sustainability Note: {recommendation['energy_consumption_footprint'].replace('_', ' ').capitalize()} energy footprint with a sustainability index of {int(recommendation['sustainability_index']*100)}/100.\n"
                f"⚖️ Risk Profile: {recommendation['volatility_rating'].capitalize()} volatility.\n"
                f"💰 Current Price: ${current_price.get('current_price_usd', 'N/A'):,.4f}\n\n"
                f"Recommendation Confidence: {confidence_score}%\n"
                f"*This analysis is for informational purposes only - please conduct additional research before making investment decisions*"
            )
            
    return "I'm sorry, I couldn't find a suitable recommendation based on your specific criteria at this moment. Please try rephrasing your request or provide more details."

# --- User Experience & Interaction Design (CLI Chatbot) ---

def start_advisor():
    """
    Initiates the AI Cryptocurrency Investment Advisory System CLI chatbot.
    """
    print("-------------------------------------------------------------------")
    print("     Welcome to CryptoAdvisor Pro: Your AI Financial Sidekick!    ")
    print("-------------------------------------------------------------------")
    print("I can help you with cryptocurrency investment recommendations.")
    print("Tell me about your goals (e.g., 'sustainable investment', 'maximize profit', 'low risk long-term').")
    print("Type 'exit' or 'quit' to end the session.")
    print("-------------------------------------------------------------------")

    while True:
        user_input = input("\n> You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("CryptoAdvisor Pro: Thank you for using CryptoAdvisor Pro. Happy investing!")
            break

        # Basic parsing for risk tolerance and investment horizon from direct questions
        # This is a simplification; a full NLP would be more robust.
        risk_tolerance_input = None
        if "low risk" in user_input.lower():
            risk_tolerance_input = "low"
        elif "high risk" in user_input.lower() or "aggressive" in user_input.lower():
            risk_tolerance_input = "high"
        
        investment_horizon_input = None
        if "long term" in user_input.lower() or "long-term" in user_input.lower():
            investment_horizon_input = "long_term"
        elif "short term" in user_input.lower() or "short-term" in user_input.lower():
            investment_horizon_input = "short_term"


        response = generate_investment_recommendation(user_input, risk_tolerance_input, investment_horizon_input)
        print("\n> CryptoAdvisor Pro:", response)

# --- Main Execution ---
if __name__ == "__main__":
    start_advisor()