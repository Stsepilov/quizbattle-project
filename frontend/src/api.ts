import {Quiz, QuizRound, FinalWinner, QuizResults} from './types';

const API_BASE_URL = 'http://localhost:8080/api'; // Mock API URL
type QuizRoundResponse = QuizRound | FinalWinner;

export const api = {
  getQuizzes: async (): Promise<Quiz[]> => {
    // Mock data for now
    const response = await fetch(API_BASE_URL+'/quizzes', {
      method: 'GET',
    });
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
    const result = (await response.json());

    console.log('result is: ', JSON.stringify(result, null, 4));

    return result;
  },

  getQuizRound: async (quizId: string): Promise<QuizRoundResponse> => {
    // Mock data for now
    const response = await fetch(API_BASE_URL+'/battle/'+quizId, {
      method: 'GET',
    });
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
    const result = (await response.json());
    if (result.message === "Победитель определён") {
      return result;
    }
    else {
      console.log('result is: ', result);
      return result;
    }
  },

  submitVote: async (roundId: string, optionId: string): Promise<void> => {
    // Mock API call
    console.log(`Vote submitted for round ${roundId}, option ${optionId}`);
    const response = await fetch(API_BASE_URL+'/vote', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        winner_id: optionId,
        battle_id: roundId,
      }),
    });
    const data = await response.json();
    if (response.ok) {
      console.log('Голос учтен успешно:', data);
    } else {
      console.error('Ошибка голосования:', data.message);
    }
  },

  getQuizResults: async (quizId: string): Promise<QuizResults> => {
    // Mock data for now
    const response = await fetch(API_BASE_URL+'/quiz_results/'+quizId, {
      method: 'GET',
    });
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
    const result = (await response.json());

    console.log('result is: ', JSON.stringify(result, null, 4));

    return result;
  },
};