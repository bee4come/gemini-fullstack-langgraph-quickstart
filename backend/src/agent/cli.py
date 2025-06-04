import argparse
import asyncio
from pathlib import Path

from langchain_core.messages import HumanMessage

from agent.graph import graph


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the research agent from the CLI")
    parser.add_argument("topic", nargs="?", help="Topic to research")
    parser.add_argument("-o", "--output", default="result.json", help="File to store the final JSON")
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    topic = args.topic or input("Enter research topic: ").strip()

    print(f"Starting research for: {topic}")
    final_state = None
    step = 1
    async for event in graph.astream_events({"messages": [HumanMessage(content=topic)]}, version="v1"):
        if event["event"] == "on_start":
            print(f"Step {step}: {event['name']}")
        if event["event"] == "on_end":
            step += 1
            final_state = event["data"]
    if final_state and final_state.get("messages"):
        output = final_state["messages"][-1].content
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Written result to {args.output}")


if __name__ == "__main__":
    asyncio.run(main())
