""" ゲームの流れ
1.ゲームタイトルは「Puzzle&Monsters」（略して「Puzmon」）とする。
2.プレイヤーは、ゲームスタート時点で4匹のモンスター（青龍、朱雀、白虎、玄武）を従えている。
3.プレイヤーは、ゲームスタート直後に４匹の味方モンスターとパーティを編成してダンジョンに行く。
4.ダンジョンでは5回のバトルが発生し、すべてのバトルで敵モンスターのHPを0にすればゲームクリア。
  途中でパーティのHPが5になるとゲームオーバー。
5.各バトルは、パーティ対敵モンスター1匹の構図で戦う。敵モンスターのHPを0にすると次のバトルに進む。
6.バトルで戦う相手は、登場順に「スライム」「ゴブリン」「オオコウモリ」「ウェアウルフ」「ドラゴン」とする。
7.ゲーム終了時には、「GAME OVER!!」または「GAME CLEARED!!」のメッセージとともに、倒した敵モンスターの数を表示する。 """

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
ELEMENT_BOOST = {
    '水火':2.0,
    '火風':2.0,
    '風土':2.0,
    '土水':2.0,

    '火水':0.5,
    '風火':0.5,
    '土風':0.5,
    '水土':0.5,

    '水水':1.0,
    '火火':1.0,
    '風風':1.0,
    '土土':1.0,
    '水風':1.0,
    '火土':1.0,
    '風水':1.0,
    '土火':1.0
}

# 関数宣言

# メイン関数
def main():
    player = input('プレイヤー名を入力してください>>')
    print("")
    print('*** Puzzle & Monsters ***')
    print("")

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
    suzaku = {
        'name':'朱雀',
        'hp':150,
        'max_hp':150,
        'element':'火',
        'ap':50,
        'dp':10
    }
    genbu = {
        'name':'玄武',
        'hp':150,
        'max_hp':150,
        'element':'水',
        'ap':40,
        'dp':15
    }
    seiryu = {
        'name':'青龍',
        'hp':150,
        'max_hp':150,
        'element':'風',
        'ap':30,
        'dp':10
    }
    byakko = {
        'name':'白虎',
        'hp':150,
        'max_hp':150,
        'element':'土',
        'ap':40,
        'dp':5
    }
    
    friends = [suzaku,genbu,seiryu,byakko]

    party = organize_party(player,friends)

    knock_down = go_dungeon(party,monsters_list)
    if knock_down == 5:
        print('*** GAME CLEARED!! ***')
        print(f'倒したモンスター数={knock_down}')
    else:
        print('*** GAME OVER!! ***')
        print(f'倒したモンスター数={knock_down}')

# 味方パーティの作成
def organize_party(player_name,friends):
    hp = 0
    max_hp = 0
    max_dp = 0
    for i in friends:
        hp += i['hp']
        max_hp += i['max_hp']
        max_dp += i['dp']
    
    ave_dp = int(max_dp/len(friends))

    party = {
        'name':player_name,
        'my_monsters':friends,
        'HP':hp,
        'MAX_HP':max_hp,
        'DP':ave_dp
    }
    
    return party

# ダンジョンでの動作
def go_dungeon(party,monsters):

    knock_down=0
    print(f"{party['name']}のパーティ（HP={party['MAX_HP']}）はダンジョンに到達した")
    
    print()
    show_party(party)
    print()

    for i in monsters:
        is_win = do_battle(party,i)
        if is_win == 1:
            knock_down += 1
            print(f"{party['name']}はさらに奥へと進んだ")
        else:
            print(f"{party['name']}はダンジョンから逃げ出した")
            break
            
    if knock_down == 5:
        print(f"{party['name']}はダンジョンを制覇した")
    return knock_down

# パーティを表示
def show_party(party):
    print('＜パーティ編成＞')
    for i in party['my_monsters']:
        print_monster_name(i)
        print(f" HP={i['hp']} 攻撃={i['ap']} DP={i['dp']}")

# バトルをする
def do_battle(party,monster):
    print_monster_name(monster)
    print("が現れた！")
    print("")
    label,element = fill_gems()
    while True:
        on_player_turn(party,monster,label,element)

        if monster['hp'] <= 0:
            print_monster_name(monster)
            print("を倒した！")
            flag = 1
            break

        on_enemy_turn(party,monster)
        
        if party['HP'] <= 0:
            flag = 0
            break

    return flag

# モンスター名を属性付きで表示
def print_monster_name(monster):
    monster_name = monster['name']
    symbol = ELEMENT_SYMBOLS[monster['element']]
    color = ELEMENT_COLORS[monster['element']]

    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0m ',end='')

