from flask import Blueprint, jsonify, request
from app.models import db, RekomendasiAkademik, KurikulumMataKuliah, Transkrip
from datetime import datetime
from app.routes.auth import token_required

bp = Blueprint('api', __name__)

# Rekomendasi Akademik
@bp.route('/mahasiswa/<int:nim>/rekomendasi', methods=['POST'])
@token_required
def add_rekomendasi(current_user, nim):
    try:
        data = request.json
        rekom = RekomendasiAkademik(
            dosen_wali_id=data['dosen_wali_id'],
            nim=nim,
            semester=data['semester'],
            isi_rekomendasi=data['isi_rekomendasi'],
            tanggal=datetime.now()
        )
        db.session.add(rekom)
        db.session.commit()
        return jsonify({'message': 'Rekomendasi ditambahkan'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@bp.route('/mahasiswa/<int:nim>/rekomendasi', methods=['GET'])
@token_required
def get_rekomendasi(current_user, nim):
    rekoms = RekomendasiAkademik.query.filter_by(nim=nim).all()
    result = []
    for r in rekoms:
        result.append({
            'semester': r.semester,
            'isi_rekomendasi': r.isi_rekomendasi,
            'tanggal': r.tanggal.strftime('%Y-%m-%d')
        })
    return jsonify(result)

# Kurikulum
@bp.route('/kurikulum', methods=['POST'])
def add_kurikulum():
    data = request.json
    mk = KurikulumMataKuliah(
        kode_mk=data['kode_mk'],
        nama_mk=data['nama_mk'],
        sifat=data['sifat'],
        sks=data['sks'],
        kode_mk_prasyarat=data.get('kode_mk_prasyarat'),
        semester=data['semester']
    )
    db.session.add(mk)
    db.session.commit()
    return jsonify({'message': 'Mata kuliah ditambahkan'})

@bp.route('/kurikulum', methods=['GET'])
def get_kurikulum():
    daftar_mk = KurikulumMataKuliah.query.all()
    result = []
    for mk in daftar_mk:
        result.append({
            'kode_mk': mk.kode_mk,
            'nama_mk': mk.nama_mk,
            'sifat': mk.sifat,
            'sks': mk.sks,
            'prasyarat': mk.kode_mk_prasyarat,
            'semester': mk.semester
        })
    return jsonify(result)

# Transkrip
@bp.route('/mahasiswa/<int:nim>/transkrip', methods=['POST'])
@token_required
def add_transkrip(current_user, nim):
    try:
        data = request.json
        transkrip = Transkrip(
            nim=nim,
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=data['sks'],
            semester=data['semester'],
            huruf_mutu=data['huruf_mutu'],
            angka_mutu=data['angka_mutu'],
            mutu=data['sks'] * data['angka_mutu']  # Mutu = SKS * Angka Mutu
        )
        db.session.add(transkrip)
        db.session.commit()
        return jsonify({'message': 'Transkrip ditambahkan', 'id': transkrip.transkrip_id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@bp.route('/mahasiswa/<int:nim>/transkrip', methods=['GET'])
@token_required
def get_transkrip(current_user, nim):
    try:
        transkrips = Transkrip.query.filter_by(nim=nim).all()
        total_sks = 0
        total_mutu = 0
        result = []
        
        for t in transkrips:
            total_sks += t.sks
            total_mutu += t.mutu
            result.append({
                'kode_mk': t.kode_mk,
                'nama_mk': t.nama_mk,
                'sks': t.sks,
                'semester': t.semester,
                'huruf_mutu': t.huruf_mutu,
                'angka_mutu': t.angka_mutu,
                'mutu': round(t.mutu, 2)  # <-- dibulatkan 2 angka di belakang koma
            })
        
        ipk = total_mutu / total_sks if total_sks > 0 else 0
        
        return jsonify({
            'transkrip': result,
            'summary': {
                'total_sks': total_sks,
                'total_mutu': round(total_mutu, 2),  # <-- dibulatkan 2 angka di belakang koma
                'ipk': round(ipk, 2)                 # <-- dibulatkan 2 angka di belakang koma
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
