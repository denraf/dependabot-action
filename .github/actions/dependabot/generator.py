import os
import re
import sys
from jinja2 import Environment, FileSystemLoader

exclude_dir = os.getenv('INPUT_EXCLUDE-DIR', "")

def find_files(filter=""):

    file_dirs = []

    for subdir, dirs, files in os.walk('.'):
        if exclude_dir != "" and subdir.find(exclude_dir) != -1:
          continue
        for file in files:
            dir = re.search(filter, file)
            if dir != None:
              if subdir == '.':
                  adddir = '/'
              else:
                  adddir = subdir[1:]

              if adddir not in file_dirs:
                  file_dirs.append(adddir)

    return file_dirs

gh_actions_dir = os.path.isdir('.github/workflows')

terraform_dirs = find_files('\.tf$')
docker_dirs = find_files('Dockerfile')
npm_dirs = find_files('package.json')
go_dirs = find_files('go.mod')
ruby_dirs = find_files('Gemfile')
pip_dirs = find_files('requirements.txt')
maven_dirs = find_files('pom.xml')

file_loader = FileSystemLoader( sys.path[0] + '/templates')
env = Environment(loader=file_loader)

template = env.get_template('dependabot.yml.j2')

rendered_output = template.render(terraform_dirs=terraform_dirs,docker_dirs=docker_dirs,npm_dirs=npm_dirs,go_dirs=go_dirs,ruby_dirs=ruby_dirs,pip_dirs=pip_dirs,maven_dirs=maven_dirs,gh_actions_dir=gh_actions_dir)

f = open(".github/dependabot.yml", "w")
f.write(rendered_output)
f.close()
