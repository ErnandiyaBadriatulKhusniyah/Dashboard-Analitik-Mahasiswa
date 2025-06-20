from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, Fakultas, Mahasiswa
from auth.token import token_required

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
        query = Mahasiswa.query
        filters = ['angkatan', 'status_studi', 'semester', 'dosen_wali_id', 'nim', 'nama']
        
        for f in filters:
            val = request.args.get(f, type=int if f in ['semester', 'dosen_wali_id'] else str)
            if val:
                if f == 'nama':
                    query = query.filter(Mahasiswa.nama.ilike(f"%{val}%"))
                else:
                    query = query.filter(getattr(Mahasiswa, f) == val)
        
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
        if not all(k in payload for k in ['nim', 'nama', 'angkatan']):
            return jsonify({'error': 'Missing required fields'}), 400
        m = Mahasiswa(nim=payload['nim'], nama=payload['nama'], angkatan=payload['angkatan'])
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
        m = Mahasiswa.query.get_or_404(nim)
        payload = request.json
        m.nim = payload.get('nim', m.nim)
        m.nama = payload.get('nama', m.nama)
        m.angkatan = payload.get('angkatan', m.angkatan)
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
