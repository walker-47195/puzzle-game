""" ゲームの流れ
1.ゲームタイトルは「Puzzle&Monsters」（略して「Puzmon」）とする。
2.プレイヤーは、ゲームスタート時点で4匹のモンスター（青龍、朱雀、白虎、玄武）を従えている。
3.プレイヤーは、ゲームスタート直後に４匹の味方モンスターとパーティを編成してダンジョンに行く。
4.ダンジョンでは5回のバトルが発生し、すべてのバトルで敵モンスターのHPを0にすればゲームクリア。
  途中でパーティのHPが5になるとゲームオーバー。
5.各バトルは、パーティ対敵モンスター1匹の構図で戦う。敵モンスターのHPを0にすると次のバトルに進む。
6.バトルで戦う相手は、登場順に「スライム」「ゴブリン」「オオコウモリ」「ウェアウルフ」「ドラゴン」とする。
7.ゲーム終了時には、「GAME OVER!!」または「GAME CLERED!!」のメッセージとともに、倒した敵モンスターの数を表示する。 """

""" パラメータの概要
1.敵モンスターのパラメータは、名前、HP、最大HP、属性、攻撃力、防御力とする。
2.味方モンスターのパラメータは、敵モンスターのパラメータと同じとする。
3.パーティのパラメータは、プレイヤー名、4匹の味方モンスター、パーティのHP及び最大HP、防御力とする。
4.パーティ編成時、パーティに参加している味方モンスターのHPの合計値がパーティのHP及び最大HPとなる。
  また、味方モンスターの防御力の平均値がパーティの防御力となる。
5.ダンジョン内のバトルでは、パーティのHPが増減し、味方モンスターごとのHPは増減しない。 """

# 作成開始日：2026/02/17　作成者：平島　隼平

# インポート

# グローバル変数の宣言
ELEMENT_SYMBOLS = {
    '火':'$',
    '水':'~',
    '風':'@',
    '土':'#',
    '命':'&',
    '無':''
}
ELEMENT_COLORS = {
    '火':'1',
    '水':'6',
    '風':'2',
    '土':'3',
    '命':'5',
    '無':'7'
}

# 関数宣言
def main():
    player=input('プレイヤー名を入力してください>>')
    print('*** Puzzle & Monsters ***')

  # 敵モンスターの生成
    slime = {
        'name':'スライム',
        'hp':100,
        'max_hp':100,
        'element':'水',
        'ap':10,
        'dp':1
    }
    goblin = {
        'name':'ゴブリン',
        'hp':200,
        'max_hp':200,
        'element':'土',
        'ap':20,
        'dp':5
    }
    bigbat = {
        'name':'オオコウモリ',
        'hp':300,
        'max_hp':300,
        'element':'風',
        'ap':30,
        'dp':10
    }
    werewolf = {
        'name':'ウェアウルフ',
        'hp':400,
        'max_hp':400,
        'element':'風',
        'ap':40,
        'dp':15
    }
    doragon = {
        'name':'ドラゴン',
        'hp':600,
        'max_hp':600,
        'element':'火',
        'ap':50,
        'dp':20
    }
    monsters_list=[slime,goblin,bigbat,werewolf,doragon]

# 味方モンスターの生成
    seiryu = {
        'name':'青龍',
        'hp':150,
        'max_hp':150,
        'element':'風',
        'ap':15,
        'dp':10
    }
    suzaku = {
        'name':'朱雀',
        'hp':150,
        'max_hp':150,
        'element':'火',
        'ap':25,
        'dp':10
    }
    byakko = {
        'name':'白虎',
        'hp':150,
        'max_hp':150,
        'element':'土',
        'ap':20,
        'dp':5
    }
    genbu = {
        'name':'玄武',
        'hp':150,
        'max_hp':150,
        'element':'水',
        'ap':20,
        'dp':15
    }
    friends=[seiryu,suzaku,byakko,genbu]
    party=organize_party(player,friends)
    print(party)
  
    knock_down = go_dungeon(player,monsters_list)
    if knock_down==5:
        print('*** GAME CLERED!! ***')
        print(f'倒したモンスター数={knock_down}')
    else:
        print('*** GAME OVER!! ***')
        print(f'倒したモンスター数={knock_down}')

def go_dungeon(player,monsters):
    # monsters=['スライム','ゴブリン','オオコウモリ','ウェアウルフ','ドラゴン']
    knock_down=0
    print(f'{player}はダンジョンに到達した')
    for i in monsters:
        is_win=do_battle(i)
        if is_win==1:
            knock_down += 1
        print(is_win)
    print(f'{player}はダンジョンを制覇した')
    return knock_down

def do_battle(monster):
    print_monster_name(monster)
    print('が現れた！')

    print_monster_name(monster)
    print('を倒した！')
  
    flag=1
    return flag

def print_monster_name(monster):
    monster_name=monster['name']
    symbol=ELEMENT_SYMBOLS[monster['element']]
    color=ELEMENT_COLORS[monster['element']]

    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0m ',end='')

def organize_party(player_name,friends):
    max_hp=0
    max_dp=0
    for i in friends:
        max_hp += i['max_hp']
        max_dp += i['dp']
    
    ave_dp=max_dp/len(friends)

    friends_party={
        'name': player_name,
        'party' : friends,
        'HP':max_hp,
        '最大HP':max_hp,
        '防御':ave_dp
    }
    
    return friends_party

# main関数の呼び出し

main()


