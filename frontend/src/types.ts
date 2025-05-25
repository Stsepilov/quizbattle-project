export interface Quiz {
  id: string;
  title: string;
  description: string;
  image_url: string;
}

export interface QuizOption {
  id: string;
  image_url: string;
  title: string;
}

export interface QuizRound {
  battle_id: string;
  items: [QuizOption, QuizOption];
}

export interface FinalWinner {
  message: string;
  winner_id: number;
  image_url: string;
  top_3: string[];
}

export interface QuizResults {
  // top_3_tournament: string[];
  top_3_total: string[];
}