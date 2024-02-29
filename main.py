import json
import requests


def get_SHOTS_ON_TARGET(game_result, game_id):
    for game in game_result['Value']:
        currend_id = game['I']
        if currend_id == game_id:
            bets = game["SC"]["ST"]
            for item in bets:
                k = item["Value"]
                for j in k:
                    if j["ID"] == 59:
                        print(j["S1"] + " " + j["S2"] )
                break
            
def get_SHOTS_OFF_TARGET(game_result, game_id):
    for game in game_result['Value']:
        currend_id = game['I']
        if currend_id == game_id:
            bets = game["SC"]["ST"]
            for item in bets:
                k = item["Value"]
                for j in k:
                    if j["ID"] == 60:
                        print(j["S1"] + " " + j["S2"] )
                break        

# def get_MATCH_NAME(game_result, game_id)



def get_game(result):
    
    for game in result['Value']:
        game_id = game['I']
        champs = game['LI']

        params = (
            ('sports', '1'),
            # ('champs', champs),
            ('count', '50'),
            ('gr', '29'),
            ('mode', '4'),
            # ('subGames', game_id),
            ('country', '2'),
            ('partner', '65'),      
            ('getEmpty', 'true'),
            )

        response = requests.get('https://1xbit6.com/LiveFeed/Get1x2_VZip', params=params)
        game_result = response.json()
        get_SHOTS_ON_TARGET(game_result , game_id)
        get_SHOTS_OFF_TARGET(game_result, game_id)

        
        break

        
        
        


def main():
    url = 'https://1xbit6.com/live/football/2048450-friendlies-u19-national-teams'
    champs = url.split('/')[5].split('-')[0]
    # print(champs)

    params = (
    ('sports', '1'),
    ('count', '50'),
    ('gr', '29'),
    ('mode', '4'),
    ('country', '2'),
    ('partner', '65'),
    ('getEmpty', 'true'),
    )

    response = requests.get('https://1xbit6.com/LiveFeed/Get1x2_VZip?', params=params)
    result = response.json()
    get_game(result)



if __name__ == '__main__':
    main()
    
