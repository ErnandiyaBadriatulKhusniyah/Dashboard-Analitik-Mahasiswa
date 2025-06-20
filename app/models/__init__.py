from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .fakultas import Fakultas
from .program_studi import ProgramStudi
from .mahasiswa import Mahasiswa
from .mata_kuliah import MataKuliah
from .transkrip import Transkrip
from .hasil_evaluasi_studi import HasilEvaluasiStudi
from .rencana_studi import RencanaStudi
from .user import User