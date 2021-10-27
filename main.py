from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

put_text("Список всех названий проблем: https://pastebin.com/iy95MB1w (В кавычках)")
# блок ввода
Qplav = 0
lamb = 0
l = 0
Qkond = 0
Qohl = 0
UdlTepl = 0
Qobsh = 0
Qnagr = 0
Qisp = 0
Vob = 0
a = 0
b = 0
c = 0
m = 0
t1 = 0
t2 = 0
V = 0
T = 0
S = 0
Plosh = 0
Per = 0
Plot = 0
probleme = 0
probleme = str(input("введи что надо найди: "))





Qobsh = float(input("Введи кол-во теплоты общее(если известна): "))















Solve = 0


# Блок функций
def Obc(Vob, b, a):

    Solve = Vob / (b * a)
    return Solve


def Obb(Vob, a, c):
    Solve = Vob / (a * c)
    return Solve


def Oba(Vob, b, c):
    Solve = Vob / (b * c)
    return Solve


def Plosha(a, b):
    Solve = a * b
    return Solve


def Plosha1(Plosh, a):
    Solve = Plosh / a
    return Solve


def Plosha2(Plosh, b):
    Solve = Plosh / b
    return Solve


def ObPl(Plosh, c):
    Solve = Plosh * c
    return Solve


def Ob(a, b, c):
    Solve = a * b * c
    return Solve


def Pl(a, b, c, m,):
    Solve = m / (a * b * c)
    return Solve


def PlOb(Plot, m):
    Solve = Plot / m
    return Solve


def PlM(Plot, Vob):
    Solve = Plot / Vob
    return Solve


def scor(S, T):

    Solve = S / T
    return Solve


def time(S, V):

    Solve = S / V
    return Solve


def rast(T, V):

    Solve = T * V
    return Solve


def perr(a, b):
    Solve = (a + b) * 2
    return Solve


def perra(Per, b):
    Solve = Per / (b * 2)
    return Solve


def perrb(Per, a):
    Solve = Per / (a * 2)
    return Solve


def Qobshh(Qnagr, Qisp, Qkond, Qohl, Qplav,):
    Solve = 0
    if Qnagr !=0:
        Solve = Qnagr + Qisp
    if Qkond != 0:
         Solve = Qkond + Qohl
    if Qplav != 0:
        Solve = Qplav + Qnagr
    return Solve


def Qnagrr(UdlTepl, m, t2, t1):
    Solve = UdlTepl * m * (t2 - t1)
    return Solve
def Mqnagrr(Qnagr, UdlTepl,t2,t1):
    Solve = Qnagr/(UdlTepl*(t2-t1))
    return Solve
def Cqnagrr(Qnagr, m, t2, t1):
    Solve = Qnagr/(m*(t2-t1))
    return Solve


def Qispp(l, m):
    Solve = l * m
    return Solve
def lQisp(Qisp, m):
    Solve = Qisp/m
    return Solve
def mQisp(Qisp, l):
    Solve = Qisp/l
    return Solve
def Qkondd(l,m):
    Solve = l * m
    return Solve
def mQkond(Qkond, l):
    Solve = Qkond/l
    return Solve
def lQkond(Qkond, m):
    Solve = Qkond/m
    return Solve
def Qplavv(lamb,m):
    Solve = lamb * m
    return Solve
def mQplavv(Qplav, lamb):
    Solve = Qplav/lamb
    return Solve
def lQplavv(Qplav,m):
    Solve = Qplav/m
    return Solve


# Блок задач
if probleme == "Vob":  # Объём
    a = float(input("Введи длинну(если известна): "))
    b = float(input("Введи ширину(если известна): "))
    c = float(input("Введи высота(если известна): "))
    Obi = Ob(a, b, c)

    put_text(Obi, "M3", "Решение: ", a, "*", b, "*", c, "=", Obi)

