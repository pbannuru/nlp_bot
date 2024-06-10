from crewai import Crew, Process
from tasks import PropertyRetrievalTask, ItineraryPlanningTask, MemoryStorageTask, MemoryRetrievalTask
from agents import PropertyFinder, ItineraryPlanner, MemoryKeeper

# Instantiate agents
property_finder = PropertyFinder()
itinerary_planner = ItineraryPlanner()
memory_keeper = MemoryKeeper()

# Create tasks
property_task = PropertyRetrievalTask(agent=property_finder, user_preferences={})
itinerary_task = ItineraryPlanningTask(agent=itinerary_planner, properties={})
memory_task = MemoryStorageTask(agent=memory_keeper, user_id='user_123', user_data={})

# Assemble the crew with memory capabilities
my_crew = Crew(
    agents=[property_finder, itinerary_planner, memory_keeper],
    tasks=[property_task, itinerary_task, memory_task],
    process=Process.sequential,
    memory=True,
    verbose=True
)

# Function to kickoff the process
def kickoff_process(inputs):
    return my_crew.kickoff(inputs=inputs)
