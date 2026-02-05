from tools.github_tool import search_repos
from tools.weather_tool import get_weather

class Executor:

    def execute(self, plan):
        results = {}

        for step in plan.steps:
            if step.tool == "github_search":
                results["github"] = search_repos(**step.parameters)

            elif step.tool == "weather":
                results["weather"] = get_weather(**step.parameters)

        return results
