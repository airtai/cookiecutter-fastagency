import glob
import os

REMOVE_PATHS = [
    {% if cookiecutter.app_type == 'console' or cookiecutter.app_type == 'mesop' %}"{{cookiecutter.project_slug}}/main_*.py",{% endif %}
    {% if 'fastapi' in cookiecutter.app_type %}"{{cookiecutter.project_slug}}/main.py",{% endif %}
    {% if 'nats' not in cookiecutter.app_type %}"{{cookiecutter.project_slug}}/main_2_fastapi.py",{% endif %}
    {% if 'nats' not in cookiecutter.app_type %}".devcontainer/nats_server.conf",{% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if not path:
        continue
    paths = list(glob.glob(path)) if "*" in path else [path]
    
    for p in paths:
        if p and os.path.exists(p):
            if os.path.isdir(p):
                os.rmdir(p)
            else:
                os.unlink(p)
