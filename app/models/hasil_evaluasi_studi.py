from . import db

class HasilEvaluasiStudi(db.Model):
    __tablename__ = 'hasil_evaluasi_studi'
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
