from project.app.src.domain.text_summarizer import TextSummarizer
from project.app.src.infrastructure.summarizers.constants import CLAUDE_MODEL

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


class ClaudeSummarizer(TextSummarizer):
    def __init__(self):
        self._model = ChatOpenAI(
            model=CLAUDE_MODEL, temperature=0.1, max_tokens=1000, timeout=30
        )

    def summarize(self, text: str) -> str:
        agent = create_agent(
            self._model,
            agent_type="chat-conversational-react-description",
            verbose=False,
        )
        prompt = f"Summarize the following text in a concise manner:\n\n{text}"
        response = agent.run(prompt)
        return response
