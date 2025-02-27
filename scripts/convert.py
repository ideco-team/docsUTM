"""
Скрипт для конвертации файлов офлайн-обновлений для >= v18 в файлы для < v18.
"""

import glob
from pathlib import Path
import tarfile


def find_file(wildcard: str) -> Path:
    files = glob.glob(wildcard)
    
    if len(files) == 1:
        return Path(files[0])
    
    if len(files) == 0:
        print(f'\tНе найден файл {wildcard}')
    
    if len(files) > 1:
        print(f'\tНайдено больше 1 файла {wildcard}, необходимо оставить только 1')


def extract_from_tar(tar_path: Path, startswith: str, converted_path: Path) -> None:
    with tarfile.open(tar_path, 'r') as tar:
        for name in tar.getnames():
            if name.startswith(startswith):
                content = tar.extractfile(name).read()
                output_filename = converted_path / name
                with open(output_filename, "wb") as f:
                    f.write(content)
                print(f"\tФайл сохранен: {output_filename}")
                break
        else:
            print(f'\t{startswith} не найден в архиве {tar_path}')


def make_license(converted_path: Path) -> None:
    print('Создаем лицензию')
    jwt_path = find_file('license*.jwt')
    if jwt_path:
        last_update = jwt_path.stat().st_mtime
        with open(jwt_path, 'r') as f:
            jwt = f.read().replace('\n', '')
        
        with open(converted_path / 'license.json', 'w') as f:
            f.write(
                f'{{"jwt": "{jwt}", "last_update": {last_update}}}\n'
            )

        print("\tФайл сохранен: license.json")


def make_content_filter(converted_path: Path):
    content_filter_path = find_file('content_filter*.tar')
    print('Создаем контент-фильтр')
    extract_from_tar(content_filter_path, 'sky-db', converted_path)


def make_common(converted_path: Path):
    common_path = find_file('common*.tar')
    print('Создаем geoip')
    extract_from_tar(common_path, 'ideco-geoip', converted_path)
    print('Создаем iplist')
    extract_from_tar(common_path, 'iplist', converted_path)
    print('Создаем suricata')
    extract_from_tar(common_path, 'suricata', converted_path)


if __name__ == "__main__":
    converted_path = Path('converted')
    converted_path.mkdir(exist_ok=True)

    make_license(converted_path)
    make_common(converted_path)
    make_content_filter(converted_path)
