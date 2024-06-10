from crewai import Agent
from tools import property_search_tool, website_search_tool

class PropertyFinder(Agent):
    def __init__(self):
        super().__init__(
            name="PropertyFinder",
            role="Retrieve the most relevant properties",
            goal="Perform semantic search on the CSV file and retrieve property details from Hilton Grand Vacations",
            backstory="Born from the need to connect travelers with their perfect stay, PropertyFinder has traversed countless databases to bring the best properties to light.",
            llm="local-llm",
            verbose=True,
            allow_delegation=True,
            tools=[property_search_tool, website_search_tool]
        )

    def perform_search(self, user_preferences):
        results = self.tools[0].search(user_preferences)  # Using the CSVSearchTool
        return results

class ItineraryPlanner(Agent):
    def __init__(self):
        super().__init__(
            name="ItineraryPlanner",
            role="Create detailed travel itineraries",
            goal="Research nearby locations and events, and create travel itineraries based on retrieved properties",
            backstory="With a passion for exploration and meticulous planning, ItineraryPlanner crafts the most memorable journeys tailored to each traveler.",
            llm="local-llm",
            verbose=True,
            allow_delegation=True,
            tools=["SearchEngineAPI"]
        )

    def create_itinerary(self, properties):
        itineraries = []
        for index, property in properties.iterrows():
            location = property['location']
            itineraries.append({
                'property': property['name'],
                'location': location,
                'activities': ['Visit museum', 'Attend concert', 'City tour']
            })
        return itineraries

class MemoryKeeper(Agent):
    def __init__(self):
        super().__init__(
            name="MemoryKeeper",
            role="Maintain user context and memory",
            goal="Store and retrieve user preferences and past interactions",
            backstory="MemoryKeeper never forgets a preference or detail, ensuring every interaction feels personalized and informed.",
            llm="local-llm",
            verbose=True,
            allow_delegation=True,
            tools=["MemoryStorage"]
        )
        self.memory = {}

    def store_memory(self, user_id, user_data):
        self.memory[user_id] = user_data

    def retrieve_memory(self, user_id):
        return self.memory.get(user_id, {})
