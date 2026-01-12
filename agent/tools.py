import json
from langchain.tools import Tool

def recommend_destination(preference: str) -> str:
    with open("data/destinations.json") as f:
        destinations = json.load(f)

    matches = [
        d for d in destinations
        if preference.lower() in d["type"].lower()
    ]

    if not matches:
        return "No destinations found matching your preference."

    return "\n".join(
        f"{d['name']} | Best Time: {d['best_time']} | Budget: {d['budget']}"
        for d in matches
    )

def recommend_hotel(city: str) -> str:
    with open("data/hotels.json") as f:
        hotels = json.load(f)

    return "\n".join(hotels.get(city, ["No hotels available"]))

def generate_itinerary(city: str) -> str:
    with open("data/itineraries.json") as f:
        itineraries = json.load(f)

    city_plan = itineraries.get(city)

    if not city_plan:
        return "No itinerary available for this destination."

    return "\n".join(
        f"{day}: {plan}" for day, plan in city_plan.items()
    )

destination_tool = Tool(
    name="Destination Recommendation",
    func=recommend_destination,
    description="Suggest travel destinations based on travel preference"
)

hotel_tool = Tool(
    name="Hotel Recommendation",
    func=recommend_hotel,
    description="Recommend hotels for a given destination"
)

itinerary_tool = Tool(
    name="Itinerary Generator",
    func=generate_itinerary,
    description="Generate a day-wise travel itinerary"
)
