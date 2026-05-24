from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# SALON RESPONSES
responses = {

    "haircut": [
        "Haircut starts from ₹299.",
        "We offer stylish haircuts from ₹299."
    ],

    "facial": [
        "We provide Gold, Fruit and Hydra facials.",
        "Facial packages start from ₹799."
    ],

    "bridal": [
        "Yes, bridal makeup services are available.",
        "Our bridal package starts from ₹7999."
    ],

    "timing": [
        "Salon timings are 10 AM to 8 PM."
    ],

    "location": [
        "We are located at MG Road, Bangalore."
    ],

    "contact": [
        "You can contact us at 9876543210."
    ],

    "hair spa": [
        "Hair spa starts from ₹999."
    ],

    "color": [
        "Hair coloring services are available."
    ]
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot():

    user_message = request.json["message"].lower()

    reply = "Sorry, please contact salon for more details."

    for key in responses:

        if key in user_message:
            reply = random.choice(responses[key])
            break

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)