if probleme == "Vobplosc":  # объём, зная площадь и высоту
    c = float(input("Введи высота(если известна): "))
    Plosh = float(input("Введи площадь(если известна): "))
    ObPl1 = ObPl(Plosh, c)
    put_text(ObPl, "M3", "Решение: ", Plosh, "*", c, "=", ObPl)
if probleme == "Cvobba":  # высоту зная объём, ширину, длинну
    b = float(input("Введи ширину(если известна): "))
    Vob = float(input("Введи объём(если известна): "))
    a = float(input("Введи длинну(если известна): "))
    Ob2 = Obc(Vob, b, a)
    put_text(Ob2, "M", "Решение: ", Vob, "/", "(", b, "*", a, ")", "=", Ob2)
if probleme == "Bvobac":  # ширину зная объём, длинну, высоту
    Vob = float(input("Введи объём(если известна): "))
    a = float(input("Введи длинну(если известна): "))
    c = float(input("Введи высота(если известна): "))
    Ob2 = Obb(Vob, a, c)
    put_text(Ob2, "M", "Решение: ", Vob, "/", "(", a, "*", c, ")", "=", Ob2)
if probleme == "Avobbc":  # длинну зная объём, ширину, высоту
    b = float(input("Введи ширину(если известна): "))
    Vob = float(input("Введи объём(если известна): "))
    c = float(input("Введи высота(если известна): "))
    Ob2 = Oba(Vob, b, c)
    put_text(Ob2, "M", "Решение: ", Vob, "/", "(", b, "*", c, ")", "=", Ob2)

if probleme == "plos":  # найти площадь
    b = float(input("Введи ширину(если известна): "))
    a = float(input("Введи длинну(если известна): "))
    Ploshs = Plosha(a, b)
    put_text(Ploshs, "M2", "Решение: ", a, "*", b, "=", Ploshs)
if probleme == "Aplosb":  # найти длинну зная площадь и ширину
    b = float(input("Введи ширину(если известна): "))
    Plosh = float(input("Введи площадь(если известна): "))
    Ploshs = Plosha1(Plosh, b)
    put_text(Ploshs, "M", "Решение: ", Plosh, "/", b, "=", Ploshs)
if probleme == "Bplosa":  # найти ширину зная площадь и длинну
    a = float(input("Введи длинну(если известна): "))
    Plosh = float(input("Введи площадь(если известна): "))
    Ploshs = Plosha2(Plosh, a)
    put_text(Ploshs, "M", "Решение: ", Plosh, "/", a, "=", Ploshs)

if probleme == "plot":  # Плотность
    a = float(input("Введи длинну(если известна): "))
    b = float(input("Введи ширину(если известна): "))
    c = float(input("Введи высота(если известна): "))
    m = float(input("Введи массу(если известна): "))
    pli = Pl(a, b, c,m)
    put_text(pli, "Кг/М3", "Решение: ", m, "/", a, "*", b, "*", c, "=", pli)
if probleme == "Vplm":  # найти объём зная плотность массу
    m = float(input("Введи массу(если известна): "))
    Plot = float(input("Введи плотность(если известна): "))
    PlOb1 = PlOb(Plot, m)
    put_text(PlOb1, "M3", "Решение: ", Plot, "/", m, "=", PlOb1)
if probleme == "Mplv":  # найти массу зная плотность объём
    Vob = float(input("Введи объём(если известна): "))
    Plot = float(input("Введи плотность(если известна): "))
    PlM1 = PlM(Plot, Vob)

    put_text(PlM1, "Кг", "Решение: ", Plot, "/", Vob, "=", PlM1)

if probleme == "rast":  # Расстояние
    T = float(input("Введи время(если известна): "))
    V = float(input("Введи скорость(если известна): "))
    rast1 = rast(T, V)

    put_text(rast1, "М/c", "Решение: ", T, "*", V, "=", rast1)
