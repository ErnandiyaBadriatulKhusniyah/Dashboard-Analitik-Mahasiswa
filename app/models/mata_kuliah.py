from . import db

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'
    kode_mk = db.Column(db.String(10), primary_key=True)
    nama_mk = db.Column(db.Text)
    sifat = db.Column(db.String(20))
    kode_mk_prasyarat = db.Column(db.String(10))
    semester = db.Column(db.Integer)

    kurikulum = db.relationship('Kurikulum', backref='mata_kuliah', lazy=True)
    transkrip = db.relationship('Transkrip', backref='mata_kuliah', lazy=True)
    rencana_studi = db.relationship('RencanaStudi', backref='mata_kuliah', lazy=True)
    khs = db.relationship('KHS', backref='mata_kuliah', lazy=True)
