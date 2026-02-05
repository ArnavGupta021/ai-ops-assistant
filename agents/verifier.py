class Verifier:

    def verify(self, user_input: str, results: dict):

        summary_parts = []

        if "github" in results:
            summary_parts.append(
                f"Found {len(results['github'])} repositories."
            )

        if "weather" in results:
            summary_parts.append(
                f"Weather in {results['weather']['city']} retrieved."
            )

        summary = " ".join(summary_parts)

        return {
            "summary": summary,
            "details": results
        }
