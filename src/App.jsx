import { Route, useLocation, Routes } from 'react-router'
import './assets/css/main.css'
import Login from './page/Login';
import Dashboard from './page/Dashboard';

function App() {
  const location = useLocation();
  return (
    <Routes key={location.pathname} location={location}>
      <Route path='/login' element={<Login />} />
      <Route path='/dashboard' element={<Dashboard />} />
    </Routes>
  )
}

export default App
