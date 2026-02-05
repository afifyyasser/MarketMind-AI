from src.graph import app
from dotenv import load_dotenv
import os

load_dotenv()

def run_market_mind_for_topic(topic: str):
    print(f"\n Starting MarketMind AI for: {topic}\n")

    # The main message that the system will enter
    inputs = {
        "messages": [
            ("human", f"حلل السوق التالي باللغة العربية فقط وبأسلوب تقرير احترافي: {topic}")
        ]
    }

    final_state = None  #We will store the last state of the graph there.

    #Display messages as the system works, moment by moment.
    for event in app.stream(inputs, stream_mode="values"):
        last_message = event["messages"][-1]
        content_preview = str(last_message.content)[:150]
        print(f"[{last_message.type.upper()}]: {content_preview}...")
        print("-" * 30)

        final_state = event  # Latest status update

    if final_state is None:
        raise RuntimeError("MarketMind لم يُنتج أي مخرجات")

    # Prepare the save path
    safe_topic = topic.replace(" ", "_").replace("/", "_")
    REPORT_DIR = os.getenv("REPORT_PATH", "reports")
    os.makedirs(REPORT_DIR, exist_ok=True)

    filename = os.path.join(REPORT_DIR, f"Market_Report_{safe_topic}.md")

    # Extract the final report
    report_content = final_state.get("report_content")

    if not report_content:
        # fallback if the report is not explicitly saved
        report_content = final_state["messages"][-1].content

    # Save the report
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n Report saved as {filename}\n")


def run_market_mind():
    while True:
        topic = input("اكتب الموضوع اللي عايز MarketMind يحلله (أو اكتب 'exit' للخروج): ")
        if topic.lower() == "exit":
            print("تم إيقاف MarketMind AI")
            break

        if not topic.strip():
            print("من فضلك اكتب موضوع صحيح\n")
            continue

        run_market_mind_for_topic(topic)


if __name__ == "__main__":
    run_market_mind()
