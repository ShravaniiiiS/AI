from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# ==========================================
# SMART TRAVEL CHATBOT RESPONSES
# ==========================================

responses = {

    "hi": "👋 Hey Traveler! Welcome to WanderBot ✨ Ask me about destinations, hotels, beaches, mountains or travel budgets.",

    "hello": "🌍 Ready for your next adventure?",

    "goa": """
🏖️ Goa Travel Plan

📅 Best Time: Nov - Feb
💸 Budget: ₹8,000 - ₹15,000

📍 Places:
• Baga Beach
• Anjuna Beach
• Fort Aguada
• Dudhsagar Falls

🍜 Famous Food:
• Seafood
• Bebinca
• Goan Curry
""",

    "kerala": """
🌴 Kerala Travel Plan

📅 Best Time: Sep - March
💸 Budget: ₹10,000 - ₹20,000

📍 Places:
• Munnar
• Alleppey
• Wayanad
• Kochi

🍛 Famous Food:
• Appam
• Kerala Sadya
""",

    "manali": """
🏔️ Manali Travel Plan

📅 Best Time: Oct - Feb
💸 Budget: ₹12,000+

📍 Places:
• Solang Valley
• Rohtang Pass
• Hidimba Temple

🎯 Activities:
• Snow Sports
• Camping
""",

    "kashmir": """
❄️ Kashmir Trip Guide

📅 Best Time: March - October
💸 Budget: ₹18,000+

📍 Places:
• Gulmarg
• Srinagar
• Dal Lake
• Pahalgam
""",

    "ooty": """
🌿 Ooty Travel Plan

📅 Best Time: Oct - June
💸 Budget: ₹7,000+

📍 Places:
• Ooty Lake
• Tea Estates
• Botanical Garden
""",

    "beach": """
🏖️ Best Beach Destinations

• Goa
• Pondicherry
• Gokarna
• Varkala
• Andaman
""",

    "mountain": """
⛰️ Best Mountain Destinations

• Manali
• Kashmir
• Ladakh
• Ooty
• Munnar
""",

    "honeymoon": """
💕 Honeymoon Destinations

• Kashmir
• Kerala
• Maldives
• Switzerland
• Bali
""",

    "solo": """
🎒 Solo Travel Destinations

• Pondicherry
• Goa
• Kasol
• Hampi
• Rishikesh
""",

    "family": """
👨‍👩‍👧 Family Trip Ideas

• Mysore
• Ooty
• Kerala
• Jaipur
• Coorg
""",

    "budget": """
💸 Budget Travel Tips

• Travel off-season
• Use public transport
• Book early
• Compare hotel prices
""",

    "packing": """
🎒 Packing Essentials

• Power Bank
• Water Bottle
• ID Proof
• First Aid Kit
• Extra Clothes
""",

    "hotel": """
🏨 Hotel Booking Tips

• Check ratings above 4⭐
• Compare prices
• Read reviews carefully
• Book early
""",

    "flight": """
✈️ Flight Booking Tips

• Book early
• Use incognito mode
• Mid-week flights are cheaper
""",

    "adventure": """
🚵 Adventure Trip Ideas

• Ladakh Bike Trip
• River Rafting
• Trekking
• Scuba Diving
""",

    "international": """
🌍 International Destinations

• Dubai
• Bali
• Thailand
• Switzerland
• Singapore
""",

    "motivation": random.choice([
        "✈️ Travel is the best investment.",
        "🌍 Collect memories, not things.",
        "🏖️ Adventure awaits you.",
        "🚞 Life is short. Travel more."
    ])
}

# ==========================================
# BEAUTIFUL HTML UI
# ==========================================

