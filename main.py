# main.py
# ═══════════════════════════════════════════════════════════
# This is the MAIN FILE — run this to start everything!
# 
# What this file does:
#   1. Asks you what topic to research
#   2. Queries Gemini AI for research
#   3. Queries Ollama (local AI) for research
#   4. Combines both results
#   5. Runs 3 AI agents to analyze and write final report
#   6. Saves everything to the outputs/ folder
#
# How to run: python main.py
# ═══════════════════════════════════════════════════════════

import os
import datetime
from dotenv import load_dotenv
from crewai import Crew, Process

# Import our custom modules
from research_tools import gemini_research, ollama_research, combine_research
from agents import create_researcher, create_analyst, create_writer
from tasks import create_research_task, create_analysis_task, create_writing_task

# Load API keys from .env file
load_dotenv()


# ═══════════════════════════════════════════════════════════
# HELPER: Save output to a file
# ═══════════════════════════════════════════════════════════
def save_to_file(topic: str, content: str, prefix: str) -> str:
    """
    Saves text content to a .md file in the outputs/ folder.
    Each file gets a timestamp so old files are never overwritten.
    
    Example filename: outputs/FINAL_REPORT_Hydrogen_20240328_143022.md
    """
    # Make timestamp (e.g. 20240328_143022)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Clean the topic name so it can be used in a filename
    # (removes special characters, replaces spaces with underscores)
    clean_topic = "".join(
        c if c.isalnum() or c == " " else "" for c in topic
    ).strip().replace(" ", "_")[:30]
    
    # Build the full filename
    filename = f"outputs/{prefix}_{clean_topic}_{timestamp}.md"
    
    # Write the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"   💾 Saved: {filename}")
    return filename


# ═══════════════════════════════════════════════════════════
# HELPER: Print a nice section header
# ═══════════════════════════════════════════════════════════
def print_header(title: str):
    print("\n" + "═" * 60)
    print(f"  {title}")
    print("═" * 60)


# ═══════════════════════════════════════════════════════════
# MAIN WORKFLOW FUNCTION
# ═══════════════════════════════════════════════════════════
def run_research_workflow(topic: str):
    """
    This runs the complete research workflow from start to finish.
    
    WORKFLOW STEPS:
    ┌─────────────────────────────────────────┐
    │  Step 1: Groq researches the topic    │
    │  Step 2: Ollama researches the topic    │
    │  Step 3: Results are combined           │
    │  Step 4: Agent 1 (Researcher) organizes │
    │  Step 5: Agent 2 (Analyst) analyzes     │
    │  Step 6: Agent 3 (Writer) writes report │
    │  Step 7: Everything saved to files      │
    └─────────────────────────────────────────┘
    """

    print_header(f"🚀 AI RESEARCH AGENT STARTING")
    print(f"\n  📌 Topic: {topic}")
    print(f"  🕐 Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


    # ── PHASE 1: Gather Raw Research ──────────────────────────
    print_header("📡 PHASE 1: Gathering Research from AI Sources")

    # Query GROQ
    gemini_result = gemini_research(topic)
    save_to_file(topic, f"# Gemini Research: {topic}\n\n{gemini_result}", "1_gemini_raw")

    # Query Ollama
    ollama_result = ollama_research(topic)
    save_to_file(topic, f"# Ollama Research: {topic}\n\n{ollama_result}", "2_ollama_raw")

    print("\n  ✅ Phase 1 Complete — Research gathered from both AIs!")


    # ── PHASE 2: Combine Research ──────────────────────────────
    print_header("🔗 PHASE 2: Combining Research Results")

    combined = combine_research(topic, gemini_result, ollama_result)
    save_to_file(topic, combined, "3_combined_research")

    print("\n  ✅ Phase 2 Complete — Research combined!")


    # ── PHASE 3: Multi-Agent Analysis & Report Writing ─────────
    print_header("🤖 PHASE 3: Multi-Agent Analysis & Report Writing")
    print("\n  Creating AI agent team...")

    # Create the 3 agents (team members)
    researcher = create_researcher()
    analyst    = create_analyst()
    writer     = create_writer()

    print("  ✅ Agents created: Researcher, Analyst, Writer")

    # Create their tasks (assignments)
    research_task = create_research_task(
        researcher, topic, gemini_result, ollama_result
    )
    analysis_task = create_analysis_task(analyst, topic)
    writing_task  = create_writing_task(writer, topic)

    print("  ✅ Tasks assigned to each agent")

    # Assemble the Crew and run!
    # Process.sequential = agents work one after another (in order)
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True
    )

    print("\n  🏃 Crew is now working... (this takes 2-4 minutes)")
    print("  You will see each agent's thinking process below:\n")

    # THIS LINE STARTS ALL THE AGENTS WORKING
    final_report = crew.kickoff()


    # ── PHASE 4: Save Final Report ─────────────────────────────
    print_header("💾 PHASE 4: Saving Final Report")

    # Build the complete final report document
    report_content = f"""# 🤖 AI Research Agent — Final Report

**Topic:** {topic}  
**Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**AI Sources Used:** Google Gemini 1.5 Flash + Ollama Llama3.2  
**System:** CrewAI Multi-Agent (Researcher → Analyst → Writer)  

---

{str(final_report)}

---

*This report was automatically generated by the AI Research Agent System*  
*Built with: Python, CrewAI, Google Gemini, Ollama*
"""

    final_file = save_to_file(topic, report_content, "FINAL_REPORT")
    # ── PHASE 5: Generate Presentation Content ─────────────
    print_header("🎨 PHASE 5: Generating Presentation Content")
    from presentation_generator import generate_all_presentation_content
    presentation_files = generate_all_presentation_content(
    topic, report_content
     )
    print("\n  ✅ Phase 5 Complete — Presentation content ready!")

    # ── DONE! ──────────────────────────────────────────────────
    print_header("🎉 WORKFLOW COMPLETE!")
    print(f"""
  All files saved in your outputs/ folder:
  
  📄 1_gemini_raw_...md       ← Raw Gemini research
  📄 2_ollama_raw_...md       ← Raw Ollama research  
  📄 3_combined_research_...md ← Combined from both
  📄 FINAL_REPORT_...md       ← ⭐ The main output
  
  ✅ Your final report is ready: {final_file}
  
  👉 Next step: Upload FINAL_REPORT to NotebookLM
     for presentation generation!
    """)

    return final_report




# ═══════════════════════════════════════════════════════════
# ENTRY POINT — This runs when you type: python main.py
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":

    print_header("🤖 AI Research Agent System")
    print("""
  This system will:
  ✅ Research your topic using 2 AI sources
  ✅ Combine and analyze the results  
  ✅ Write a professional final report
  ✅ Save everything to the outputs/ folder
    """)

    # Ask the user what to research
    topic = input("📌 Enter your research topic: ").strip()

    # Use default topic if nothing entered
    if not topic:
        topic = "Hydrogen applications in refining and fertilizers"
        print(f"  (Using default topic: {topic})")

    # Check API key exists
    if not os.getenv("GEMINI_API_KEY"):
        print("\n❌ ERROR: GEMINI_API_KEY not found in your .env file!")
        print("   Make sure your .env file contains: GEMINI_API_KEY=your_key_here")
        exit(1)

    # Run the full workflow!
    run_research_workflow(topic)