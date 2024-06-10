import streamlit as st
from crew import kickoff_process
from tasks import MemoryRetrievalTask

st.title('Travel Agent Chatbot')

# User input for preferences
user_preferences = st.text_input('Enter your travel preferences:')
user_id = 'user_123'  # Dummy user ID for demonstration

if st.button('Generate Itinerary'):
    # Retrieve user memory
    memory_retrieval_task = MemoryRetrievalTask(agent=memory_task.agent, user_id=user_id)
    past_preferences = kickoff_process({'memory_task': memory_retrieval_task})[0]

    # Combine past preferences with current input
    combined_preferences = user_preferences
    if past_preferences:
        combined_preferences += " " + past_preferences

    # Run the full process
    results = kickoff_process({'topic': combined_preferences})

    # Display results
    if 'property_task' in results:
        properties = results['property_task']
        if properties.empty:
            st.write('No properties found matching your preferences.')
        else:
            for itinerary in results['itinerary_task']:
                st.write(f"Property: {itinerary['property']}")
                st.write(f"Location: {itinerary['location']}")
                st.write("Activities:")
                for activity in itinerary['activities']:
                    st.write(f"- {activity}")
