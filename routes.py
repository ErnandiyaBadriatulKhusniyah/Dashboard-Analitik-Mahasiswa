# routes.py
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app.models import db, Fakultas, Mahasiswa, MataKuliah, Kurikulum
from app.routes.auth import token_required

mahasiswa_bp = Blueprint('mahasiswa_bp', __name__)

@mahasiswa_bp.route('/')
def index():
    fakultas = Fakultas.query.all()
    return render_template('index.html', fakultas=fakultas)

@mahasiswa_bp.route('/fakultas/tambah', methods=['POST'])
def tambah_fakultas():
    kode = request.form['kode_fakultas']
    nama = request.form['nama_fakultas']
    lokasi = request.form['lokasi']

    fakultas_baru = Fakultas(kode_fakultas=kode, nama_fakultas=nama, lokasi=lokasi)
    db.session.add(fakultas_baru)
    db.session.commit()
    return redirect(url_for('mahasiswa_bp.index'))

@mahasiswa_bp.route('/mahasiswa', methods=['GET'])
@token_required
def get_mahasiswa(current_user):
    try:
        angkatan = request.args.get('angkatan')
        status_studi = request.args.get('status_studi')
        semester = request.args.get('semester', type=int)
        dosen_wali_id = request.args.get('dosen_wali_id', type=int)
        nim = request.args.get('nim')
        nama = request.args.get('nama')

        query = Mahasiswa.query

        if angkatan:
            query = query.filter_by(angkatan=angkatan)
        if status_studi:
            query = query.filter_by(status_studi=status_studi)
        if semester is not None:
            query = query.filter_by(semester=semester)
        if dosen_wali_id is not None:
            query = query.filter_by(dosen_wali_id=dosen_wali_id)
        if nim:
            query = query.filter_by(nim=nim)
        if nama:
            query = query.filter(Mahasiswa.nama.ilike(f"%{nama}%"))

        data = query.all()
        return jsonify([{
            "id": m.nim,
            "nama": m.nama,
            "nim": m.nim,
            "angkatan": m.angkatan,
            "semester": getattr(m, 'semester', None),
            "status_studi": getattr(m, 'status_studi', None),
            "dosen_wali_id": getattr(m, 'dosen_wali_id', None)
        } for m in data])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@mahasiswa_bp.route('/mahasiswa', methods=['POST'])
@token_required
def add_mahasiswa(current_user):
    try:
        payload = request.json
        required_fields = ['nim', 'nama', 'angkatan']
        if not all(key in payload for key in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        m = Mahasiswa(
            nim=payload['nim'],
            nama=payload['nama'],
            angkatan=payload['angkatan']
            # tambahkan field lain sesuai kebutuhan jika sudah ada di model
        )
        db.session.add(m)
        db.session.commit()
        return jsonify({'message': 'Mahasiswa created', 'id': m.nim}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@mahasiswa_bp.route('/mahasiswa/<int:nim>', methods=['PUT'])
@token_required
def update_mahasiswa(current_user, nim):
    try:
        payload = request.json
        m = Mahasiswa.query.get_or_404(nim)
        m.nim = payload.get('nim', m.nim)
        m.nama = payload.get('nama', m.nama)
        m.angkatan = payload.get('angkatan', m.angkatan)
        # tambahkan field lain sesuai kebutuhan
        db.session.commit()
        return jsonify({'message': 'Mahasiswa updated'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@mahasiswa_bp.route('/mahasiswa/<int:nim>', methods=['DELETE'])
@token_required
def delete_mahasiswa(current_user, nim):
    try:
        m = Mahasiswa.query.get_or_404(nim)
        db.session.delete(m)
        db.session.commit()
        return jsonify({'message': 'Mahasiswa deleted'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# --- CRUD MataKuliah ---
@mahasiswa_bp.route('/matakuliah', methods=['GET'])
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

@mahasiswa_bp.route('/matakuliah', methods=['POST'])
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

@mahasiswa_bp.route('/matakuliah/<string:kode_mk>', methods=['PUT'])
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

@mahasiswa_bp.route('/matakuliah/<string:kode_mk>', methods=['DELETE'])
@token_required
def delete_matakuliah(current_user, kode_mk):
    m = MataKuliah.query.get_or_404(kode_mk)
    db.session.delete(m)
    db.session.commit()
    return jsonify({'message': 'Mata kuliah deleted'})

# --- CRUD Kurikulum ---
@mahasiswa_bp.route('/kurikulum', methods=['GET'])
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

@mahasiswa_bp.route('/kurikulum', methods=['POST'])
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

@mahasiswa_bp.route('/kurikulum/<int:kode_kurikulum>', methods=['PUT'])
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

@mahasiswa_bp.route('/kurikulum/<int:kode_kurikulum>', methods=['DELETE'])
@token_required
def delete_kurikulum(current_user, kode_kurikulum):
    k = Kurikulum.query.get_or_404(kode_kurikulum)
    db.session.delete(k)
    db.session.commit()
    return jsonify({'message': 'Kurikulum deleted'})
