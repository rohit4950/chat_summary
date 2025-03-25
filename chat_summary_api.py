from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from collections import Counter

app = FastAPI()

class ChatTranscript(BaseModel):
    chat_id: str
    content: list

@app.post("/summarize_chat")
def summarize_chat(transcript: ChatTranscript):
    try:
        # Extract chat details
        chat_id = transcript.chat_id
        messages = transcript.content

        if not messages:
            raise HTTPException(status_code=400, detail="Chat content is empty")
        
        # Extract article link (assumed first message contains article reference)
        possible_article_link = "Unknown"
        for message in messages:
            if "http" in message["message"]:
                possible_article_link = message["message"]
                break

        # Initialize counters
        agent1_count, agent2_count = 0, 0
        agent1_sentiments, agent2_sentiments = [], []
        
        for message in messages:
            agent = message["agent"]
            sentiment = message["sentiment"]
            
            if agent == "Agent 1":
                agent1_count += 1
                agent1_sentiments.append(sentiment)
            elif agent == "Agent 2":
                agent2_count += 1
                agent2_sentiments.append(sentiment)
        
        # Compute sentiment distributions
        agent1_sentiment_summary = dict(Counter(agent1_sentiments))
        agent2_sentiment_summary = dict(Counter(agent2_sentiments))

        return {
            "chat_id": chat_id,
            "possible_article_link": possible_article_link,
            "messages_by_agent_1": agent1_count,
            "messages_by_agent_2": agent2_count,
            "overall_sentiment_agent_1": agent1_sentiment_summary,
            "overall_sentiment_agent_2": agent2_sentiment_summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run using: uvicorn chat_summary_api:app --reload