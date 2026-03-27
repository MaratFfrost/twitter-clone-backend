from pathlib import Path
# Here must be env varuables, now db params are hardcode and if owner of the business has diceded to change db, he will have to look for it in code instead of change it in a file

# Папка, где лежит этот файл (то есть app/)
BASE_DIR = Path(__file__).resolve().parent

# В app/ создается папка media — туда будем сохранять файлы
MEDIA_DIR = BASE_DIR / "media"
