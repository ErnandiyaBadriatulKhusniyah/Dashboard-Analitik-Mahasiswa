import { Route, useLocation, Routes } from 'react-router'
import './assets/css/main.css'
import Login from './page/Login';
import Mahasiswa from './page/Mahasiswa';

function App() {
  const location = useLocation();
  return (
    <Routes key={location.pathname} location={location}>
      <Route path='/login' element={<Login />} />
      <Route path='/mahasiswa' element={<Mahasiswa />} />
    </Routes>
  )
}

export default App;
