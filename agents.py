# agents.py
# AI agents now use Groq as their brain instead of Gemini.
# Groq is faster and has a very generous free tier!

import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# AGENT 1: The Researcher
# ═══════════════════════════════════════════════════════════
def create_researcher():
    return Agent(
        role="Senior Research Specialist",
        goal="""Carefully read and organize research findings
        from multiple AI sources into clear, structured information.""",
        backstory="""You are an experienced research specialist with
        15 years of experience. You are known for your ability to
        read information from multiple sources and organize it
        clearly. You always cross-check facts and highlight where
        sources agree or disagree.""",
        llm=groq_llm,
        verbose=True,
        allow_delegation=False
    )


# AGENT 2: The Analyst
# ═══════════════════════════════════════════════════════════
def create_analyst():
    return Agent(
        role="Strategic Research Analyst",
        goal="""Analyze research findings deeply to extract
        the most valuable insights, patterns, and actionable
        recommendations.""",
        backstory="""You are a brilliant strategic analyst
        who has worked with Fortune 500 companies. You excel
        at taking large amounts of raw information and finding
        the patterns that others miss. You always ask 'so what?'
        — meaning you don't just report facts, you explain
        WHY they matter and WHAT to do about them.""",
        llm=groq_llm,
        verbose=True,
        allow_delegation=False
    )

# ═══════════════════════════════════════════════════════════
# AGENT 3: The Writer
# ═══════════════════════════════════════════════════════════
def create_writer():
    return Agent(
        role="Professional Technical Writer",
        goal="""Transform research and analysis into a clear,
        professional report that anyone can understand,
        formatted perfectly for presentations.""",
        backstory="""You are an award-winning technical writer
        who has written reports for governments, universities,
        and top companies. Your superpower is making complex
        topics easy to understand without losing accuracy.
        Your reports are always beautifully structured,
        concise, and immediately useful to the reader.""",
        llm=groq_llm,
        verbose=True,
        allow_delegation=False
    )
