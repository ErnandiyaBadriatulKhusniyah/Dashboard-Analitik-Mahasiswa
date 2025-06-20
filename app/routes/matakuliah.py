from flask import Blueprint, request, jsonify
from models import db, MataKuliah, Kurikulum
from auth.token import token_required

matakuliah_bp = Blueprint('matakuliah_bp', __name__)

@matakuliah_bp.route('/matakuliah', methods=['GET'])
@token_required
def get_matakuliah(current_user):
    data = MataKuliah.query.all()
    return jsonify([{
        "kode_mk": m.kode_mk,
        "nama_mk": m.nama_mk,
        "sks": m.sks,
        "sifat": m.sifat,
        "semester": m.semester
    } for m in data])

@matakuliah_bp.route('/matakuliah', methods=['POST'])
@token_required
def add_matakuliah(current_user):
    payload = request.json
    m = MataKuliah(
        kode_mk=payload['kode_mk'],
        nama_mk=payload['nama_mk'],
        sks=payload['sks'],
        sifat=payload.get('sifat'),
        semester=payload.get('semester')
    )
    db.session.add(m)
    db.session.commit()
    return jsonify({'message': 'Mata kuliah created', 'kode_mk': m.kode_mk}), 201

@matakuliah_bp.route('/matakuliah/<string:kode_mk>', methods=['PUT'])
@token_required
def update_matakuliah(current_user, kode_mk):
    m = MataKuliah.query.get_or_404(kode_mk)
    payload = request.json
    m.nama_mk = payload.get('nama_mk', m.nama_mk)
    m.sks = payload.get('sks', m.sks)
    m.sifat = payload.get('sifat', m.sifat)
    m.semester = payload.get('semester', m.semester)
    db.session.commit()
    return jsonify({'message': 'Mata kuliah updated'})

@matakuliah_bp.route('/matakuliah/<string:kode_mk>', methods=['DELETE'])
@token_required
def delete_matakuliah(current_user, kode_mk):
    m = MataKuliah.query.get_or_404(kode_mk)
    db.session.delete(m)
    db.session.commit()
    return jsonify({'message': 'Mata kuliah deleted'})

# --- Kurikulum ---
@matakuliah_bp.route('/kurikulum', methods=['GET'])
@token_required
def get_kurikulum(current_user):
    data = Kurikulum.query.all()
    return jsonify([{
        "kode_kurikulum": k.kode_kurikulum,
        "kode_mk": k.kode_mk,
        "nama_mk": k.nama_mk,
        "kode_mk_prasyarat": k.kode_mk_prasyarat,
        "semester": k.semester
    } for k in data])


@matakuliah_bp.route('/kurikulum', methods=['POST'])
@token_required
def add_kurikulum(current_user):
    payload = request.json
    k = Kurikulum(
        kode_mk=payload['kode_mk'],
        nama_mk=payload['nama_mk'],
        kode_mk_prasyarat=payload.get('kode_mk_prasyarat'),
        semester=payload.get('semester')
    )
    db.session.add(k)
    db.session.commit()
    return jsonify({'message': 'Kurikulum created', 'kode_kurikulum': k.kode_kurikulum}), 201

@matakuliah_bp.route('/kurikulum/<int:kode_kurikulum>', methods=['PUT'])
@token_required
def update_kurikulum(current_user, kode_kurikulum):
    k = Kurikulum.query.get_or_404(kode_kurikulum)
    payload = request.json
    k.kode_mk = payload.get('kode_mk', k.kode_mk)
    k.nama_mk = payload.get('nama_mk', k.nama_mk)
    k.kode_mk_prasyarat = payload.get('kode_mk_prasyarat', k.kode_mk_prasyarat)
    k.semester = payload.get('semester', k.semester)
    db.session.commit()
    return jsonify({'message': 'Kurikulum updated'})

@matakuliah_bp.route('/kurikulum/<int:kode_kurikulum>', methods=['DELETE'])
@token_required
def delete_kurikulum(current_user, kode_kurikulum):
    k = Kurikulum.query.get_or_404(kode_kurikulum)
    db.session.delete(k)
    db.session.commit()
    return jsonify({'message': 'Kurikulum deleted'})
