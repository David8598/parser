import json
import requests


def get_SHOTS_TARGET(game_result):
    for game in game_result['Value']:
        country = game['CN']
        comand1 = ['O1R']
        comand2 = ['O2R']
        try:
            bets = game["SC"]["ST"]
            for item in bets:
                match_info = item["Value"]
                for SHOTS_TARGET in match_info:
                    if SHOTS_TARGET["ID"] == 59:
<<<<<<< HEAD
                        SHOTS_on_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_on_TARGET_S2 = SHOTS_TARGET["S2"] 
                    if SHOTS_TARGET["ID"] == 60:
                        SHOTS_off_TARGET_S1 = SHOTS_TARGET["S1"]
                        SHOTS_off_TARGET_S2 = SHOTS_TARGET["S2"]                      
        except:
            print('nothing')
            # break
    print( "SHOTS_on_TARGET_S1:" + SHOTS_on_TARGET_S1 " SHOTS_on_TARGET_S2:"  + SHOTS_on_TARGET_S2 + " SHOTS_off_TARGET_S1:" + SHOTS_off_TARGET_S1 + " SHOTS_off_TARGET_S2:" + SHOTS_off_TARGET_S2 + country)        
=======
                       print(f"SHOTS on TARGET left {SHOTS_TARGET['S1']} \n SHOTS on TARGET right {SHOTS_TARGET['S2']}")

                    if SHOTS_TARGET["ID"] == 60:
                        print( f" SHOTS off TARGET left {SHOTS_TARGET['S1']} \n SHOTS off TARGET right {SHOTS_TARGET['S2']}" )                     
        except:
            print('nothing')
        # получаем страну
        country = game["CN"]
        print(country)  
        break
>>>>>>> 7bbc241041c05549f07372323cffc8b5510b61b3



def get_game(result):
    for game in result['Value']:
        champs = game['LI']
        print(champs)

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

        
        # break

        
        
        


def main():
    url = 'https://1xbit6.com/live/football/'
    # champs = url.split('/')[5].split('-')[0]
    # # print(champs)

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
    # get_SHOTS_TARGET(game_result)



if __name__ == '__main__':
    main()
    
