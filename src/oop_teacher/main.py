#!/usr/bin/env python
import os
from datetime import datetime
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from oop_teacher.crews.oop_crew.oop_crew import OopCrew


class OopState(BaseModel):
    topic: str = ""
    explanation: str = ""
    code: str = ""


class OopFlow(Flow[OopState]):

    @start()
    def generate_topic(self):
        topic = input("Enter a topic: ")
        self.state.topic = topic

    @listen(generate_topic)
    def generate_oop_explanation(self):
        print("Generating oop explanation")
        result = (
            OopCrew()
            .crew()
            .kickoff(inputs={"topic": self.state.topic})
        )

        # print("Oop explanation generated", result.raw)
        self.state.explanation = result.raw

    @listen(generate_oop_explanation)
    def save_oop_explanation(self):
        print("Combining OOP explanation and code into a single file")
        
        try:
            with open("oop_explanation.md", "r") as exp_file:
                explanation = exp_file.read()
        except FileNotFoundError:
            explanation = "No explanation available"
            print("Warning: oop_explanation.md not found")
        try:
            with open("oop_code.md", "r") as code_file:
                code = code_file.read()
        except FileNotFoundError:
            code = "No code implementation available"
            print("Warning: oop_code.md not found")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        combined_content = f"""
# OOP Concept: {self.state.topic}
Generated on: {timestamp}
        
## Concept Explanation
{explanation}
        
## Code Implementation
{code}"""

        with open("oop_simplified.md", "w") as f:
            f.write(combined_content)
        
        print("Combined output saved to oop_combined_output.md")
        try:
            if os.path.exists("oop_explanation.md"):
                os.remove("oop_explanation.md")
            if os.path.exists("oop_code.md"):
                os.remove("oop_code.md")
            print("Cleaned up individual files")
        except Exception as e:
            print(f"Warning: Could not clean up individual files: {str(e)}")





def kickoff():
    oop_flow = OopFlow()
    oop_flow.kickoff()


def plot():
    oop_flow = OopFlow()
    oop_flow.plot()

