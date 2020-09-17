from pathlib import Path
import os
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.exists(r'\PycharmProjects'))
print(os.path.isfile(r'\PycharmProjects'))
print(os.path.isdir(r'\PycharmProjects'))
# os.path.join('/tmp/a/', 'b/c')


p = Path('.')
print(type(p))
print(p.resolve())

print(p.is_dir())

# q = Path('/tmp/a/b/c')
# Path.mkdir(q, parents=True)
