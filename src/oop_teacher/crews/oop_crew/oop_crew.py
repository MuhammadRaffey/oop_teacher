from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class OopCrew:
    """OOP Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def oop_concept_explainer(self) -> Agent:
        return Agent(
            config=self.agents_config["oop_concept_explainer"],
        )
    
    @agent
    def oop_concept_coder(self) -> Agent:
        return Agent(
            config=self.agents_config["oop_concept_coder"],
        )

    @task
    def explain_oop_concept(self) -> Task:
        return Task(
            config=self.tasks_config["explain_oop_concept"],
            output_file="oop_explanation.md",
        )
    
    @task
    def code_oop_concept(self) -> Task:
        return Task(
            config=self.tasks_config["code_oop_concept"],
            output_file="oop_code.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the OOP Crew"""

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
