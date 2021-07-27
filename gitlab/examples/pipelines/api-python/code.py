import os
import gitlab

gl = gitlab.Gitlab('https://gitlab.com/', private_token=os.getenv('GITLAB_PRIVATE_TOKEN'))

# List all the projects
#projects = gl.projects.list()
#for project in projects:
#    print(project)

# Given the current project
project_id = os.getenv('CI_PROJECT_ID')
project = gl.projects.get(project_id)

print("-----------------")
for pipe in project.pipelines.list():
    print(pipe)

print("-----------------")
for job in project.jobs.list():
    print(job)
    print()

