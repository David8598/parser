import json
import requests

def get_SHOTS_TARGET(game_result):
    for game in game_result['Value']:
        country = game["CN"]
        league = game["L"]
        comand1 = game["O1"]
        comand2 = game["O2"]
        try:
            bets = game["SC"]["ST"]
            for item in bets:
                match_info = item["Value"]
                for SHOTS_TARGET in match_info:
                    if SHOTS_TARGET["ID"] == 59:
                        SHOTS_on_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_on_TARGET_S2 = SHOTS_TARGET["S2"] 
                    if SHOTS_TARGET["ID"] == 60:
                        SHOTS_off_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_off_TARGET_S2 = SHOTS_TARGET["S2"] 
        except:
            break
        try:
            shots_On_num1 = int(SHOTS_on_TARGET_S1)
            shots_On_num2 = int(SHOTS_on_TARGET_S2)
            print(abs(shots_On_num1 - shots_On_num2))
            # print( f"============\n{country}\n============\n{league}\n=============\n{comand1} vs {comand2}\n=============\nSHOTS_on_TARGET:\n{SHOTS_on_TARGET_S1} ======== {SHOTS_on_TARGET_S2} \n SHOTS_off_TARGET_:\n{SHOTS_off_TARGET_S1}  ======== {SHOTS_off_TARGET_S2}" )             
        except:  break 
        

def get_game(result):
    for game in result['Value']:
        champs = game['LI']
        # print(champs)

        params = (
            ('sports', '1'),
            ('champs', champs),
            ('count', '50'),
            ('gr', '29'),
            ('mode', '4'),
            ('country', '2'),
            ('partner', '65'),      
            ('getEmpty', 'true'),
            )

        response = requests.get('https://1xbit6.com/LiveFeed/Get1x2_VZip', params=params)
        game_result = response.json()
        get_SHOTS_TARGET(game_result)
        

def main():
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
    
