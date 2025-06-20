from . import db

class RencanaStudi(db.Model):
    __tablename__ = 'rencana_studi'
    krs_id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.nim'))
    semester = db.Column(db.String(10))
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    kelas = db.Column(db.String(10))
    sks = db.Column(db.Integer)
    keterangan = db.Column(db.Text)
    jadwal = db.Column(db.Text)
