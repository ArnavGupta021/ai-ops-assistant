from schemas import Plan, Step

class Planner:

    def create_plan(self, user_input: str) -> Plan:

        steps = []
        text = user_input.lower()

        # Extract topic for repo search
        repo_query = None
        if "repository" in text or "repo" in text:
            words = user_input.split()

            # Basic topic detection
            for i, w in enumerate(words):
                if w.lower() in ["ai", "python", "javascript", "java"]:
                    repo_query = w
                    break

            if not repo_query:
                repo_query = "machine learning"

            steps.append(
                Step(
                    tool="github_search",
                    parameters={
                        "query": repo_query,
                        "limit": 2
                    }
                )
            )

        # Weather detection
        if "weather" in text:
            words = user_input.split()
            city = None

            for w in words:
                if w.istitle():
                    city = w

            if city:
                steps.append(
                    Step(
                        tool="weather",
                        parameters={"city": city}
                    )
                )

        return Plan(steps=steps)
