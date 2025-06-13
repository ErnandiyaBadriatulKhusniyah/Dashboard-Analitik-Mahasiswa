import { Route, useLocation, Routes } from 'react-router'
import './assets/css/main.css'
import Login from './page/Login';
import Mahasiswa from './page/Mahasiswa';
import Dashboard from './page/Dashboard';
import MahasiswaNonAktif from './page/MahasiswaNonAktif';
import MahasiswaAktif from './page/MahasiswaAktif';
import InputDanEvaluasi from './page/InputDanEvaluasi';
import Statistik from './page/Statistik';

function App() {
  const location = useLocation();
  return (
    <Routes key={location.pathname} location={location}>
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
