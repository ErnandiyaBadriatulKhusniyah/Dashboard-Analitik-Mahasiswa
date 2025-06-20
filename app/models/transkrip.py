from . import db

class Transkrip(db.Model):
    __tablename__ = 'transkrip'
    transkrip_id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.nim'))
    kode_mk = db.Column(db.String(10), db.ForeignKey('mata_kuliah.kode_mk'))
    nama_mk = db.Column(db.Text)
    sks = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    huruf_mutu = db.Column(db.String(2))
    angka_mutu = db.Column(db.Numeric(4, 2))
    mutu = db.Column(db.Numeric(4, 2))
