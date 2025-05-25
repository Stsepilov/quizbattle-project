import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { api } from '../api';
import {FinalWinner, QuizRound} from '../types';
import { useNavigate } from 'react-router-dom';

function QuizGame() {
  const { quizId } = useParams<{ quizId: string }>();
  const [round, setRound] = useState<QuizRound | FinalWinner | null>(null);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [globalStats, setGlobalStats] = useState<any[]>([]);
  const [quizStats, setQuizStats] = useState<any[]>([]);
  const navigate = useNavigate();

  const safeLoadNextRound = React.useCallback(() => {
    if (!quizId) return;

    setLoading(true);
    api.getQuizRound(quizId)
        .then((newRound) => {
          if (newRound) {
              setRound(newRound);
          } else {
            console.warn('Пустой раунд');
            setRound(null);
          }
        })
        .catch((error) => {
          console.error('Ошибка загрузки раунда:', error);
          setRound(null);
        })
        .finally(() => {
          setLoading(false);
        });
  }, [quizId]);

  useEffect(() => {
    if (quizId) {
      safeLoadNextRound();
    }
  }, [safeLoadNextRound]);

    useEffect(() => {
        if (round && 'message' in round && round.message === "Победитель определён") {
            console.log(round.top_3);
            setQuizStats(round.top_3);
        }
    }, [round]);

  const handleVote = async (optionId: string) => {
    if (!round) return;
    try {
      if ("battle_id" in round) {
        await api.submitVote(round.battle_id, optionId);
      }
      safeLoadNextRound();
    } catch (error) {
      console.error('Failed to submit vote:', error);
    }
  };

  const handleOpenStats = async () => {
      try {
          if (!quizId) return;

          const result = await api.getQuizResults(quizId);

          setGlobalStats(result.top_3_total);
          setIsModalOpen(true);
      } catch (error) {
          console.error('Ошибка загрузки статистики:', error);
      }
  };

  const handleCloseModal = () => {
      setIsModalOpen(false);
  };

  if (loading || !round) {
    return <div className="text-center">Loading round...</div>;
  }

  if ('message' in round && round.message === "Победитель определён") {
      return (
          <div className="text-center mt-10">
              <h2 className="mx-auto text-2xl font-bold mb-4">Победитель определён!</h2>
              <img
                  src={round.image_url}
                  alt="Победитель"
                  className="mx-auto rounded-lg shadow-md w-5/12 h-80 object-cover mb-6"
              />
              <div className="mx-auto flex flex-col items-center gap-4">
                  <button
                      onClick={handleOpenStats}
                      className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                  >
                      Посмотреть общий рейтинг
                  </button>
                  <button
                      onClick={() => navigate('/')}
                      className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                  >
                      Вернуться к списку квизов
                  </button>
              </div>
              {isModalOpen && (
                  <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
                      <div className="bg-white relative rounded-lg p-8 max-w-4xl w-full flex gap-8">
                          <div className="flex-1">
                              <h3 className="text-xl font-bold mb-4">Общая статистика</h3>
                              {globalStats.length ? (
                                  <ul className="space-y-2">
                                      {globalStats.map((item, idx) => (
                                          <li key={idx} className="flex items-center gap-4 border-b pb-2">
                                              <img
                                                  src={item.image_url}
                                                  alt={item.title}
                                                  className="w-12 h-12 rounded-full object-cover"
                                              />
                                              <div className="flex flex-col items-start">
                                                  <div className="font-semibold">{item.title}</div>
                                                  <div className="text-gray-500 text-sm">{item.wins} побед</div>
                                              </div>
                                          </li>
                                      ))}
                                  </ul>
                              ) : (
                                  <p>Нет данных.</p>
                              )}
                          </div>

                          <div className="flex-1">
                              <h3 className="text-xl font-bold mb-4">Статистика квиза</h3>
                              {quizStats.length ? (
                                  <ul className="space-y-2">
                                      {quizStats.map((item, idx) => (
                                          <li key={idx} className="flex items-center gap-4 border-b pb-2">
                                              <img
                                                  src={item.image_url}
                                                  alt={item.title}
                                                  className="w-12 h-12 rounded-full object-cover"
                                              />
                                              <div className="font-semibold">{item.title}</div>
                                          </li>
                                      ))}
                                  </ul>
                              ) : (
                                  <p>Нет данных.</p>
                              )}
                          </div>
                          <button
                              onClick={handleCloseModal}
                              className="absolute top-4 right-4 text-gray-500 hover:text-gray-700 text-2xl font-bold"
                          >
                              ×
                          </button>
                      </div>
                  </div>
              )}
          </div>

      );
  }
    if ('items' in round && round.items) {
        return (
            <div className="max-w-5xl mx-auto">
                <div className="grid grid-cols-2 gap-8">
                    {round.items.map((item) => (
                        <button
                            key={item.id}
                            onClick={() => handleVote(item.id)}
                            className="bg-white rounded-lg shadow-md hover:shadow-lg transition-all transform hover:scale-105"
                        >
                            <div className="w-full h-80 overflow-hidden rounded-t-lg">
                                <img
                                    src={item.image_url}
                                    alt={item.title}
                                    className="w-full h-full object-cover rounded-t-lg"
                                />
                            </div>
                            <div className="p-4">
                                <h3 className="text-lg font-semibold text-gray-900">{item.title}</h3>
                            </div>
                        </button>
                    ))}
                </div>
            </div>
        );
    }
}

export default QuizGame;