html = '''

<!DOCTYPE html>
<html>

<head>

<title>WanderBot</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    background:linear-gradient(135deg,#faedcd,#f8edeb,#e9edc9,#dbe7e4,#cddafd);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:15px;
}

.container{
    width:92%;
    max-width:1000px;
    height:96vh;

    background:rgba(255,255,255,0.35);
    backdrop-filter:blur(18px);

    border-radius:28px;

    padding:15px;

    display:flex;
    flex-direction:column;

    box-shadow:0px 10px 35px rgba(0,0,0,0.12);
}

.header{
    text-align:center;
    padding:5px 0;
}

.header h1{
    font-size:34px;
    color:#6d597a;
    margin-bottom:2px;
}

.header p{
    color:#7f5539;
    font-size:14px;
}

.chatbox{
    flex:1;

    overflow-y:auto;

    margin-top:10px;

    padding:18px;

    border-radius:24px;

    background:rgba(255,255,255,0.28);

    display:flex;
    flex-direction:column;
}

.user-msg{
    background:linear-gradient(135deg,#ffc8dd,#ffafcc);

    color:#333;

    padding:14px 18px;

    border-radius:20px 20px 5px 20px;

    width:fit-content;

    max-width:75%;

    margin-left:auto;

    margin-top:14px;

    box-shadow:0px 4px 10px rgba(0,0,0,0.08);

    font-size:15px;
}

.bot-msg{
    background:white;

    color:#444;

    padding:16px 20px;

    border-radius:20px 20px 20px 5px;

    width:fit-content;

    max-width:82%;

    margin-top:10px;

    white-space:pre-line;

    line-height:1.7;

    box-shadow:0px 4px 10px rgba(0,0,0,0.08);

    font-size:15px;
}

form{
    display:flex;

    gap:10px;

    margin-top:12px;
}

input{
    flex:1;

    padding:15px;

    border:none;

    border-radius:15px;

    font-size:15px;

    outline:none;

    background:white;

    box-shadow:0px 3px 8px rgba(0,0,0,0.06);
}

button{
    padding:15px 24px;

    border:none;

    border-radius:15px;

    background:linear-gradient(135deg,#a2d2ff,#cdb4db);

    font-weight:600;

    cursor:pointer;

    transition:0.3s;

    font-size:15px;
}

button:hover{
    transform:scale(1.04);
}

.quick{
    margin-top:8px;

    text-align:center;
}

.quick span{
    display:inline-block;

    padding:7px 13px;

    background:rgba(255,255,255,0.55);

    border-radius:14px;

    margin:4px;

    font-size:12px;

    color:#555;
}

::-webkit-scrollbar{
    width:6px;
}

::-webkit-scrollbar-thumb{
    background:#cdb4db;
    border-radius:10px;
}

</style>

</head>

<body>

<div class="container">

<div class="header">
    <h1>🌍 WanderBot</h1>
    <p>Your Smart Travel Planner</p>
</div>

<div class="chatbox">

{% for chat in chats %}

<div class="user-msg">
{{ chat.user }}
</div>

<div class="bot-msg">
{{ chat.bot }}
</div>

{% endfor %}

</div>

<form method="POST">

<input type="text" name="message" placeholder="Ask about trips, beaches, mountains..." required>

<button type="submit">Send</button>

</form>

<div class="quick">
<span>Goa</span>
<span>Kerala</span>
<span>Budget</span>
<span>Hotels</span>
<span>Packing</span>
<span>Solo Trip</span>
<span>Adventure</span>
<span>Flights</span>
<span>Honeymoon</span>
</div>

</div>

</body>
</html>

'''

# ==========================================
# CHAT HISTORY
# ==========================================

chat_history = [
    {
        "user": "Hello",
        "bot": "👋 Welcome to WanderBot! Ask me anything about travel and trips."
    }
]

# ==========================================
# MAIN ROUTE
# ==========================================

@app.route("/", methods=["GET", "POST"])

def home():

    if request.method == "POST":

        user_message = request.form["message"].lower()

        bot_reply = "❌ Sorry, I don't understand. Try asking about Goa, Kerala, hotels, beaches or mountains."

        for key in responses:

            if key in user_message:

                bot_reply = responses[key]
                break

        chat_history.append({
            "user": user_message,
            "bot": bot_reply
        })

    return render_template_string(html, chats=chat_history)

# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
