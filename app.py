from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# ==========================================
# AI SMART TRAVEL PLANNER CHATBOT
# ==========================================

travel_data = {
    "goa": {
        "budget": "₹6,000 - ₹15,000",
        "days": "3-5 Days",
        "places": ["Baga Beach", "Anjuna Beach", "Dudhsagar Falls", "Fort Aguada", "Chapora Fort"],
        "food": ["Goan Fish Curry", "Prawn Fry", "Bebinca Dessert"]
    },

    "kerala": {
        "budget": "₹8,000 - ₹18,000",
        "days": "4-6 Days",
        "places": ["Munnar", "Alleppey", "Wayanad", "Kochi", "Varkala Beach"],
        "food": ["Appam", "Kerala Sadya", "Fish Molee"]
    },

    "manali": {
        "budget": "₹10,000 - ₹20,000",
        "days": "5-7 Days",
        "places": ["Solang Valley", "Rohtang Pass", "Old Manali", "Hidimba Temple"],
        "food": ["Trout Fish", "Siddu", "Tibetan Momos"]
    },

    "pondicherry": {
        "budget": "₹5,000 - ₹12,000",
        "days": "2-4 Days",
        "places": ["Rock Beach", "Auroville", "French Colony", "Paradise Beach"],
        "food": ["French Pastries", "Seafood", "South Indian Meals"]
    },

    "kashmir": {
        "budget": "₹15,000 - ₹30,000",
        "days": "5-8 Days",
        "places": ["Srinagar", "Gulmarg", "Pahalgam", "Dal Lake"],
        "food": ["Rogan Josh", "Kahwa", "Yakhni"]
    },

    "jaipur": {
        "budget": "₹7,000 - ₹14,000",
        "days": "3-5 Days",
        "places": ["Hawa Mahal", "Amber Fort", "City Palace", "Jal Mahal"],
        "food": ["Dal Baati", "Ghewar", "Kachori"]
    },

    "ladakh": {
        "budget": "₹18,000 - ₹40,000",
        "days": "6-10 Days",
        "places": ["Pangong Lake", "Nubra Valley", "Leh Palace", "Magnetic Hill"],
        "food": ["Thukpa", "Momos", "Butter Tea"]
    },

    "ooty": {
        "budget": "₹5,000 - ₹11,000",
        "days": "2-4 Days",
        "places": ["Ooty Lake", "Botanical Garden", "Doddabetta Peak", "Tea Estates"],
        "food": ["Chocolate", "Tea", "South Indian Meals"]
    }
}

# ==========================================
# HTML UI
# ==========================================

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI Travel Planner</title>

    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
            text-align: center;
            padding: 30px;
        }

        .container {
            width: 70%;
            margin: auto;
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        }

        input {
            width: 60%;
            padding: 12px;
            border-radius: 10px;
            border: none;
            font-size: 18px;
        }

        button {
            padding: 12px 25px;
            border: none;
            border-radius: 10px;
            background: orange;
            color: black;
            font-weight: bold;
            cursor: pointer;
            font-size: 18px;
        }

        .result {
            margin-top: 30px;
            text-align: left;
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
        }

        h1 {
            color: orange;
        }

        .highlight {
            color: cyan;
        }

    </style>
</head>

<body>

<div class="container">
    <h1>🌍 AI Smart Travel Planner</h1>

    <form method="POST">
        <input type="text" name="destination" placeholder="Say Hi or Enter Destination" required>
        <button type="submit">Plan Trip</button>
    </form>

    {% if response %}
    <div class="result">
        {{ response|safe }}
    </div>
    {% endif %}
</div>

</body>
</html>
'''

# ==========================================
# AVAILABLE DESTINATIONS
# ==========================================

available_places = ', '.join([place.title() for place in travel_data.keys()])

# ==========================================
# CHATBOT LOGIC
# ==========================================

@app.route('/', methods=['GET', 'POST'])
def home():

    response = ""

    if request.method == 'POST':

        user_input = request.form['destination'].lower()

        if user_input in ['hi', 'hello', 'hey']:

            response = f'''
            <h2 class="highlight">👋 Welcome to AI Travel Planner</h2>

            <p><b>🌍 Available Destinations:</b></p>

            <ul>
                {''.join(f'<li>{place.title()}</li>' for place in travel_data.keys())}
            </ul>

            <p>Type any destination name to get a complete AI trip plan ✈️</p>
            '''

        elif user_input in travel_data:

            data = travel_data[user_input]

            response = f'''
            <h2 class="highlight">✈️ Trip Plan for {user_input.title()}</h2>

            <p><b>💰 Estimated Budget:</b> {data['budget']}</p>

            <p><b>📅 Recommended Duration:</b> {data['days']}</p>

            <p><b>📍 Top Places to Visit:</b></p>
            <ul>
                {''.join(f'<li>{place}</li>' for place in data['places'])}
            </ul>

            <p><b>🍴 Famous Foods:</b></p>
            <ul>
                {''.join(f'<li>{food}</li>' for food in data['food'])}
            </ul>

            <p><b>🤖 AI Suggestion:</b>
            {random.choice([
                'Best for friends trip!',
                'Perfect for photography lovers!',
                'Great choice for budget travel!',
                'Amazing destination for relaxation!'
            ])}
            </p>
            '''

        else:
            response = '''
            <h2 style="color:red;">❌ Destination Not Found</h2>
            <p>Try: Goa, Kerala, Manali, Pondicherry</p>
            '''

    return render_template_string(html, response=response)

# ==========================================
# RUN APP
# ==========================================

if __name__ == '__main__':
    app.run(debug=True)
