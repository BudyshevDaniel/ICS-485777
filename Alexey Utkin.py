answer = input ("Здравствуйте! Меня зовут Алексей Уткин. Хотите расскажу анекдот  ? Да,Нет:  ")
if answer == "Да":
    answer = input ("Сидит программист в баре, пьет пиво. К нему подходит девица:\n- Если хочешь хорошо отдохнуть сегодня, то меня зовут Бэтти...\n- А если я не хочу сегодня хорошо отдохнуть, то как тебя зовут?\n\n\n Ну как ? ")
    print ("Спасибо!)")
if answer == "Нет":
    answer = input ("А почему ? ")
    answer1 = input ("А может всё-таки рассказать ? Да,Нет: ")
    if answer1 == "Да":
       answer2 = input ("Сидит программист в баре, пьет пиво. К нему подходит девица:\n- Если хочешь хорошо отдохнуть сегодня, то меня зовут Бэтти...\n- А если я не хочу сегодня хорошо отдохнуть, то как тебя зовут?\n\n\n Ну как ? ")
       print ("Спасибо!")
    if answer1 == "Нет":
       print ("Ну тогда пока(")
    

