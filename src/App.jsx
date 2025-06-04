import { Route, useLocation } from 'react-router'
import './assets/css/main.css'

function App() {
  const location = useLocation();
  return (
    <Routes location={location}>
      <Route path='/login' element={<Login to="/" />} />
    </Routes>
  )
}

export default App
