import Sidebar from './components/Sidebar'
import Header from './components/Header'
import Calculator from './components/Calculator'

function App() {
  return (
    <div className='bg-surface font-body text-on-surface antialiased'>
      <Sidebar />
      <main className='ml-64 min-h-screen'>
        <Header />
        <Calculator />
      </main>
    </div>
  )
}

export default App
