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
import random

# グローバル変数の宣言
ELEMENT_SYMBOLS = {
    '火':'$',
    '水':'~',
    '風':'@',
    '土':'#',
    '命':'&',
    '無':' '
}
ELEMENT_COLORS = {
    '火':'1',
    '水':'6',
    '風':'2',
    '土':'3',
    '命':'5',
    '無':'7'
}
ELEMENT_NUMBER = {
    0:'$',
    1:'~',
    2:'@',
    3:'#',
    4:'&'
}

# 関数宣言

# メイン関数
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
  
    knock_down = go_dungeon(party,monsters_list)
    if knock_down==5:
        print('*** GAME CLEARED!! ***')
        print(f'倒したモンスター数={knock_down}')
    else:
        print('*** GAME OVER!! ***')
        print(f'倒したモンスター数={knock_down}')

# ダンジョンでの動作
def go_dungeon(party,monsters):
    
    knock_down=0
    print(f"{party['name']}のパーティ（HP={party['最大HP']}）はダンジョンに到達した")

    print()
    show_party(party)
    print()
  
    for i in monsters:
        is_win=do_battle(party,i)
        if is_win==1:
            knock_down += 1
            print(f"{party['name']}はさらに奥へと進んだ")
            print(is_win)
        else:
            print(f"{party['name']}はダンジョンから逃げ出した")
            break

    if knock_down == 5:
        print(f'{party['name']}はダンジョンを制覇した')
    return knock_down

# バトルをする
def do_battle(party,monster):
    print_monster_name(monster)
    print('が現れた！')
    label,element = fill_gems()
    while True:
        on_player_turn(party,monster,label,element)

        if monster['hp'] <= 0:
            print_monster_name(monster)
            print('を倒した！')
            flag = 1
            break

        on_enemy_turn(party,monster)
        
        if party['HP'] <= 0:
            flag = 0
            break

    return flag

# モンスター名を属性付きで表示
def print_monster_name(monster):
    monster_name=monster['name']
    symbol=ELEMENT_SYMBOLS[monster['element']]
    color=ELEMENT_COLORS[monster['element']]

    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0m ',end='')

# 味方パーティの作成
def organize_party(player_name,friends):
    hp=0
    max_hp=0
    max_dp=0
    for i in friends:
        hp += i['hp']
        max_hp += i['max_hp']
        max_dp += i['dp']
    
    ave_dp=int(max_dp/len(friends))

    friends_party={
        'name': player_name,
        'my_party' : friends,
        'HP':hp,
        '最大HP':max_hp,
        '防御':ave_dp
    }
    
    return friends_party

# パーティを表示
def show_party(party):
    print('＜パーティ編成＞')
    for i in party['my_party']:
        print_monster_name(i)
        print(f"{ HP={i['hp']} 攻撃={i['ap']} 防御={i['dp']}")

# プレイヤーのターン
def on_player_turn(my_party,monster,label,element):
    print(f"【{my_party['name']}のターン】（HP={my_party['HP']}）")
    
    show_battle_field(monster,my_party,label,element)
    com = check_valid_command(label)
    move_gem(com,label,element)
    last_num,count = check_banishable(element)
    if count >= 3:
        banish_gems(element,last_num,count)
        shift_gems(element,last_num,count)
        spawn_gems(element,count)
    damege=do_attack(monster)
    print(f"{damege}のダメージを与えた！")

# 敵モンスターのターン
def on_enemy_turn(my_party,monster):
    print(f"【{monster['name']}のターン】（HP={monster['hp']}）")
    damege=do_enemy_attack(my_party)
    print(f"{damege}のダメージを受けた！")

# 敵モンスターへのダメージを管理
def do_attack(monster):
    main_damege=100
    r = random.uniform(-10,10)
    
    damege = int(main_damege*(1+r/100))

    print(monster['hp'])
    monster['hp']=monster['hp']-damege
    print(monster['hp'])
    return damege

# 敵モンスターの攻撃を管理
def do_enemy_attack(my_party):
    damege=200
    print(my_party['HP'])
    my_party['HP']=my_party['HP']-damege
    print(my_party['HP'])
    return damege

# バトルフィールドを生成
def show_battle_field(monster,my_party,label,element):
    print("バトルフィールド")
    print_monster_name(monster)
    print(f"HP= {monster['hp']}/{monster['max_hp']}")
    for i in my_party['my_party']:
        print_monster_name(i)
    print("")
    print(f"HP = {my_party['HP']}/{my_party['最大HP']}")

    print_gems(label,element)
    
# 宝石を生成
def fill_gems():
    gems = []
    for i in range(14):
        gems.append(random.randint(0,4))
    # print(gems)

    element = []
    for num in gems:
        element.append(ELEMENT_NUMBER[num])
    # print(element)
    label=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    # gems_set = dict(zip(label,element))
    # print(gems_set)
    return label,element

# 宝石を表示
def print_gems(label,element):
    print(label)
    print(element)

# 入力されたコマンドを確認
def check_valid_command(label):
    while True:
        com=input("コマンド入力>>")
      
        if len(com) != 2:
            print("2文字でコマンドを入力してください")
            continue
          
        if com[0] not in label or com[1] not in label:
            print("A～Nで入力してください")
            continue
          
        if is_unique(com) == False:
            print("同じ文字は使えません")
            continue
          
        return com

# 動かす宝石のインデックスを確認
def move_gem(com,label,element):
    l_index = label.index(com[0])
    r_index = label.index(com[1])

    swap_gem(element,l_index,r_index)

# 宝石を移動させる
def swap_gem(element,l_index,r_index):
    r = r_index-l_index
    for i in range(abs(r)):
        if r > 0:
            element[l_index+i], element[l_index+1+i] = element[l_index+1+i], element[l_index+i]
            print(element)
        else:
            element[l_index-1-i], element[l_index-i] = element[l_index-i], element[l_index-1-i]
            print(element)

# コマンドに同じ文字がないか確認する
def is_unique(s):
    seen = []
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    return True

# 宝石の並びを調べて消去可能な個所を検索して返す
def check_banishable(element):
    count = 1
    last_num = 0
    for i in range(1,len(element)):
        if element[i] == element[i-1]:
            count += 1
        else:
            if count >= 3:
                print(element[i-1],"match",count)
                last_num = i-1
                print(last_num)
                return last_num,count
            else:
                count = 1

    if count >= 3:
        print(element[-1],"match",count)
        last_num = len(element)-1
        print(last_num)
        return last_num,count
    return last_num,count

# 消去可能な宝石を確認し消去する(実際にリストから消去して宝石を追加する方法のほうが短くなる可能性あり)
def banish_gems(element,last_num,count):
    for i in range(count):
        element[last_num-i] = " "
    print(element)

# 空スロットの右側に並ぶ宝石を左詰めする
def shift_gems(element,last_num,count):
    for x in range(count):
        for i in range(len(element)-last_num-1):
            element[last_num+i], element[last_num+1+i] = element[last_num+1+i], element[last_num+i]
        last_num -= 1

# 空スロットにランダムな宝石を生成する
def spawn_gems(element,count):
    for i in range(count):
        element[-1-i] = ELEMENT_NUMBER[random.randint(0,4)]
    print(element)
  
# main関数の呼び出し
main()





