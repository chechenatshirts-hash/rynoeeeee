# storage.py
import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

USER_FILE = DATA_DIR / "user.json"
ENTRENOS_FILE = DATA_DIR / "entrenos.json"
METAS_FILE = DATA_DIR / "metas.json"
FANTASY_FILE = DATA_DIR / "fantasy.json"

def _leer(path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except:
            return default
    return default

def _escribir(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# ---------- Usuario ----------
def guardar_usuario(profile: dict):
    profile["created_at"] = datetime.now().isoformat()
    _escribir(USER_FILE, profile)

def cargar_usuario():
    return _leer(USER_FILE, {})

def borrar_usuario():
    if USER_FILE.exists():
        USER_FILE.unlink()

def usuario_existe():
    return USER_FILE.exists()

# ---------- Entrenos ----------
def _init_listas():
    if not ENTRENOS_FILE.exists():
        _escribir(ENTRENOS_FILE, [])
    if not METAS_FILE.exists():
        _escribir(METAS_FILE, [])
    if not FANTASY_FILE.exists():
        _escribir(FANTASY_FILE, {"xp":0,"level":1,"coins":0,"badges":[]})

_init_listas()

def cargar_entrenos():
    return _leer(ENTRENOS_FILE, [])

def guardar_entreno(entreno: dict):
    entrenos = cargar_entrenos()
    entrenos.append(entreno)
    _escribir(ENTRENOS_FILE, entrenos)

def borrar_entrenos():
    _escribir(ENTRENOS_FILE, [])

# ---------- Metas ----------
def cargar_metas():
    return _leer(METAS_FILE, [])

def guardar_meta(meta: dict):
    metas = cargar_metas()
    metas.append(meta)
    _escribir(METAS_FILE, metas)

# ---------- Fantasy (perfil simple) ----------
def cargar_fantasy():
    return _leer(FANTASY_FILE, {"xp":0,"level":1,"coins":0,"badges":[]})

def guardar_fantasy(profile: dict):
    _escribir(FANTASY_FILE, profile)
