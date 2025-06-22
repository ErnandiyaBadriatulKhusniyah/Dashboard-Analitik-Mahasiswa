import { Route, useLocation, Routes, Navigate } from 'react-router'
import './assets/css/main.css'
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
    </Routes>
  )
}

export default App;
