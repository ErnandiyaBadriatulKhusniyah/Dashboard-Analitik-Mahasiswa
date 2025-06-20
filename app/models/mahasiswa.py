from . import db

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'
    
    nim = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    angkatan = db.Column(db.Integer)
    kode_prodi = db.Column(db.String(4), db.ForeignKey('program_studi.kode_prodi'))

    transkrip = db.relationship('Transkrip', backref='mahasiswa', lazy=True)
    hasil_evaluasi = db.relationship('HasilEvaluasiStudi', backref='mahasiswa', lazy=True)
    rencana_studi = db.relationship('RencanaStudi', backref='mahasiswa', lazy=True)
