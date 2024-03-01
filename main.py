import json
import requests
from datetime import datetime
from telegram import send_telegram


def get_message(shots_target):             #создаем ответ в тг 
    timestemp = shots_target['S']
    game_date = datetime.fromtimestamp(timestemp).strftime('%d.%m %H:%M')
    country, league, team_1, team_2, time_S, shots_on_T1, shots_on_T2, shots_off_T1, shots_off_T2, dif = shots_target.values()
    # формируем сообщение для тг 
    massege = f'{league}({game_date})\n' \
                f'{team_1} - {team_2}\n' \
                f'\n' \
                f'on {shots_on_T1} - {shots_on_T2}\n' \
                f'off {shots_off_T1} - {shots_off_T2}'     
   
    send_telegram(massege)            
    
                
# def search_db(game_id, shots_target):
#     with open ('db.txt', 'r' ) as file:
#         for item in file.readlines():
#             line = item.strip()
#             if int(float(line)) != game_id:
#                 print("id со списка" + int(float(line)))
#                 print("id с запроса" + game_id)
#                 get_message(shots_target)
#     with open ('db.txt', 'a' ) as file:
#         file.write(f'\n{game_id}')     
def search_db(game_id, shots_target):
    with open ('db.txt', 'r' ) as file:
        if file.read() != game_id:
            get_message(shots_target)
            with open ('db.txt', 'a' ) as f:
                f.write(f'\n{game_id}')


def get_SHOTS_TARGET(game_result):
        game = game_result['Value']
        shots_target = {}                  #здесь храняться все файлы которые получили из json игры 
        shots_target['CN'] = game["CN"]
        shots_target['L']= game["L"]
        shots_target['COM1'] = game["O1"]
        shots_target['COM2'] = game["O2"]
        shots_target['S'] = game['S']
                
        try:
            bets = game["SC"]["ST"]         #парсим json который получили 
            for item in bets:
                match_info = item["Value"]
                for SHOTS_TARGET in match_info:
                    if SHOTS_TARGET["ID"] == 59:
                        SHOTS_on_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_on_TARGET_S2 = SHOTS_TARGET["S2"] 
                    if SHOTS_TARGET["ID"] == 60:
                        SHOTS_off_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_off_TARGET_S2 = SHOTS_TARGET["S2"]
                shots_target['ONS1'] = SHOTS_on_TARGET_S1
                shots_target['ONS2'] = SHOTS_on_TARGET_S2
                shots_target['OFFS1'] = SHOTS_off_TARGET_S1
                shots_target['OFFS2'] = SHOTS_off_TARGET_S2         
        except: 
            print()
        try:
            shots_On_numS1 = int(SHOTS_on_TARGET_S1)
            shots_On_numS2 = int(SHOTS_on_TARGET_S2)
            difference = abs(shots_On_numS1 - shots_On_numS2)  
            shots_target['DIFf'] = difference
        except:  
            print()
        game_id = game['I']    
        search_db(game_id, shots_target)

        

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
    