if probleme == "time":  # Время зная расстояние
    S = float(input("Введи расстояние(если известна): "))
    V = float(input("Введи скорость(если известна): "))
    time1 = time(S, V)
    put_text(time1, "Сек", "Решение: ", S, "/", V, "=", time1)
if probleme == "scor":  # Скорость зная расстояние
    S = float(input("Введи расстояние(если известна): "))
    T = float(input("Введи время(если известна): "))
    scor1 = scor(S, T)
    put_text(scor1, "м/c", "Решение: ", S, "/", T, "=", scor1)

if probleme == "perr":  # перриметр
    b = float(input("Введи ширину(если известна): "))
    a = float(input("Введи длинну(если известна): "))
    perr1 = perr(a, b)
    put_text(perr1, "M", "Решение: ", "(", a, "+", b, ")", "*", "2", "=", perr1)
if probleme == "Aperb":  # Длинну зная перриметр и ширину
    a = float(input("Введи длинну(если известна): "))
    Per = float(input("Введи перриметр(если известна): "))
    perr1 = perra(perr, a)
    put_text(perr1, "M", "Решение: ", Per, "/", b, "*", "2" "=", perr1)
if probleme == "Bpera":  # ширину зная перриметр и длинну
    b = float(input("Введи ширину(если известна): "))
    Per = float(input("Введи перриметр(если известна): "))
    perr1 = perrb(perr, b)
    put_text(perr1, "M", "Решение: ", Per, "/", a, "*", "2" "=", perr1)

if probleme == "Qobsh":  # Ку общая
    Qisp = float(input("Введи колл-во теплоты испарения(если известна): "))
    Qnagr = float(input("Введи колл-во теплоты нагрева(если известна): "))
    Qohl = float(input("Введи кол-во теплоты охлаждения(если известна): "))
    Qkond = float(input("Введи кол-во теплоты конденсации(если известна): "))
    Qplav = float(input("Введи колл-во энергии затраченное на плавление(если известна): "))
    Qobshh1 = Qobshh(Qnagr, Qisp, Qkond, Qohl, Qplav)

    put_text(Qobshh1, "Дж", "Решение: ", Qnagr or Qkond , "+", Qisp or Qohl or Qplav, "=", Qobshh1)
if probleme == "Qnagr":  # Q нагревания
    m = float(input("Введи массу(если известна): "))
    UdlTepl = float(input("Введи Удельную теплоёмкость(если известна): "))
    t1 = float(input("Введи температуру 1(если известна): "))
    t2 = float(input("Введи температуру 2(если известна): "))
    Qnagrr1 = Qnagrr(UdlTepl, m, t2, t1)
    put_text(Qnagrr1, "Дж", "Решение:", c, "*", m, "*", "(", t2, "-", t1, ")")
if probleme == "Mqnagr": #найти массу зная ку нагр
    Qnagr = float(input("Введи колл-во теплоты нагрева(если известна): "))
    UdlTepl = float(input("Введи Удельную теплоёмкость(если известна): "))
    t1 = float(input("Введи температуру 1(если известна): "))
    t2 = float(input("Введи температуру 2(если известна): "))
    Mqnagrr1 =Mqnagrr(Qnagr, UdlTepl, t2 ,t1)
    put_text(Mqnagrr1, "кг", "Решение: ", Qnagr, "/", "(", c,"*","(", t2, "-", t1,")", ")", "=", Mqnagrr1)
if probleme == "Cqnagr": # найти ц зная ку нагр
    Qnagr = float(input("Введи колл-во теплоты нагрева(если известна): "))
    m = float(input("Введи массу(если известна): "))
    t1 = float(input("Введи температуру 1(если известна): "))
    t2 = float(input("Введи температуру 2(если известна): "))
    Cqnagrr1 = Cqnagrr(Qnagr,m,t2,t1)
    put_text(Cqnagrr1, "Дж/кг*°С", "Решение: ", Qnagr, "/", "(", m, "*", "(", t2, "-", t1, ")", ")", "=", Cqnagrr1)

