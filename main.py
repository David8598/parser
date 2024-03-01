import json
import requests
from datetime import datetime
from telegram import send_telegram


def get_message(shots_target):             #создаем ответ в тг 
    timestemp = shots_target['S']
    game_date = datetime.fromtimestamp(timestemp).strftime('%d.%m %H:%M')
    country, league, team_1, team_2, time_S, id, shots_on_T1, shots_on_T2, shots_off_T1, shots_off_T2, dif = shots_target.values()
    # формируем сообщение для тг 
    massege = f'{league}({game_date})\n' \
                f'{team_1} - {team_2}\n' \
                f'\n' \
                f'on {shots_on_T1} - {shots_on_T2}\n' \
                f'off {shots_off_T1} - {shots_off_T2}'        
    print(massege)
    send_telegram(massege)            
    
                
     
# def search_db(game_id, shots_target):
#     with open ('db.txt', 'r'  ) as file:
#         for item in file.readlines():
#             line = item.strip()
#             if int(line) != game_id:
#                 get_message(shots_target)
#         with open ('db.txt', 'a' ) as file:
#             file.write(f'\n{game_id}')




def sort_data(shots_target):
    try:
        if abs(int(shots_target['ONS1']) - int(shots_target['ONS2']))  > 4: 
            # print(abs(int(shots_target['ONS1']) - int(shots_target['ONS2'])))
            # print(abs(int(shots_target['OFFS1']) - int(shots_target['OFFS2'])))
            get_message(shots_target)
        elif abs(int(shots_target['OFFS1']) - int(shots_target['OFFS2'])) > 4:
            #  print(abs(int(shots_target['ONS1']) - int(shots_target['ONS2'])))
            #  print(abs(int(shots_target['OFFS1']) - int(shots_target['OFFS2'])))
             get_message(shots_target)
        else:
            # print(shots_target['I'])
            pass
    except:
        # print(shots_target['I'])
         pass
    

            # abs(int(shots_target['OFFS1']) - int(shots_target['OFFS2']))
        # diference_on_target = abs(int(shots_target['ONS1']) - int(shots_target['ONS2']))
        # diference_off_target = abs(int(shots_target['OFFS1']) - int(shots_target['OFFS2']))


def get_SHOTS_TARGET(game_result):
        game = game_result['Value']
        shots_target = {}  
        try:                #здесь храняться все файлы которые получили из json игры 
            shots_target['CN'] = game["CN"]
        except:
            shots_target['CN'] = '-'
        shots_target['L']= game["L"]
        shots_target['COM1'] = game["O1"]
        shots_target['COM2'] = game["O2"]
        shots_target['S'] = game['S']
        shots_target['I'] = game['I']
        try:
            bets = game["SC"]["ST"]         #парсим json который получили 
            for item in bets:
                match_info = item["Value"]
                for SHOTS_TARGET in match_info:
                        if SHOTS_TARGET["ID"] == 59:
                            try:
                                shots_target['ONS1'] = SHOTS_TARGET["S1"]
                                shots_target['ONS2'] = SHOTS_TARGET["S2"] 
                            except:
                                 shots_target['ONS1'] = "0"
                                 shots_target['ONS2'] = "0"
                        if SHOTS_TARGET["ID"] == 60:
                            try:
                                shots_target['OFFS1'] = SHOTS_TARGET["S1"]
                                shots_target['OFFS2'] = SHOTS_TARGET["S2"]
                            except:
                                 shots_target['OFFS1'] = "0"
                                 shots_target['OFFS2'] = "0"

        except: 
            pass
        sort_data(shots_target)
        # search_db(game_id, shots_target)

        

def get_game(result):                         # проходимся по всем матчам 
    for game in result['Value']:
        champs = game['I']
        # print(champs)

        params = (
            ('id', champs),
            ('lng', 'ru'),
            ('isSubGames', 'true'),
            ('GroupEvents', 'true'),
            ('allEventsGroupSubGames', 'true'),
           ('countevents', '250'),
            ('partner', '65'),
            ('country', '2'),
            ('fcountry', '2'),
            ('marketType', '1'),
            ('gr', '29'),
            ('isNewBuilder', 'true'),
            )

        response = requests.get('https://1xbit-ua.com/LiveFeed/GetGameZip?', params=params)
        game_result = response.json()
        get_SHOTS_TARGET(game_result)
        # break
        

def main(): #достаем json с сайта 
    params = (
    ('sports', '1'),  
    ('count', '50'),
    ('gr', '29'),
    ('mode', '4'),
    ('country', '2'),
    ('partner', '65'),
    ('getEmpty', 'true'),
    )

    response = requests.get('https://1xbit6.com/LiveFeed/Get1x2_VZip', params=params)
    result = response.json()
    get_game(result)  

if __name__ == '__main__':
    main()
    