# 宝石を生成
def fill_gems():
    gems = []
    for i in range(14):
        gems.append(random.randint(0,4))

    element = []
    for num in gems:
        element.append(ELEMENT_NUMBER[num])

    label=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

    return label,element

# プレイヤーのターン
def on_player_turn(party,monster,label,element):
    print(f"【{party['name']}のターン】（HP={party['HP']}）")
    
    show_battle_field(party,monster,label,element)
    
    all_attack(party,monster,label,element)

# バトルフィールドを生成
def show_battle_field(party,monster,label,element):
    print("バトルフィールド")
    print_monster_name(monster)
    print(f"HP= {monster['hp']}/{monster['max_hp']}")
    for i in party['my_monsters']:
        print_monster_name(i)
    print("")
    print(f"HP = {party['HP']}/{party['MAX_HP']}")

    print(label)
    print(element)

# 1回の攻撃をまとめて処理する
def all_attack(party,monster,label,element):
    combo = 1
    count = 0
    command = check_valid_command(label)
    move_gem(command,label,element)
    while True:
        last_num,count = check_banishable(element)
        combo_mag = combo_magnification(count,combo)
        if count >= 3:
            attack_element = element[last_num]
            banish_gems(element,last_num,count)
            shift_gems(element,last_num,count)
            spawn_gems(element,count)
            if combo >= 2:
                print(f"{combo}COMBO!")
            if attack_element == '&':
                recover = do_recover(party,combo_mag)
                print(f"{party['name']}は{recover}回復した！")
            else:
                attack_mons,element_name = attack_monster(attack_element)
                element_mag = ELEMENT_BOOST[element_name + monster['element']]
                damage = do_attack(party,monster,attack_mons,element_mag,combo_mag)
                print(f"{party['my_monsters'][attack_mons]['name']}の攻撃！")
                if element_mag == 2.0:
                    print("効果は抜群だ！")
                elif element_mag == 0.5:
                    print("効果はいまひとつのようだ...")
                print(f"{damage}のダメージを与えた！")
            combo += 1
        else:
            break

# 入力されたコマンドを確認
def check_valid_command(label):
    while True:
        com = input("コマンド入力>>")

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

# コマンドに同じ文字がないか確認する
def is_unique(command):
    check_box = []
    for char in command:
        if char in check_box:
            return False
        check_box.append(char)
    return True

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

# 宝石の並びを調べて消去可能な個所を検索して返す
def check_banishable(element):
    count = 1
    last_num = 0
    for i in range(1,len(element)):
        if element[i] == element[i-1]:
            count += 1
        else:
            if count >= 3:
                last_num = i-1
                return last_num,count
            else:
                count = 1

    if count >= 3:
        last_num = len(element)-1
        return last_num,count
    return None,0

# コンボ補正
def combo_magnification(count,combo):
    return 1.5**(count -3 + combo)

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

# '命'の属性で回復する
def do_recover(party,combo_mag):
    recover = int(20 * combo_mag * blur_damage())
    party['HP'] += recover
    if party['HP'] > party['MAX_HP']:
        party['HP'] = party['MAX_HP']
    return recover

# 攻撃モンスターを判定する変数を取り出す
def attack_monster(attack_element):
    attack_mons = None
    element_name = None
    match attack_element:
        case '$':
            attack_mons = 0
            element_name = '火'
        case '~':
            attack_mons = 1
            element_name = '水'
        case '@':
            attack_mons = 2
            element_name = '風'
        case '#':
            attack_mons = 3
            element_name = '土'
    return attack_mons,element_name

# ダメージに乱数を入れる
def blur_damage():
    r = random.uniform(-10,10)
    blur = (1+r/100)
    return blur

# 敵モンスターへのダメージを管理
def do_attack(party,monster,attack_mons,element_mag,combo_mag):
    
    main_damage = party['my_monsters'][attack_mons]['ap'] - monster['dp']
    element_damage = main_damage * element_mag
    conbo_damage = element_damage * combo_mag
    blur = blur_damage()
    
    damage = int(conbo_damage*blur)
    if damage < 0:
        damage = 1

    monster['hp']=monster['hp']-damage

    return damage

# 敵モンスターのターン
def on_enemy_turn(party,monster):
    print(f"【{monster['name']}のターン】（HP={monster['hp']}）")
    damage = do_enemy_attack(party,monster)
    print(f"{damage}のダメージを受けた！")

# 敵モンスターの攻撃を管理
def do_enemy_attack(party,monster):
    blur = blur_damage()
    damage = int((monster['ap'] - party['DP'])*blur)
    if damage <= 0:
        damage = 1

    party['HP']=party['HP']-damage

    return damage

# main関数の呼び出し
main()
