print("=== PLAN MY TRIP ===")

destination = input("Enter destination: ")
days = int(input("Enter number of days: "))
budget = float(input("Enter total budget: ₹"))

daily = budget / days

travel = budget * 0.20
stay = budget * 0.30
food = budget * 0.20
activities = budget * 0.30

print("\n--- TRIP SUMMARY ---")
print("Destination:", destination)
print("Days:", days)
print("Total Budget: ₹", budget)
print("Daily Budget: ₹", round(daily, 2))

print("\n--- BUDGET PLAN ---")
print("Travel: ₹", round(travel, 2))
print("Accommodation: ₹", round(stay, 2))
print("Food: ₹", round(food, 2))
print("Activities: ₹", round(activities, 2))

print("\n--- ITINERARY ---")

for day in range(1, days + 1):
    print("\nDay", day)
    print("Morning  : Local sightseeing")
    print("Afternoon: Lunch and tourist attraction")
    print("Evening  : Shopping / leisure")
    print("Night    : Dinner and hotel stay")

print("\nTrip planned successfully!")