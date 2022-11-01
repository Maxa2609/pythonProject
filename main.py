import telebot, random, datetime, pickle
from telebot import types

with open('data.txt', 'rb') as file:
    statistics = pickle.load(file)
    print(statistics)


token = '5619483761:AAG02UBWBIrnZ1dq_hy9r05VPqySov-dH3Q'
bot = telebot.TeleBot(token)

def iq(board):
    global b
    for s in list:
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == s and board[i][2] == '◻':
                b = [i, 2]
                return True
            elif board[i][2] == board[i][1] and board[i][1] == s and board[i][0] == '◻':
                b = [i, 0]
                return True
            elif board[i][2] == board[i][0] and board[i][0] == s and board[i][1] == '◻':
                b = [i, 1]
                return True
            elif board[0][i] == board[1][i] and board[0][i] == s and board[2][i] == '◻':
                b = [2, i]
                return True
            elif board[2][i] == board[1][i] and board[2][i] == s and board[0][i] == '◻':
                b = [0, i]
                return True
            elif board[0][i] == board[2][i] and board[0][i] == s and board[1][i] == '◻':
                b = [1, i]
                return True
            elif board[0][0] == board[1][1] and board[0][0] == s and board[2][2] == '◻':
                b = [2, 2]
                return True
            elif board[2][2] == board[1][1] and board[1][1] == s and board[0][0] == '◻':
                b = [0, 0]
                return True
            elif board[0][0] == board[2][2] and board[0][0] == s and board[1][1] == '◻':
                b = [1, 1]
                return True
            elif board[0][2] == board[1][1] and board[0][2] == s and board[2][0] == '◻':
                b = [2, 0]
                return True
            elif board[2][0] == board[1][1] and board[2][0] == s and board[0][2] == '◻':
                b = [0, 2]
                return True
            elif board[0][2] == board[2][0] and board[2][0] == s and board[1][1] == '◻':
                b = [1, 1]
                return True
    return False

def check_win(board):
    global a
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][0] != '◻':
            a = board[i][0]
            return True
        elif board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[0][i] != '◻':
            a = board[0][i]
            return True
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]!='◻':
            a = board[1][1]
            return True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1]!='◻':
            a = board[1][1]
            return True
    if board[0][0] != '◻' and board[0][1] != '◻' and board[0][2] != '◻' and board[1][0] != '◻' and board[1][
        1] != '◻' and board[1][2] != '◻' and board[2][0] != '◻' and board[2][1] != '◻' and board[2][2] != '◻':
        return None
    return False

def make_board(end=False, draw=False):
    if end:
        dt = datetime.datetime.now()
        hour = (int(dt.strftime('%H'))+3)
        dt_string = dt.strftime(f"Дата: %d/%m/%Y  Час: {hour}:%M:%S")
        print('Кінець. ', dt_string)
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        n=-1
        for i in statistics:
            n+=1
            if i['id_of_user'] == id_of_user:
                statistics[n]['games'] +=1
        if draw:
            txt = 'Нічия!'
            n = -1
            for i in statistics:
                n += 1
                if i['id_of_user'] == id_of_user:
                    statistics[n]['draws'] += 1
                    with open('data.txt', 'wb') as file:
                        pickle.dump(statistics, file)
        else:
            if symbol == a:
                txt = 'Кінець! Ти вийграв у бота, вітаю 👍'
                n = -1
                for i in statistics:
                    n += 1
                    if i['id_of_user'] == id_of_user:
                        statistics[n]['wins'] += 1
                        with open('data.txt', 'wb') as file:
                            pickle.dump(statistics, file)
            else:
                txt = 'Кінець! Бот вийграв тебе 🙁'
                n = -1
                for i in statistics:
                    n += 1
                    if i['id_of_user'] == id_of_user:
                        statistics[n]['losses'] += 1
                        with open('data.txt', 'wb') as file:
                            pickle.dump(statistics, file)
        b1 = types.InlineKeyboardButton(text=txt, callback_data=102)
        keyboard.add(b1)
        return keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text=board[0][0], callback_data=1)
    b2 = types.InlineKeyboardButton(text=board[0][1], callback_data=2)
    b3 = types.InlineKeyboardButton(text=board[0][2], callback_data=3)
    b4 = types.InlineKeyboardButton(text=board[1][0], callback_data=4)
    b5 = types.InlineKeyboardButton(text=board[1][1], callback_data=5)
    b6 = types.InlineKeyboardButton(text=board[1][2], callback_data=6)
    b7 = types.InlineKeyboardButton(text=board[2][0], callback_data=7)
    b8 = types.InlineKeyboardButton(text=board[2][1], callback_data=8)
    b9 = types.InlineKeyboardButton(text=board[2][2], callback_data=9)
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    global board, start_game, id_of_user
    id_of_user = f'{message.from_user.id}'
    availability = False
    for i in statistics:
        if i['id_of_user'] == id_of_user:
            availability = True
    if availability == False:
        statistics.append({'id_of_user':id_of_user,"games":0,"wins":0,"draws":0,"losses":0})
        with open('data.txt', 'wb') as file:
            pickle.dump(statistics, file)
    board = [['◻'] * 3 for i in range(3)]
    markup = types.InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text='Дуже легко', callback_data='eazy')
    a2 = types.InlineKeyboardButton(text='Нормально', callback_data='normal')
    a3 = types.InlineKeyboardButton(text='Неможливо', callback_data='impossible')
    markup.add(a1, a2, a3)
    print('{0.first_name} /start'.format(message.from_user))
    start_game = bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}! Обери складність: ',
                                  reply_markup=markup)

