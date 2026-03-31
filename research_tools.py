
# This file contains the "skills" our AI agents will use.


import os
import time
import ollama
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Create the Groq client using your API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


GROQ_MODEL = "llama-3.3-70b-versatile"


def ask_groq(prompt: str) -> str:
    """
    Helper function — sends any prompt to Groq and returns the response.
    Think of this as the 'phone call' to the Groq AI service.
    """
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Groq call failed: {str(e)}"


# ═══════════════════════════════════════════════════════════
# TOOL 1 — Ask Groq to research a topic
# ═══════════════════════════════════════════════════════════
def gemini_research(topic: str) -> str:
    """
    Now powered by Groq instead of Gemini.
    We kept the function name same so rest of code doesn't break.
    Think of this as: Source 1 research (Groq Cloud AI)
    """
    try:
        print(f"\n⚡ Groq AI is researching: {topic}")
        print("   Please wait...")

        prompt = f"""You are a professional research expert.

Research this topic thoroughly and provide detailed, accurate information.

Topic: {topic}

Structure your response EXACTLY like this:

## 1. Overview
(Write a clear introduction to the topic)

## 2. Key Applications
(List and explain the main real-world uses)

## 3. Current Developments
(What is happening right now in this field?)

## 4. Challenges & Limitations
(What problems exist? What are the difficulties?)

## 5. Future Potential
(Where is this heading? What's possible in future?)

## 6. Key Takeaways
(Summarize the 3-5 most important points)
"""
        result = ask_groq(prompt)
        print("   ✅ Groq research complete!")
        return result

    except Exception as e:
        return f"❌ Groq research failed: {str(e)}"


# ═══════════════════════════════════════════════════════════
# TOOL 2 — Ask Ollama (local AI) to research a topic
# ═══════════════════════════════════════════════════════════
def ollama_research(topic: str) -> str:
    """
    Sends your research topic to Ollama — the AI running
    locally on YOUR computer (no internet needed!)
    This is Source 2 research.
    """
    try:
        print(f"\n🦙 Ollama (local AI) is researching: {topic}")
        print("   Please wait...")

        response = ollama.chat(
            model="tinyllama",
            messages=[
                {
                    "role": "user",
                    "content": f"""You are a professional research expert.

Research this topic and provide detailed insights.

Topic: {topic}

Structure your response EXACTLY like this:

## 1. Technical Overview
(Explain the technical aspects clearly)

## 2. Practical Use Cases
(Give real-world examples of how this is used)

## 3. Industry Impact
(How does this affect businesses and industries?)

## 4. Challenges
(What are the main problems and obstacles?)

## 5. Expert Recommendations
(What should someone know or do about this topic?)
"""
                }
            ]
        )

        print("   ✅ Ollama research complete!")
        return response['message']['content']

    except Exception as e:
        return f"❌ Ollama research failed: {str(e)}"


# ═══════════════════════════════════════════════════════════
# TOOL 3 — Combine both research results into one report
# ═══════════════════════════════════════════════════════════
def combine_research(topic: str, groq_result: str, ollama_result: str) -> str:
    """
    Takes research from BOTH Groq and Ollama and combines
    them into one perfect final report using Groq.
    """
    try:
        print(f"\n📝 Combining research from both AI sources...")
        print("   Please wait...")

        # Small delay to be safe with rate limits
        time.sleep(2)

        prompt = f"""You are a senior research analyst and editor.

You have received research on "{topic}" from TWO different AI systems.
Your job is to combine them into ONE perfect, comprehensive report.

Remove duplicate information.
Keep the best insights from each source.
Make the final report flow naturally and read professionally.

════════════════════════════════════
RESEARCH FROM SOURCE 1 (Groq Cloud AI):
════════════════════════════════════
{groq_result}

════════════════════════════════════
RESEARCH FROM SOURCE 2 (Ollama Local AI):
════════════════════════════════════
{ollama_result}

════════════════════════════════════

Now write the FINAL COMBINED REPORT using this structure:

# 📊 Research Report: {topic}

## Executive Summary
(3-4 sentences capturing the most important points)

## Key Findings
(The most important discoveries from both sources)

## Applications & Use Cases
(Real-world applications, combining best from both sources)

## Current Developments
(What is happening right now)

## Challenges & Limitations
(Problems and obstacles)

## Future Outlook
(Where this is heading)

## Conclusion & Recommendations
(Final thoughts and what someone should do with this information)

---
*Research Sources: Groq LLaMA3-70B + Ollama TinyLlama (Local)*
"""

        result = ask_groq(prompt)
        print("   ✅ Research combined successfully!")
        return result

    except Exception as e:
        return f"❌ Combining research failed: {str(e)}"