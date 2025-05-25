import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api';
import { Quiz } from '../types';

function QuizList() {
  const [quizzes, setQuizzes] = useState<Quiz[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const data = await api.getQuizzes();
        setQuizzes(data);
      } catch (error) {
        console.error('Failed to fetch quizzes:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchQuizzes();
  }, []);

  if (loading) {
    return <div className="text-center">Loading quizzes...</div>;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
      {quizzes.map((quiz) => (
        <Link
          key={quiz.id}
          to={`/quiz/${quiz.id}`}
          className="block bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <div className="p-6 text-center">
            <h2 className="text-xl font-semibold text-gray-900">{quiz.title}</h2>
            <div className="mx-auto flex flex-col gap-6">
              <p className="mt-2 text-gray-600">{quiz.description}</p>
              <img
                  src={quiz.image_url}
                  alt={quiz.title}
                  className="mx-auto rounded-lg shadow-md w-full max-w-sm h-80 object-cover mb-6"
              />
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}

export default QuizList;