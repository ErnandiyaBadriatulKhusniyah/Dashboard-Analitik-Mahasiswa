from . import db

class Fakultas(db.Model):
    __tablename__ = 'fakultas'
    kode_fakultas = db.Column(db.String(3), primary_key=True)
    nama_fakultas = db.Column(db.String(30))
    lokasi = db.Column(db.String(15))

    prodis = db.relationship('ProgramStudi', backref='fakultas', lazy=True)
