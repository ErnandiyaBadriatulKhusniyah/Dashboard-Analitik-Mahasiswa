from . import db

class ProgramStudi(db.Model):
    __tablename__ = 'program_studi'
    kode_prodi = db.Column(db.String(4), primary_key=True)
    nama_prodi = db.Column(db.String(100))
    kode_fakultas = db.Column(db.String(3), db.ForeignKey('fakultas.kode_fakultas'))

    mahasiswa = db.relationship('Mahasiswa', backref='program_studi', lazy=True)
