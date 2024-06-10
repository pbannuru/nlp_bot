from crewai_tools import CSVSearchTool, WebsiteSearchTool

# Initialize the tools with the appropriate CSV file and website using custom model and embeddings
property_search_tool = CSVSearchTool(
    csv='property_feature_rag.csv',
    config=dict(
        llm=dict(
            provider="ollama",  # Customize as needed
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=True,
            ),
        ),
        embedder=dict(
            provider="google",  # Customize as needed
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

website_search_tool = WebsiteSearchTool(
    website='https://www.hiltongrandvacations.com/',
    config=dict(
        llm=dict(
            provider="ollama",  # Customize as needed
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=True,
            ),
        ),
        embedder=dict(
            provider="google",  # Customize as needed
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
