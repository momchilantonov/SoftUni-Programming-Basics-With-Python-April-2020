exam_hour = int(input())  # час на изпита - цяло число от 0 до 23
exam_minutes = int(input())  # минути на изпита - цяло число от 0 до 59
hour_of_arrival = int(input())  # час на пристигане - цяло число от 0 до 23
minutes_of_arrival = int(input())  # минути на пристигане - цяло число от 0 до 59

time_in_minutes_exam = exam_hour * 60+exam_minutes  # часовете и минутите на изпита в минути
time_in_minutes_arrival = hour_of_arrival * 60+minutes_of_arrival  # часовете и минутите на пристигане в минути

if time_in_minutes_arrival > time_in_minutes_exam:  # проверка при закъснение
    print('Late')  # отпечатваме закъснение
    minutes_after_exam = (time_in_minutes_arrival-time_in_minutes_exam) % 60  # обръщане на минути
    hour_after_exam = (time_in_minutes_arrival-time_in_minutes_exam) // 60  # обръщане на часове
    if time_in_minutes_arrival <= time_in_minutes_exam+59:  # проверка ако няма завършен час
        print(f'{minutes_after_exam} minutes after the start')  # принтираме минути закъснение
    else:  # проверка ако има завършен час
        if minutes_after_exam < 10:  # проверка ако минутите са под 10 (да отпечата 0 преди минути < 10)
            print(f'{hour_after_exam}:0{minutes_after_exam} hours after the start')  # отпечатва час и минути закъснение
        else:  # проверка ако минутите са над 10
            print(f'{hour_after_exam}:{minutes_after_exam} hours after the start')  # отпечатва час и минути закъснение
elif time_in_minutes_exam-30 <= time_in_minutes_arrival <= time_in_minutes_exam:  # проверка за приситгане на време
    print('On time')  # отпечатваме пристигане на време
    minutes_before_exam = (time_in_minutes_exam-time_in_minutes_arrival) % 60  # обръщане на минути
    if time_in_minutes_arrival != time_in_minutes_exam:  # проверка за еднаквост (ако са да не отпечатва минути)
        print(f'{minutes_before_exam} minutes before the start')  # отпечатва до 30 мин преди изпита
elif time_in_minutes_arrival < time_in_minutes_exam-30:  # проверка при подраняване
    print('Early')  # отпечатва подраняване
    minutes_before_exam = (time_in_minutes_exam-time_in_minutes_arrival) % 60  # обръщане на минути
    hour_before_exam = (time_in_minutes_exam-time_in_minutes_arrival) // 60  # обръщане на часове
    if time_in_minutes_exam <= time_in_minutes_arrival+59:  # проверка ако няма завършен час
        print(f'{minutes_before_exam} minutes before the start')  # отпечатва минути подраняване
    else:  # проверка ако има завършен час
        if minutes_before_exam < 10:  # проверка ако минутите са под 10 (да отпечата 0 преди минути < 10)
            print(f'{hour_before_exam}:0{minutes_before_exam} hours before the start')  # отпечатва
        else:  # проверка ако минутите са над 10
            print(f'{hour_before_exam}:{minutes_before_exam} hours before the start')  # отпечатва