if probleme == "Qohl":  # Q охлаждения
    UdlTepl = float(input("Введи Удельную теплоёмкость(если известна): "))
    Qnagr = float(input("Введи колл-во теплоты нагрева(если известна): "))
    m = float(input("Введи массу(если известна): "))
    t1 = float(input("Введи температуру 1(если известна): "))
    t2 = float(input("Введи температуру 2(если известна): "))
    Qohl1 = Qnagrr(UdlTepl,m,t2,t1) or Qnagr
    put_text(Qnagr, "Дж", "Решение: Qохл = Qнагр")
if probleme == "Qisp":  # Q испарения
    l = float(input("Введи удельную теплоту парообразования(если известна): "))
    m = float(input("Введи массу(если известна): "))
    Qispp1 = Qispp(l, m)
    put_text(Qispp1, "Дж", "Решение: ", l, "*", m, "=", Qispp1)
if probleme == "mQisp": # масса из ку испарения
    l = float(input("Введи удельную теплоту парообразования(если известна): "))
    Qisp = float(input("Введи колл-во теплоты испарения(если известна): "))
    mQisp1 = mQisp(Qisp,l)
    put_text(mQisp1, "Кг", "Решение: ", Qisp, "/", l, "=",mQisp1)
if probleme == "lQisp": # L из ку испарения
    Qisp = float(input("Введи колл-во теплоты испарения(если известна): "))
    m = float(input("Введи массу(если известна): "))
    lQisp1 = lQisp(Qisp,m)
    put_text(lQisp1, "Дж/кг", "Решение: ", Qisp, "/", m, "=",lQisp1)

if probleme == "Qkond": #Q Конденсации
    m = float(input("Введи массу(если известна): "))
    Qkondd1 = Qkondd(l,m)
    l = float(input("Введи удельную теплоту парообразования(если известна): "))
    put_text("-",Qkondd1, "Дж", "Решение: ", "-",l, "*", m )
if probleme == "lQkond": # L из ку конденсации
    Qkond = float(input("Введи кол-во теплоты конденсации(если известна): "))
    m = float(input("Введи массу(если известна): "))
    lQkond1 = lQkond(Qkond,m)
    put_text("-", lQkond1, "Дж/кг", "Решение: ", Qkond, "/", m, "=","-",lQkond1)
if probleme == "mQkond":  # масса из ку конденсации
    l = float(input("Введи удельную теплоту парообразования(если известна): "))
    Qkond = float(input("Введи кол-во теплоты конденсации(если известна): "))
    mQkond1 = mQkond(Qkond, l)
    put_text(mQkond1, "Дж/кг", "Решение: ", Qkond, "/", l, "=", mQkond1)
if probleme == "Qplav": #Q плавления
    lamb = float(input("Введи лямбду(если известна): "))
    m = float(input("Введи массу(если известна): "))
    Qplavv1 = Qplavv(lamb,m)
    put_text(Qplavv1, "Дж", "Решение: ", lamb, "*", m, "=", Qplavv1)
if probleme == "mQplav": # масса из Q плавления
    Qplav = float(input("Введи колл-во энергии затраченное на плавление(если известна): "))
    lamb = float(input("Введи лямбду(если известна): "))
    mQplavv1 = mQplavv(Qplav,lamb)
    put_text(mQplavv1, "кг", "Решение: ", Qplav, "/", lamb, "=", mQplavv1)
if probleme == "lQplav": # l из Q плавления
    Qplav = float(input("Введи колл-во энергии затраченное на плавление(если известна): "))
    m = float(input("Введи массу(если известна): "))
    lQplavv1 = lQplavv(Qplav,m)
    put_text(lQplavv1, "кг", "Решение: ", Qplav, "/", m, "=", lQplavv1)
if probleme == "Обэме":
    put_text("https://www.youtube.com/watch?v=19R6CyjHqzE&ab_channel=BRED")