def symbol_choose(call):
    button = types.InlineKeyboardMarkup()
    c1 = types.InlineKeyboardButton(text='❌', callback_data='❌')
    c2 = types.InlineKeyboardButton(text='⭕', callback_data='⭕')
    button.add(c1, c2)
    bot.edit_message_text('Обери символ, за який будеш грати:', chat_id=call.message.chat.id, message_id=start_game.id)
    bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id, reply_markup=button)

def go(call):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, x, y
    if symbol == '⭕':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        board[x][y] = '❌'
        bot.edit_message_text(text='Граймо! 🎲', chat_id=call.message.chat.id, message_id=start_game.id)
        bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id, reply_markup=make_board())
        if check_win(board) == None or check_win(board) == True:
            if check_win(board) == None:
                draw = True
            else:
                draw = False
            bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id,
                                          reply_markup=make_board(end=True, draw=draw))
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        b1 = types.InlineKeyboardButton(text='◻', callback_data=1)
        b2 = types.InlineKeyboardButton(text='◻', callback_data=2)
        b3 = types.InlineKeyboardButton(text='◻', callback_data=3)
        b4 = types.InlineKeyboardButton(text='◻', callback_data=4)
        b5 = types.InlineKeyboardButton(text='◻', callback_data=5)
        b6 = types.InlineKeyboardButton(text='◻', callback_data=6)
        b7 = types.InlineKeyboardButton(text='◻', callback_data=7)
        b8 = types.InlineKeyboardButton(text='◻', callback_data=8)
        b9 = types.InlineKeyboardButton(text='◻', callback_data=9)
        keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        bot.edit_message_text(text='Граймо! 🎲', chat_id=call.message.chat.id, message_id=start_game.id)
        bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id, reply_markup=keyboard)

@bot.message_handler(commands=['statistics'])
def st(message):
    global id_of_user
    print('{0.first_name} /st'.format(message.from_user))
    id_of_user = f'{message.from_user.id}'
    availability = False
    for i in statistics:
        if i['id_of_user'] == id_of_user:
            availability = True
    if availability == False:
        statistics.append({'id_of_user': id_of_user, "games": 0, "wins": 0, "draws": 0, "losses": 0})
        with open('data.txt', 'wb') as file:
            pickle.dump(statistics, file)
    for i in statistics:
        if i['id_of_user'] == id_of_user:
            print(f'ID: {i["id_of_user"]}. Games: {i["games"]}. Wins: {i["wins"]}. Draws: {i["draws"]}. Losses: {i["losses"]}.')
            bot.send_message(message.chat.id,
            f'''Твоя статистика:

Ігри - {i['games']}
Перемоги - {i['wins']}
Нічиї - {i['draws']}
Програші - {i['losses']}''')

@bot.message_handler(commands=['clear'])
def clear(message):
    global id_of_user
    print('{0.first_name} /clear'.format(message.from_user))
    id_of_user = f'{message.from_user.id}'
    availability = False
    for i in statistics:
        if i['id_of_user'] == id_of_user:
            availability = True
    if availability == False:
        statistics.append({'id_of_user': id_of_user, "games": 0, "wins": 0, "draws": 0, "losses": 0})
        with open('data.txt', 'wb') as file:
            pickle.dump(statistics, file)
    n = -1
    for i in statistics:
        n += 1
        if i['id_of_user'] == id_of_user:
            if i['games'] == 0:
                bot.send_message(message.chat.id, 'Твоя статистика і так пуста 😦')
            else:
                statistics[n] = {'id_of_user': id_of_user, "games": 0, "wins": 0, "draws": 0, "losses": 0}
                with open('data.txt', 'wb') as file:
                    pickle.dump(statistics, file)
                print(f'Статистика успішно обнулена!')
                bot.send_message(message.chat.id, 'Статистика успішно обнулена!')

