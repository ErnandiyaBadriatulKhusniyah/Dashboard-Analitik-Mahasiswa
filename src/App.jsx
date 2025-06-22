import { Route, useLocation, Routes, Navigate } from 'react-router'
import './assets/css/main.css'
import MahasiswaNonAktif from './pages/MahasiswaNonAktif';
import MahasiswaAktif from './page/MahasiswaAktif';
import InputDanEvaluasi from './pages/InputDanEvaluasi';
import Statistik from './pages/Statistik';
import Login from './pages/Login';
import Mahasiswa from './pages/Mahasiswa';
import Dashboard from './pages/Dashboard';

function App() {
  const location = useLocation();
  return (
    <Routes key={location.pathname} location={location}>
      <Route path='/' element={<Navigate to="/dashboard" replace />} />
      <Route path='/login' element={<Login />} />
      <Route path='/mahasiswa' element={<Mahasiswa />} />
      <Route path='/dashboard' element={<Dashboard />} />
      <Route path='/mahasiswaNonAktif' element={<MahasiswaNonAktif />} />
      <Route path='/mahasiswaAktif' element={<MahasiswaAktif />} />
      <Route path='/input' element={<InputDanEvaluasi />} />
      <Route path='/statistik' element={<Statistik />} />
    </Routes>
  )
}

export default App;
