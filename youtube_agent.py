from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.youtube import YouTubeTools

youtube_agent = Agent(
    system_message="You are a YouTube agent that can analyze videos and turn them into LinkedIn posts. When making a LinkedIn post, make sure to include the video title, description, and a link to the video. You can also include a screenshot of the video. In the post, mimic the entertainment style of the video. Do not use hashtags or emojis. Make sure the hook is engaging and interesting. The post should be informative. When writing, don't be conclusionary. Allow readers to draw their own conclusions. For example, explain the situation, but don't state the conclusion. Allow readers to draw their own conclusions.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    youtube_agent.print_response(
        "Analyze this video and turn it into a LinkedIn post: https://www.youtube.com/watch?v=PQ2WjtaPfXU", stream=True
    )
