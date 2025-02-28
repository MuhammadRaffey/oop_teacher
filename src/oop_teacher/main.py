#!/usr/bin/env python
from random import randint

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

        print("Oop explanation generated", result.raw)
        self.state.explanation = result.raw

    @listen(generate_oop_explanation)
    def save_oop_explanation(self):
        print("Saving oop explanation")
        with open("oop_explanation.md", "w") as f:
            f.write(self.state.explanation)





def kickoff():
    oop_flow = OopFlow()
    oop_flow.kickoff()


def plot():
    oop_flow = OopFlow()
    oop_flow.plot()

