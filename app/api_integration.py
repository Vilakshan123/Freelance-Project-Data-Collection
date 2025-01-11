import requests
import time

class FreelancerAPI:
    BASE_URL = "https://www.freelancer.com/api/projects/0.1/projects/active/"

    def __init__(self, logger, rate_limit=1):
        self.logger = logger
        self.rate_limit = rate_limit

    def fetch_ai_projects(self):
        params = {
            "query": "AI",
            "limit": 50
        }
        try:
            self.logger.info("Fetching projects from Freelancer API...")
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            time.sleep(self.rate_limit)  # Rate limiting
            projects = response.json().get("result", []).get("projects", [])
            self.logger.info(f"Fetched {len(projects)} projects.")
            return self.process_projects(projects)
        except requests.RequestException as e:
            self.logger.error(f"Error fetching data: {e}")
            return []

    def process_projects(self, projects):
        processed = []
        for project in projects:

            processed.append({
                "title": project.get("title"),
                "description": project.get("preview_description"),
                "budget_range": {
                    "minimum": project.get("budget", {}).get("minimum"),
                    "maximum": project.get("budget", {}).get("maximum")
                },
                "posted_date": project.get("time_submitted"),
                "skills": [skill["name"] for skill in project.get("skills", [])],
                "client_country": project.get("location", {}).get("country", {}).get("name", ""),
            })
        return processed
