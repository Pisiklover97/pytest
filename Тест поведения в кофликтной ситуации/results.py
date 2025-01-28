from inst import scoring_keys

def calculate_results(user_answers):
    # Подсчитываем количество совпадений для каждого типа
    # рваопроласроплросла
    scores = {key: 0 for key in scoring_keys}

    for q_num, answer in user_answers:
        for category, keys in scoring_keys.items():
            if (q_num, answer) in keys:
                scores[category] += 1

    # Формируем текст результатов
    result_text = "Результаты:\n"
    for category, score in scores.items():
        result_text += f"{category}: {score}\n"

    return result_text
