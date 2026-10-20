print('номер 7')
from pathlib import Path
directory=input('Каталог:')
rash=input('Расширение:')
path=Path(directory)
if not path.exists():
    print('Каталога нет')
elif not path.is_dir():
    print('Это не каталог')
else:
    for file in path.rglob(f"*{rash}"):
        if file.is_file():
            print(file, '\n', file.stat().st_size)