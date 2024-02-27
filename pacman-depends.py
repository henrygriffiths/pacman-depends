import subprocess
import re

package_list = [package for package in subprocess.run(['pacman', '-Qq'], capture_output = True).stdout.decode().split('\n') if len(package) > 0]

packages = {}
for package in package_list:
    print(f"Processing Package {package}")
    package_info = [re.sub(r' +', ' ', line) for line in re.sub(r'\n +', ' ', subprocess.run(['pacman', '-Qi', package], capture_output = True).stdout.decode()).split('\n') if len(line) > 0]
    packages[package] = {line[0]: line[1] for line in (line.split(' : ', 1) for line in package_info)}
print('Completed Processing\n\n\n\n')


print('Undepended on Packages:')
for package, package_data in packages.items():
    if package_data['Required By'] == 'None' and package_data['Optional For'] == 'None':
        print(f"{package}: {package_data['Description']}. {package_data['URL']}")
