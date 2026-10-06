'''from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("=== AI PLAN MY TRIP ===")

destination = input("Enter destination: ")
days = int(input("Enter number of days: "))
budget = float(input("Enter total budget: ₹"))
preference = input("Enter preference (history/nature/shopping/food): ")

travel = budget * 0.20
stay = budget * 0.30
food = budget * 0.20
activities = budget * 0.30

prompt = f"""
Plan a {days}-day trip to {destination}.
Total budget is ₹{budget}.
The user's preference is {preference}.

Give a simple day-wise itinerary with:
Morning activity,
Afternoon activity,
Evening activity,
Food suggestion,
and useful travel tips.
Keep it budget-friendly.
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\n=== AI GENERATED ITINERARY ===")
print(response.output_text)

print("\n=== BUDGET PLAN ===")
print("Travel: ₹", round(travel, 2))
print("Accommodation: ₹", round(stay, 2))
print("Food: ₹", round(food, 2))
print("Activities: ₹", round(activities, 2))

print("\nTrip planned successfully!")'''



from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan_trip():

    data = request.json

    destination = data["destination"]
    days = int(data["days"])
    budget = float(data["budget"])
    preference = data["preference"]

    travel = budget * 0.20
    stay = budget * 0.30
    food = budget * 0.20
    activities = budget * 0.30

    prompt = f"""
    Create a budget-friendly {days}-day trip itinerary for {destination}.

    Total budget: ₹{budget}
    Travel preference: {preference}

    Give:
    - Day-wise itinerary
    - Morning activity
    - Afternoon activity
    - Evening activity
    - Food suggestion
    - Travel tips

    Keep the plan simple and suitable for the given budget.
    """

    response = client.responses.create(
        model="llama3.2",
        input=prompt
    )

    return jsonify({
        "itinerary": response.output_text,
        "travel": round(travel, 2),
        "stay": round(stay, 2),
        "food": round(food, 2),
        "activities": round(activities, 2)
    })


if __name__ == "__main__":
    app.run(debug=True) 


