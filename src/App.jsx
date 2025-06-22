import { Route, useLocation, Routes, Navigate } from 'react-router'
import './assets/css/main.css'
<<<<<<< HEAD
import Login from './page/Login';
import Mahasiswa from './page/Mahasiswa';
import Dashboard from './page/Dashboard';
import MahasiswaNonAktif from './page/MahasiswaNonAktif';
import MahasiswaAktif from './page/MahasiswaAktif';
import InputDanEvaluasi from './page/InputDanEvaluasi';
import Statistik from './page/Statistik';
=======
import Login from './pages/Login';
import Mahasiswa from './pages/Mahasiswa';
import Dashboard from './pages/Dashboard';
>>>>>>> 065d2e40513a86f4af7422bb9b685c3f93bd2708

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
