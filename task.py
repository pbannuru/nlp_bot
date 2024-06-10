from crewai import Task

class PropertyRetrievalTask(Task):
    def __init__(self, agent, user_preferences):
        super().__init__(agent, user_preferences)
        self.description = "Retrieve properties based on user preferences from CSV and website."
        self.expected_output = "A list of properties matching the user preferences."

    def run(self):
        return self.agent.perform_search(self.user_preferences)

class ItineraryPlanningTask(Task):
    def __init__(self, agent, properties):
        super().__init__(agent, properties)
        self.description = "Create detailed itineraries based on retrieved properties."
        self.expected_output = "A detailed itinerary with activities and locations."

    def run(self):
        return self.agent.create_itinerary(self.properties)

class MemoryStorageTask(Task):
    def __init__(self, agent, user_id, user_data):
        super().__init__(agent, user_id, user_data)
        self.description = "Store user preferences and data."
        self.expected_output = "Confirmation of data storage."

    def run(self):
        self.agent.store_memory(self.user_id, self.user_data)

class MemoryRetrievalTask(Task):
    def __init__(self, agent, user_id):
        super().__init__(agent, user_id)
        self.description = "Retrieve stored user data and preferences."
        self.expected_output = "User preferences and data."

    def run(self):
        return self.agent.retrieve_memory(self.user_id)