@bot.message_handler(content_types=["text"])
def text(message):
    hello = 'Привіт!'
    txt = '\n\nОбери одну з поданих команд:'
    commands = '\n\n/start - розпочати гру\n/statistics - побачити свою статистику\n/clear - обнулити свою статистику'
    bot.send_message(message.chat.id, f'{hello} {txt} {commands}')

def bot_move():
    global x, y
    if skl != 0:
        if iq(board) == True:
            x = b[0]
            y = b[1]
        else:
            while board[x][y] != '◻':
                x = random.randint(0, 2)
                y = random.randint(0, 2)
    else:
        while board[x][y] != '◻':
            x = random.randint(0, 2)
            y = random.randint(0, 2)

def bot_impossible():
    global x, y, ugol_ugol, ugol_centre_storoni, centre_ugol
    if iq(board) == True:
        x = b[0]
        y = b[1]
    else:
        if bot_symbol == '❌':
            if hod == 1:
                if board[0][0] == '❌' or board[0][2] == '❌' or board[2][0] == '❌' or board[2][2] == '❌':
                    if board[0][0] == '⭕' or board[0][2] == '⭕' or board[2][0] == '⭕' or board[2][2] == '⭕':
                        ugol_ugol = True
                        while board[x][y] != '◻':
                            rand = random.randint(1, 4)
                            if rand == 1:
                                x = 0
                                y = 0
                            elif rand == 2:
                                x = 0
                                y = 2
                            elif rand == 3:
                                x = 2
                                y = 0
                            elif rand == 4:
                                x = 2
                                y = 2
                    elif board[1][1] == '⭕':
                        ugol_centre = True
                        if board[0][0] == '❌':
                            x = 2
                            y = 2
                        elif board[0][2] == '❌':
                            x = 2
                            y = 0
                        elif board[2][0] == '❌':
                            x = 0
                            y = 2
                        elif board[2][2] == '❌':
                            x = 0
                            y = 0
                    elif board[0][1] == '⭕' or board[1][0] == '⭕' or board[1][2] == '⭕' or board[2][1] == '⭕':
                        ugol_centre_storoni = True
                        if board[0][0] == '❌' and board[0][1] == '⭕':
                            x = 2
                            y = 0
                        elif board[0][0] == '❌' and board[1][0] == '⭕':
                            x = 0
                            y = 2
                        elif board[0][0] == '❌' and (board[1][2] == '⭕' or board[2][1] == '⭕'):
                            while (x != 0 or y != 2) and (x != 2 or y != 0):
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                        elif board[0][2] == '❌' and board[0][1] == '⭕':
                            x = 2
                            y = 2
                        elif board[0][2] == '❌' and board[1][2] == '⭕':
                            x = 0
                            y = 0
                        elif board[0][2] == '❌' and (board[1][0] == '⭕' or board[2][1]):
                            while (x != 0 or y != 0) and (x != 2 or y != 2):
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                        elif board[2][0] == '❌' and board[1][0]:
                            x = 2
                            y = 2
                        elif board[2][0] == '❌' and board[2][1]:
                            x = 0
                            y = 0
                        elif board[2][0] == '❌' and (board[0][1] == '⭕' or board[1][2]):
                            while (x != 0 or y != 0) and (x != 2 or y != 2):
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                        elif board[2][2] == '❌' and board[2][1] == '⭕':
                            x = 0
                            y = 2
                        elif board[2][2] == '❌' and board[1][2] == '⭕':
                            x = 2
                            y = 0
                        elif board[2][2] == '❌' and (board[1][0] == '⭕' or board[0][1] == '⭕'):
                            while (x != 0 or y != 2) and (x != 2 or y != 0):
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                elif board[1][1] == '❌':
                    if board[0][0] == '⭕' or board[0][2] == '⭕' or board[2][0] == '⭕' or board[2][2] == '⭕':
                        centre_ugol = True
                        if board[0][0] == '⭕':
                            x = 2
                            y = 2
                        elif board[0][2] == '⭕':
                            x = 2
                            y = 0
                        elif board[2][0] == '⭕':
                            x = 0
                            y = 2
                        elif board[2][2] == '⭕':
                            x = 0
                            y = 0
                    elif board[0][1] == '⭕' or board[1][0] == '⭕' or board[1][2] == '⭕' or board[2][1] == '⭕':
                        if board[0][1] == '⭕':
                            x = 2
                            y = 2
                        elif board[1][0] == '⭕':
                            x = 0
                            y = 2
                        elif board[1][2] == '⭕':
                            x = 2
                            y = 0
                        elif board[2][1] == '⭕':
                            x = 0
                            y = 0
            elif hod == 2:
                if ugol_ugol:
                    while board[x][y] != '◻':
                        rand = random.randint(1, 4)
                        if rand == 1:
                            x = 0
                            y = 0
                        elif rand == 2:
                            x = 0
                            y = 2
                        elif rand == 3:
                            x = 2
                            y = 0
                        elif rand == 4:
                            x = 2
                            y = 2
                elif ugol_centre_storoni:
                    x = 1
                    y = 1
                elif centre_ugol:
                    if (board[0][0] == '⭕' and board[2][1] == '⭕') or (board[2][2] == '⭕' and board[1][0] == '⭕'):
                        x = 0
                        y = 2
                    elif (board[0][0] == '⭕' and board[1][2] == '⭕') or (board[2][2] == '⭕' and board[0][1] == '⭕'):
                        x = 2
                        y = 0
                    elif (board[2][0] == '⭕' and board[1][2] == '⭕') or (board[0][2] == '⭕' and board[2][1] == '⭕'):
                        x = 0
                        y = 0
                    elif (board[2][0] == '⭕' and board[0][1] == '⭕') or (board[0][2] == '⭕' and board[1][0] == '⭕'):
                        x = 2
                        y = 2
                    else:
                        bot_move()
            else:
                bot_move()

