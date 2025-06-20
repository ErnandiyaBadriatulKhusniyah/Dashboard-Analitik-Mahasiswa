# models.py
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fakultas(db.Model):
    _tablename_ = 'fakultas'
    kode_fakultas = db.Column(db.String(3), primary_key=True)
    nama_fakultas = db.Column(db.String(30))
    lokasi = db.Column(db.String(15))

    prodis = db.relationship('ProgramStudi', backref='fakultas', lazy=True)

class ProgramStudi(db.Model):
    _tablename_ = 'program_studi'
    kode_prodi = db.Column(db.String(4), primary_key=True)
    nama_prodi = db.Column(db.String(100))
    kode_fakultas = db.Column(db.String(3), db.ForeignKey('fakultas.kode_fakultas'))

    mahasiswa = db.relationship('Mahasiswa', backref='program_studi', lazy=True)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    nip = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.Text)
    roles = db.Column(ARRAY(db.String))  # contoh: ['kaprodi', 'dosen'] atau ['dosen']

class Mahasiswa(db.Model):
    _tablename_ = 'mahasiswa'
    
    nim = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    angkatan = db.Column(db.Integer)
    kode_prodi = db.Column(db.String(4), db.ForeignKey('program_studi.kode_prodi'))

    transkrip = db.relationship('Transkrip', backref='mahasiswa', lazy=True)
    hasil_evaluasi = db.relationship('HasilEvaluasiStudi', backref='mahasiswa', lazy=True)



class MataKuliah(db.Model):
    _tablename_ = 'mata_kuliah'
    kode_mk = db.Column(db.String(10), primary_key=True)
    nama_mk = db.Column(db.Text)
    sifat = db.Column(db.String(20))
    kode_mk_prasyarat = db.Column(db.String(10))
    semester = db.Column(db.Integer)

    kurikulum = db.relationship('Kurikulum', backref='mata_kuliah', lazy=True)
    transkrip = db.relationship('Transkrip', backref='mata_kuliah', lazy=True)
    rencana_studi = db.relationship('RencanaStudi', backref='mata_kuliah', lazy=True)
    khs = db.relationship('KHS', backref='mata_kuliah', lazy=True)



class Transkrip(db.Model):
    _tablename_ = 'transkrip'
    transkrip_id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.nim'))
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    sks = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    huruf_mutu = db.Column(db.String(2))
    mutu = db.Column(db.Numeric(4, 2))
    ipk = db.Column(db.Numeric(4, 2))
    jumlah_sks = db.Column(db.Integer)

class HasilEvaluasiStudi(db.Model):
    _tablename_ = 'hasil_evaluasi_studi'
    evaluasi_id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.nim'))
    semester = db.Column(db.Integer)
    ip = db.Column(db.Numeric(3, 2))
    ipk = db.Column(db.Numeric(3, 2))
    sks_lulus = db.Column(db.Integer)
    total_sks = db.Column(db.Integer)
    status_akademik = db.Column(db.String(20))
    catatan = db.Column(db.Text)
    tanggal_evaluasi = db.Column(db.Date)
    sks_tidak_lulus = db.Column(db.Integer)

class Kurikulum(db.Model):
    _tablename_ = 'kurikulum'
    kode_kurikulum = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    kode_mk_prasyarat = db.Column(db.String(10))
    semester = db.Column(db.Integer)

class KHS(db.Model):
    _tablename_ = 'khs'
    khs_id = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    kelas = db.Column(db.String(10))
    sifat = db.Column(db.String(20))
    sks = db.Column(db.Integer)
    nilai = db.Column(db.String(2))



class RencanaStudi(db.Model):
    _tablename_ = 'rencana_studi'
    krs_id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.nim'))
    semester = db.Column(db.String(10))
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    kelas = db.Column(db.String(10))
    sks = db.Column(db.Integer)
    keterangan = db.Column(db.Text)
    jadwal = db.Column(db.Text)

    mahasiswa = db.relationship('Mahasiswa', backref='rencana_studi', lazy=True)