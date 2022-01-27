import os
import re
import sys
from jinja2 import Environment, FileSystemLoader

print(sys.argv)

exclude_dir = os.getenv('EXCLUDE_DIR', "")

def find_files(filter=""):

    file_dirs = []

    for subdir, dirs, files in os.walk('.'):
        if subdir.find(exclude_dir) != -1:
          continue
        for file in files:
            dir = re.search(filter, file)
            if dir != None:
              if subdir[1:] not in file_dirs:
                  file_dirs.append(subdir[1:])

    return file_dirs

terraform_dirs = find_files('.*.tf')
docker_dirs = find_files('Dockerfile')
npm_dirs = find_files('package.json')

file_loader = FileSystemLoader('/templates')
env = Environment(loader=file_loader)

template = env.get_template('dependabot.yml.j2')

rendered_output = template.render(terraform_dirs=terraform_dirs,docker_dirs=docker_dirs,npm_dirs=npm_dirs)

f = open(".github/dependabot.yml", "w")
f.write(rendered_output)
f.close()