def call_data(index1, index2, call):
    global x,y, hod
    if board[index1][index2] == '◻':
        board[index1][index2] = symbol
        bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id, reply_markup=make_board())
        if check_win(board) == True or check_win(board) == None:
            if check_win(board) == None:
                draw = True
            else:
                draw = False
            bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id,
                                          reply_markup=make_board(end=True, draw=draw))
        else:
            x = index1
            y = index2
            if skl == 0 or skl == 1:
                bot_move()
            else:
                hod += 1
                bot_impossible()
            board[x][y] = bot_symbol
            bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id,reply_markup=make_board())
            if check_win(board) == None or check_win(board) == True:
                if check_win(board) == None:
                    draw = True
                else:
                    draw = False
                bot.edit_message_reply_markup(call.message.chat.id, message_id=start_game.id,
                                              reply_markup=make_board(end=True, draw=draw))

    else:
        bot.answer_callback_query(callback_query_id=call.id, text='Ця клітинка вже зайнята!')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global skl, symbol, bot_symbol, list, hod, ugol_ugol, ugol_centre_storoni, ugol_centre
    if call.data == 'eazy':
        skl = 0
        symbol_choose(call=call)
    elif call.data == 'normal':
        skl = 1
        symbol_choose(call=call)
    elif call.data == 'impossible':
        ugol_ugol = False
        ugol_centre_storoni = False
        centre_ugol = False
        hod = 0
        skl = 2
        symbol_choose(call=call)
    elif call.data == '⭕':
        symbol = '⭕'
        bot_symbol = '❌'
        if skl == 0:
            list = [bot_symbol]
        else:
            list = [bot_symbol,symbol]
        go(call=call)
    elif call.data == '❌':
        symbol = '❌'
        bot_symbol = '⭕'
        if skl == 0:
            list = [bot_symbol]
        else:
            list = [bot_symbol, symbol]
        go(call=call)
    elif call.data == '1':
        call_data(0, 0, call=call)
    elif call.data == '2':
        call_data(0, 1, call=call)
    elif call.data == '3':
        call_data(0, 2, call=call)
    elif call.data == '4':
        call_data(1, 0, call=call)
    elif call.data == '5':
        call_data(1, 1, call=call)
    elif call.data == '6':
        call_data(1, 2, call=call)
    elif call.data == '7':
        call_data(2, 0, call=call)
    elif call.data == '8':
        call_data(2, 1, call=call)
    elif call.data == '9':
        call_data(2, 2, call=call)
    elif call.data == '102':
        bot.answer_callback_query(call.message.chat.id, 'Гра завершена!')

while True:
  try:
    bot.polling(non_stop=True)
  except Exception as _ex:
    print(_ex)
