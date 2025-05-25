import { BrowserRouter, Routes, Route } from 'react-router-dom';
import QuizList from './components/QuizList';
import QuizGame from './components/QuizGame';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-100">
        <header className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto py-4 px-4">
            <h1 className="text-2xl font-bold text-gray-900">Quiz Battle</h1>
          </div>
        </header>
        <main className="max-w-7xl mx-auto py-6 px-4">
          <Routes>
            <Route path="/" element={<QuizList />} />
            <Route path="/quiz/:quizId" element={<QuizGame />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;