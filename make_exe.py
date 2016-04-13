import os
from subprocess import check_output

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Project root:", project_root)
pyinstaller_path = os.getenv('PYINSTALLER_PATH', 'pyinstaller')

target = os.path.join(project_root, 'PyInstallerTest', 'main.py')

default_opts = ['--clean ',
                '-y ',
                '-p "{}" '.format(project_root),
                '--onedir',
                '--name {} '.format("main"),
                '--debug',
                ]

command = '{pyinstaller} {opts} "{target}"'.format(pyinstaller=pyinstaller_path,
                                                   opts=' '.join(default_opts),
                                                   target=target)
print(check_output(command, shell=True))
