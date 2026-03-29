# presentation_generator.py
# ═══════════════════════════════════════════════════════════
# STEP 6 OF THE WORKFLOW: Generate Presentation Content
#
# This file takes the final research report and automatically
# generates 3 presentation-ready documents:
#
#   1. PRESENTATION SLIDES  — 8 slides ready to present


import os
import time
import datetime
import glob
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
GROQ_MODEL = "llama-3.3-70b-versatile"


# ═══════════════════════════════════════════════════════════
# HELPER: Ask Groq a question and get answer
# ═══════════════════════════════════════════════════════════
def ask_groq(prompt: str) -> str:
    """Sends a prompt to Groq and returns the response."""
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ═══════════════════════════════════════════════════════════
# HELPER: Get the latest final report from outputs/ folder
# ═══════════════════════════════════════════════════════════
def get_latest_final_report() -> tuple:
    """
    Finds the most recently generated FINAL_REPORT file.
    Returns (filepath, content) tuple.
    """
    report_files = glob.glob("outputs/FINAL_REPORT_*.md")

    if not report_files:
        print("   ❌ No final report found! Run main.py first.")
        return None, None

    # Get most recently created file
    latest_file = max(report_files, key=os.path.getctime)

    with open(latest_file, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"   📄 Using report: {latest_file}")
    return latest_file, content


# ═══════════════════════════════════════════════════════════
# GENERATOR 1: Presentation Slides
# ═══════════════════════════════════════════════════════════
def generate_slides(topic: str, report_content: str) -> str:
    """
    Generates 8 complete presentation slides from the report.
    Each slide has a title, bullet points, and speaker notes.
    Think of it as: an AI PowerPoint creator!
    """
    print("\n   📊 Generating presentation slides...")

    prompt = f"""You are a professional presentation designer.

Based on this research report, create a complete 8-slide presentation.

RESEARCH REPORT:
{report_content[:3000]}

Create EXACTLY 8 slides in this format:

═══════════════════════════════
SLIDE 1: Title Slide
═══════════════════════════════
Title: [Main title]
Subtitle: [One line description]
Presenter Notes: [What to say when opening]

═══════════════════════════════
SLIDE 2: Executive Summary
═══════════════════════════════
Title: Executive Summary
Bullet 1: [Key point]
Bullet 2: [Key point]
Bullet 3: [Key point]
Presenter Notes: [What to say]

[Continue same format for slides 3-8]

Cover these topics across slides:
- Slide 1: Title
- Slide 2: Executive Summary
- Slide 3: Key Findings
- Slide 4: Applications & Use Cases
- Slide 5: Current Developments
- Slide 6: Challenges & Limitations
- Slide 7: Future Outlook
- Slide 8: Conclusion & Recommendations

Make it professional and impressive!
"""

    slides = ask_groq(prompt)
    print("   ✅ Slides generated!")
    return slides

# ═══════════════════════════════════════════════════════════
# MAIN FUNCTION: Generate ALL presentation content
# ═══════════════════════════════════════════════════════════
def generate_all_presentation_content(topic: str, report_content: str) -> dict:
    """
    This is the main function called from main.py
    
    Takes the topic and report content, generates all 3 
    presentation documents, saves them to outputs/ folder,
    and returns the file paths.
    
    Returns a dictionary with all generated file paths.
    """

    print(f"\n🎨 Generating presentation content for: {topic}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Clean topic for filename
    clean_topic = "".join(
        c if c.isalnum() or c == " " else ""
        for c in topic
    ).strip().replace(" ", "_")[:25]

    saved_files = {}

    # ── Generate Slides ────────────────────────────────────
    slides_content = generate_slides(topic, report_content)
    slides_file = f"outputs/SLIDES_{clean_topic}_{timestamp}.md"
    with open(slides_file, "w", encoding="utf-8") as f:
        f.write(f"# 📊 Presentation Slides\n")
        f.write(f"**Topic:** {topic}\n")
        f.write(f"**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**AI Model:** Groq LLaMA 3.3-70B\n\n")
        f.write("---\n\n")
        f.write(slides_content)
    print(f"   💾 Saved: {slides_file}")
    saved_files["slides"] = slides_file

    # Small delay to avoid rate limits
    time.sleep(3)


# ═══════════════════════════════════════════════════════════
# Run this file directly to test presentation generation
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  🎨 PRESENTATION GENERATOR TEST")
    print("="*60)

    # Get the latest report
    report_file, report_content = get_latest_final_report()

    if report_content:
        topic = "Hydrogen applications in refining and fertilizers"
        files = generate_all_presentation_content(topic, report_content)

        print("\n" + "="*60)
        print("  ✅ ALL PRESENTATION FILES GENERATED!")
        print("="*60)
        for name, path in files.items():
            print(f"  📄 {name}: {path}")
    else:
        print("❌ Please run main.py first to generate a report!")