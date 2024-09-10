import pip
import os
from cookiecutter.main import cookiecutter
from git import Repo
import logging

def slug_to_pascal_case(slug):
    # Replace hyphens or underscores with spaces, split into words
    words = slug.replace('-', ' ').replace('_', ' ').split()
    # Capitalize the first letter of each word and join them
    return ''.join(word.capitalize() for word in words)

if __name__ == '__main__':
    logging.getLogger("git").setLevel(logging.WARNING)

    # Extract environment variables set by the CR
    project_name = os.getenv("PROJECT_NAME")
    project_slug = os.getenv("PROJECT_SLUG")
    template_name = os.getenv("TEMPLATE_NAME")
    git_username = os.getenv("GIT_USERNAME")
    git_password = os.getenv("GIT_PASSWORD")
    bff_service_name_and_port = os.getenv("BFF_SERVICE_NAME_AND_PORT")
    repo_url = os.getenv("REPO_URL")
    commit_message = os.getenv("COMMIT_MESSAGE", "Initial commit")

    print("Generate project")
    project_path = cookiecutter("https://github.com/djajcevic/bootstrapping", no_input=True, directory=template_name, extra_context={
        'project_slug': project_slug,
        'app_name': slug_to_pascal_case(project_slug),
        'bff_service_name_and_port': bff_service_name_and_port
    })

    # Initialize Git and push
    repo = Repo.init(project_path)
    repo.git.add(all=True)
    repo.index.commit(commit_message)

    # DO NOT PRINT THIS!!!
    tmp_repo_url = f"https://{git_username}:{git_password}@{repo_url.split('https://')[1]}"

    origin = repo.create_remote('origin', tmp_repo_url)
    try:
        origin.push(refspec='HEAD:refs/heads/main')
        print(f"Pushed code to {repo_url}")
    except:
        print(f"Had some trouble pushing code to remote {repo_url}")