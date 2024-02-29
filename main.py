import json
import requests


def get_SHOTS_ON_TARGET(game_result):
        for game in game_result['Value']:
            bets = game["SC"]["ST"]
            for item in bets:
                k = item["Value"]
                for shot_on_target in k:
                    if shot_on_target["ID"] == 59:
                        print(shot_on_target["S1"] + " " + shot_on_target["S2"] )
                for shot_off_target in k:
                    if shot_off_target["ID"] == 60:
                        print(shot_off_target["S1"] + " " + shot_off_target["S2"])
                break 



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

    response = requests.get('https://1xbit6.com/LiveFeed/Get1x2_VZip?', params=params)
    game_result = response.json()   
    get_SHOTS_ON_TARGET(game_result)



if __name__ == '__main__':
    main()
    
