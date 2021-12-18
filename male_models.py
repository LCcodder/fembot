# -*- coding: utf8 -*-
import random

male_calls = [ "биомусор" , "ишак", "остолбень", "отморозок" ,"изверг", "ирод", "извращенец", "щенок", "долбоящер", "долботряс", "дегенерат", "выблядок","женоненавистник", 'унтерменьш',  "угнетатель", "генератор спермы", "недоразум", "завод по производству спермы",  "блядословник-унтерменьш", "спермобак", "гиббон", "спермоносец", "морж"]
male_angers = ["недоразвитый", "недоебанный",  "безмозглый", "аморальный", "безбожный", "одноклеточный", "цисгендерный",  "хуестопный","жалкий","абьюзивный", "блядский", "опущенный",'ходячий', "мерзкий", "гендерный", "генетический", "озабоченный", "очередной", "патриархальный", "низкотестостероновый", "ущемленный", "хуеблядский", "вонючий", "несчастный", "аггресивный", "тупой", "безалаберный"]
male_tippings = ['гореть тебе в аду', "вам место в лесу, жалкие существа", "надеюсь, ваш род умрет", "вас даже людьми назвать нельзя", "надеюсь ты будешь изнасилован, жалкое отродье человеческого вида" ,'выпили себя ножом, псина', "господи убей себя" , "ненавижу тебя мразь" ,"назвать тебя животным — значить льстить тебе", "сделай себе харакири", "отрежь свой спермовыбрасыватель, уродина", "сдохни от рака простаты, тупое говно", "да чтоб тебя обоссали"]

male_sentences = [ "К таким вещам как феминизм несерьёзно относиться нельзя.","Я думаю, вам даже бессмысленно говорить что ваша мать-женщина.","Правильно, правильно, не уважай дальше женщин...", "Вот бы тебя мать увидела","Боже блять...",'Какого хуя я тут за вас одна отдуваюсь?','Только и думаешь, чтобы изнасиловать независимую девушку!!!!', "Ты далёк от нормального члена общества так же, как неандерталец от кроманьонца" ,"Небось гордишься тем, что ты мужчина и тем, что природа тебе дала возможность ссать стоя" ,'Ты априори свинья, поработитель и угнетатель!', "Пол - это всего лишь социальный конструкт!"]

male_crops = ['Сделаем человечество вновь эстетичным! Давайте же сотрём дешёвок в порошок.' ,'Хуеблядский Спермоносец имени Первого Подзалупного Пиздострадального фронта.' ,'Хотя той же справедливости ради стоит заметить, что у мужика выше вероятность забухать. Особенно у такого как ты.' ,'ты — всего лишь машина, ходячий спермобак с вибратором.' ,'Я хочу видеть тебя избитым в кровавое месиво, с каблуком, забитым тебе в рот, подобно яблоку в пасти у свиньи, мерзкое хуястое существо.' ,'Типа ты дофига весь такой рациональный, ведь у тебя нет месячных. Оставь свои кухонные рассуждения о патриархате кому нибудь другому, ок.' ,'Чего тебе надо, пораждение патриархата? мммм? Того же чего и всем остальным хуястым, скорее всего. Ты этого не получишь.' ,'Знаешь, конечно не хорошо так говорить, но когда патриархат умрёт, это одна из рож, которая будет висеть на его надробии','Для тебя это легко, потому что этот мир был построен агрессивными тестостероновыми хуемразями, для таких же агрессивных тестостероновых хуемразей.', 'Когда вы уже блять все переведётесь?', 'Бесполезный блядословник-унтерменш, у которого на ебарезине написано, что он генетический придурок, который, сука, тупее чем чехол от телефона, и у которого есть лишь один лучший друг лучший друг - темнота, потому что она скрывает его кривое ебало.']

male_links = ['https://yakutia-daily.ru/40062-2/', 'https://vecherka.tj/archives/33648', 'https://myslo.ru/city/people/interview/chetyre-strashnye-istorii-o-domashnem-nasilii', 'https://news.ykt.ru/article/102270' ,'https://73online.ru/r/zhenshiny_kotorye_smogli_istorii_o_domashnem_nasilii_i_bullinge_-75931' ,'https://74.ru/text/relations/2019/09/16/66229729/', 'https://www.the-village.ru/city/ustory/254783-nasilei-v-semie']

male_lost = ['Научись для начала проигрывать', "Ты проиграл и это не обсуждается", "Пошел в пизду, ты проиграл", "Лузер, проигрывать это твое", "Ты не одолел меня"]

male_photo_desc = ['Я не вижу этой фотографии людей', "Скинь лучше фото с людьми", "Где здесь люди на фото", "Что за биомусор..."]

male_nahui = ['Заткнись', "Сам иди туда", "Ебальничек прикрой", "Завали свой спермоприемник", "Еблет на ноль", "Ты себя имел в виду", "Ага, ага, продолжай", "Прям сразу", "Раскомандовался"]

male_headliners = ['!', '.']

ending_male = ['б', "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ш", "щ", "ы", ]
ending_middle = ['о', "е"]
ending_female = ["а", "я"]


male_output_array = [0, 1, 2, 3, 4 ]




class maleGen():
    def __init__(male):
        male.calllist = male_calls
        male.anglist = male_angers
        male.tiplist = male_tippings

    def maleRandList(ran_list):
        rand = random.randint(0, len(ran_list) - 1)
        return ran_list[rand]
    def maleWordGen():

        first_call = maleGen.maleRandList(male_angers)
        second_call = maleGen.maleRandList(male_calls)
        third_call = maleGen.maleRandList(male_tippings)
        fourth_call = maleGen.maleRandList(male_sentences)
        fifth_call = maleGen.maleRandList(male_crops)

        space = ' '
        coma = ','
        headl = maleGen.maleRandList(male_headliners)

        type_1 = first_call.title() + space + second_call + coma + space + third_call + headl + space + fourth_call
        type_2 = first_call.title() + space + second_call + coma + space + third_call + headl
        type_3 = fourth_call + space + first_call.title() + space + second_call
        type_4 = fifth_call
        type_5 = first_call.title() + space + second_call + coma + space + third_call + headl + space + fourth_call

        output_random = maleGen.maleRandList(male_output_array)

        if output_random == 0:
            output_male = type_1
        if output_random == 1:
            output_male = type_2
        if output_random == 2:
            output_male = type_3
        if output_random == 3:
            output_male = type_4
        if output_random == 4:
            output_male = type_5

        return output_male
    def maleOutsGen(inp):
        if inp == 0:
            output_male = 'читай, '+ maleGen.maleRandList(male_calls) + ':\n'+ maleGen.maleRandList(male_links)
        if inp == 1:
            space = ' '
            coma = ','
            first_call = maleGen.maleRandList(male_angers)
            second_call = maleGen.maleRandList(male_calls)

            output_male = maleGen.maleRandList(male_lost) + coma + space + first_call + space + second_call
        if inp == 2:
            output_male = maleGen.maleRandList(male_photo_desc) + ', ' + maleGen.maleRandList(male_angers) + ' ' + maleGen.maleRandList(male_calls)
        if inp == 3:
            output_male = maleGen.maleRandList(male_nahui) + ', ' + maleGen.maleRandList(male_angers) + ' ' + maleGen.maleRandList(male_calls)
        return output_male

