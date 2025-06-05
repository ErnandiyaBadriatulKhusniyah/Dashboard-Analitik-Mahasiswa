import { Route, useLocation, Routes } from 'react-router'
import './assets/css/main.css'
import Login from './page/Login';

function App() {
  const location = useLocation();
  return (
    <Routes key={location.pathname} location={location}>
      <Route path='/login' element={<Login />} />
    </Routes>
  )
}

export default App
