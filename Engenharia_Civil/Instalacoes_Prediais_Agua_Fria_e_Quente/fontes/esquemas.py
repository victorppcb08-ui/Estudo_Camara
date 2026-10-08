"""Esquemas didáticos originais para o resumo da NBR 5626:2020."""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch

OUT = sys.argv[1]
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 9

AZ = "#1F6FB2"      # água fria
AZ_CL = "#D6E8F7"
VM = "#C8432B"      # água quente
CZ = "#5B6570"      # estrutura
CZ_CL = "#E9ECEF"
TX = "#1F2933"
VD = "#2E7D5B"
AM = "#B7791F"


def base(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def salvar(fig, nome):
    arq = f"{OUT}/{nome}.png"
    fig.savefig(arq, dpi=200, bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)
    from PIL import Image, ImageChops
    im = Image.open(arq).convert("RGB")
    caixa_ = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
    if caixa_:
        m = 14
        im.crop((max(caixa_[0] - m, 0), max(caixa_[1] - m, 0), min(caixa_[2] + m, im.width), min(caixa_[3] + m, im.height))).save(arq)


def rotulo(ax, xy, xytext, texto, cor=TX, ha="left", va="center", fs=8.5, weight="normal"):
    ax.annotate(texto, xy=xy, xytext=xytext, ha=ha, va=va, fontsize=fs, color=cor, fontweight=weight,
                arrowprops=dict(arrowstyle="-", color=CZ, lw=0.7, shrinkA=2, shrinkB=2))


def cota(ax, p1, p2, texto, lado=(0, 0), cor=TX, fs=9, ha="center", va="center"):
    ax.annotate("", xy=p1, xytext=p2, arrowprops=dict(arrowstyle="<->", color=cor, lw=1.0, shrinkA=0, shrinkB=0))
    mx, my = (p1[0] + p2[0]) / 2 + lado[0], (p1[1] + p2[1]) / 2 + lado[1]
    ax.text(mx, my, texto, ha=ha, va=va, fontsize=fs, color=cor, fontweight="bold")


# ---------------------------------------------------------------- E1: visão geral
def e1():
    fig, ax = base(7.4, 5.3, (0, 148), (0, 106))
    # terreno
    ax.plot([0, 148], [30, 30], color=CZ, lw=1.2)
    ax.add_patch(Rectangle((0, 0), 148, 30, color="#F3EFE6", zorder=0))
    ax.text(3, 32, "nível da rua", fontsize=7.5, color=CZ)
    # edifício
    ax.add_patch(Rectangle((62, 30), 62, 54, fill=False, ec=CZ, lw=1.4))
    for y in (48, 66):
        ax.plot([62, 124], [y, y], color=CZ, lw=0.8)
    ax.add_patch(Rectangle((62, 8), 62, 22, fill=False, ec=CZ, lw=1.0, ls="--"))
    ax.text(121, 11, "subsolo", fontsize=7.5, color=CZ, ha="right")
    # rede pública
    ax.add_patch(Circle((10, 18), 3.2, fc=AZ_CL, ec=AZ, lw=1.4))
    ax.text(10, 10.5, "rede pública", ha="center", fontsize=8.5, color=TX)
    # ramal predial até hidrômetro
    ax.plot([13.2, 30], [18, 18], color=AZ, lw=2.2)
    ax.add_patch(FancyBboxPatch((30, 15), 9, 6, boxstyle="round,pad=0.2", fc="white", ec=AZ, lw=1.3))
    ax.text(34.5, 18, "HD", ha="center", va="center", fontsize=8, color=AZ, fontweight="bold")
    # alimentador predial
    ax.plot([39, 70], [18, 18], color=AZ, lw=2.2)
    ax.plot([70, 70], [18, 24.5], color=AZ, lw=2.2)
    # reservatório inferior
    ax.add_patch(Rectangle((66, 10), 22, 15, fc=AZ_CL, ec=AZ, lw=1.4))
    ax.add_patch(Rectangle((66, 10), 22, 11, fc="#A9CDEC", ec="none"))
    ax.add_patch(Rectangle((66, 10), 22, 15, fill=False, ec=AZ, lw=1.4))
    ax.text(77, 15, "reservatório\ninferior", ha="center", va="center", fontsize=7.8, color=TX)
    # bombas
    ax.plot([88, 96], [13, 13], color=AZ, lw=2.0)
    for by in (13, 20):
        ax.add_patch(Circle((99, by), 3, fc="white", ec=AZ, lw=1.4))
        ax.text(99, by, "B", ha="center", va="center", fontsize=7.5, color=AZ, fontweight="bold")
    ax.plot([94, 94], [13, 20], color=AZ, lw=2.0)
    ax.plot([94, 96], [20, 20], color=AZ, lw=2.0)
    ax.plot([102, 108], [13, 13], color=AZ, lw=2.0)
    ax.plot([102, 108], [20, 20], color=AZ, lw=2.0)
    ax.plot([108, 108], [13, 20], color=AZ, lw=2.0)
    # recalque
    ax.plot([108, 116], [16.5, 16.5], color=AZ, lw=2.2)
    ax.plot([116, 116], [16.5, 98], color=AZ, lw=2.2)
    ax.plot([116, 104], [98, 98], color=AZ, lw=2.2)
    ax.plot([104, 104], [98, 95.5], color=AZ, lw=2.2)
    # reservatório superior
    ax.add_patch(Rectangle((80, 86), 28, 14, fc=AZ_CL, ec=AZ, lw=1.4))
    ax.add_patch(Rectangle((80, 86), 28, 9.5, fc="#A9CDEC", ec="none"))
    ax.add_patch(Rectangle((80, 86), 28, 14, fill=False, ec=AZ, lw=1.4))
    ax.plot([94, 94], [86, 100], color=AZ, lw=1.0)
    ax.text(87, 90.5, "reserv.", ha="center", va="center", fontsize=7.5, color=TX)
    ax.text(101, 90.5, "superior", ha="center", va="center", fontsize=7.5, color=TX)
    # barrilete
    ax.plot([87, 87], [86, 80], color=AZ, lw=2.0)
    ax.plot([101, 101], [86, 80], color=AZ, lw=2.0)
    ax.plot([70, 101], [80, 80], color=AZ, lw=2.6)
    # colunas
    for cx in (70, 90):
        ax.plot([cx, cx], [80, 36], color=AZ, lw=2.2)
    # ramais e sub-ramais
    for y in (74, 56, 38):
        for x0, sxs in ((70, (75, 80)), (90, (95, 100))):
            ax.plot([x0, sxs[-1]], [y, y], color=AZ, lw=1.6)
            for sx in sxs:
                ax.plot([sx, sx], [y, y - 3.5], color=AZ, lw=1.1)
                ax.add_patch(Circle((sx, y - 4.2), 0.8, fc=AZ, ec=AZ))
    # rótulos
    rotulo(ax, (21, 18), (14, 26), "ramal predial", ha="center", va="bottom")
    rotulo(ax, (34.5, 21), (36, 26), "hidrômetro", ha="left", va="bottom")
    rotulo(ax, (50, 18), (46, 10), "alimentador predial", ha="center", va="top")
    rotulo(ax, (102, 22), (128, 24), "sistema de\nrecalque (mín.\n2 bombas)", ha="left", va="center", fs=7.8)
    rotulo(ax, (116, 60), (128, 60), "tubulação\nde recalque", ha="left")
    rotulo(ax, (76, 80), (56, 90), "barrilete", ha="right")
    rotulo(ax, (70, 66), (56, 70), "coluna de\ndistribuição", ha="right")
    rotulo(ax, (73, 56), (56, 52), "ramal", ha="right")
    rotulo(ax, (80, 35.5), (56, 38), "sub-ramal e ponto\nde utilização", ha="right")
    ax.text(74, 103.5, "Abastecimento indireto: a água chega aos pontos a partir de reservatório do edifício",
            ha="center", fontsize=8.5, color=TX, style="italic")
    salvar(fig, "e1_sistema")


# ---------------------------------------------------------------- E2: reservatório
def e2():
    fig, ax = base(7.4, 4.3, (0, 148), (0, 86))
    # corpo do reservatório
    ax.add_patch(Rectangle((40, 18), 70, 50, fc="white", ec=CZ, lw=2.2))
    ax.add_patch(Rectangle((41.1, 19.1), 67.8, 34, fc="#A9CDEC", ec="none"))
    ax.plot([41, 109], [53, 53], color=AZ, lw=1.0)
    ax.text(100, 54.5, "nível máximo\nde operação", fontsize=7.5, color=AZ, ha="center", va="bottom")
    # tampa
    ax.add_patch(Rectangle((66, 68), 20, 3, fc=CZ, ec=CZ))
    rotulo(ax, (76, 71), (76, 80), "tampa ou porta de acesso opaca,\nfirmemente presa", ha="center", va="bottom")
    # entrada com registro e boia
    ax.plot([12, 40], [62, 62], color=AZ, lw=2.6)
    ax.plot([40, 48], [62, 62], color=AZ, lw=2.6)
    reg(ax, 24, 62)
    ax.plot([48, 60], [62, 55], color=CZ, lw=1.2)
    ax.add_patch(Circle((61.5, 54), 2.6, fc="white", ec=CZ, lw=1.2))
    rotulo(ax, (24, 64), (22, 76), "registro de fechamento\na montante e próximo", ha="center", va="bottom")
    ax.text(3, 59, "entrada\n(alimentador\nou recalque)", fontsize=7.8, color=TX, va="top")
    rotulo(ax, (55, 58), (46, 44), "controle automático\nde nível, com proteção\ncontra refluxo", ha="left", va="top", fs=7.8)
    # extravasor
    ax.plot([110, 128], [57.5, 57.5], color=AM, lw=2.6)
    ax.plot([128, 128], [57.5, 42], color=AM, lw=2.6)
    ax.add_patch(Rectangle((126, 38.5), 4, 3.5, fc="white", ec=AM, lw=1.0, hatch="xxxx"))
    rotulo(ax, (120, 58.8), (120, 70), "extravasor: acima do\nnível máximo de operação", ha="center", va="bottom")
    rotulo(ax, (130, 40.2), (134, 40.2), "tela na\nextremidade", ha="left", va="center", fs=7.8)
    # aviso derivado do extravasor
    ax.plot([118, 118], [57.5, 49], color=AM, lw=1.4)
    ax.plot([118, 122], [49, 49], color=AM, lw=1.4)
    rotulo(ax, (122, 49), (133, 50), "aviso de\nextravasão", ha="left", va="center", fs=7.8)
    # saída
    ax.plot([109, 138], [24, 24], color=AZ, lw=2.6)
    reg(ax, 122, 24)
    ax.text(130, 19.5, "saída para o barrilete", fontsize=7.8, color=TX, va="top", ha="center")
    # limpeza
    ax.plot([75, 75], [18, 8], color=CZ, lw=2.6)
    reg(ax, 75, 12, vertical=True)
    rotulo(ax, (77, 11), (86, 8), "limpeza, com registro de fácil acesso", ha="left", va="center")
    ax.text(42, 21.5, "fundo com leve declividade para a limpeza", fontsize=7.3, color=TX, style="italic")
    salvar(fig, "e2_reservatorio")


def reg(ax, x, y, vertical=False, cor=TX):
    """Símbolo de registro (gravata-borboleta)."""
    s = 2.4
    if vertical:
        pts1 = [(x - s, y + s), (x + s, y + s), (x, y)]
        pts2 = [(x - s, y - s), (x + s, y - s), (x, y)]
    else:
        pts1 = [(x - s, y + s), (x - s, y - s), (x, y)]
        pts2 = [(x + s, y + s), (x + s, y - s), (x, y)]
    for p in (pts1, pts2):
        ax.add_patch(Polygon(p, closed=True, fc="white", ec=cor, lw=1.2, zorder=5))


# ---------------------------------------------------------------- E3: separação atmosférica
def e3():
    fig, ax = base(6.6, 4.0, (0, 132), (0, 80))
    # parede e laje
    ax.add_patch(Rectangle((30, 8), 8, 62, fc=CZ_CL, ec=CZ, lw=1.2, hatch="..."))
    ax.add_patch(Rectangle((30, 62), 96, 8, fc=CZ_CL, ec=CZ, lw=1.2, hatch="..."))
    # água
    ax.add_patch(Rectangle((38, 8), 88, 24, fc="#A9CDEC", ec="none"))
    ax.plot([38, 126], [32, 32], color=AZ, lw=1.4)
    ax.text(124, 28, "nível de transbordamento", fontsize=8, color=AZ, ha="right", va="top")
    ax.text(124, 22.5, "(água no nível do extravasor)", fontsize=7.3, color=AZ, ha="right", va="top")
    # extravasor
    ax.plot([8, 38], [30, 30], color=AM, lw=4.5, solid_capstyle="butt")
    ax.text(10, 24.5, "extravasor", fontsize=8.5, color=AM)
    # tubo de alimentação entrando e curva para baixo
    ax.plot([8, 70], [52, 52], color=AZ, lw=5.5, solid_capstyle="butt")
    ax.plot([70, 70], [54.4, 44], color=AZ, lw=5.5, solid_capstyle="butt")
    ax.text(41, 56.5, "alimentação (ponto de suprimento)", fontsize=8.5, color=AZ)
    # cota S
    ax.plot([70, 92], [44, 44], color=TX, lw=0.6, ls=":")
    cota(ax, (88, 44), (88, 32), "S", lado=(3.2, 0))
    ax.text(95, 38, "separação atmosférica\n(mínimo pela tabela)", fontsize=8, color=TX, va="center")
    # cota L
    ax.plot([70, 70], [44, 40], color=TX, lw=0.6, ls=":")
    cota(ax, (38, 40.5), (67.5, 40.5), "L ≥ 3d", lado=(0, -3.4))
    # diâmetro d
    cota(ax, (76, 54.6), (76, 49.4), "d", lado=(3, 0))
    ax.text(82, 52, "diâmetro interno do tubo", fontsize=7.5, color=TX, va="center")
    ax.text(66, 75, "A saída do tubo fica no ar, acima do nível de transbordamento:\na água do reservatório não tem como voltar para a tubulação.",
            ha="center", va="center", fontsize=8.3, color=TX, style="italic")
    salvar(fig, "e3_separacao")


# ---------------------------------------------------------------- E4: pressões
def e4():
    fig, ax = base(7.4, 2.9, (0, 148), (0, 58))
    y = 26
    xs = {0: 10, 5: 24, 10: 38, 400: 104, 600: 134}
    ax.add_patch(Rectangle((xs[0], y - 3), xs[5] - xs[0], 6, fc="#F4D6D0", ec="none"))
    ax.add_patch(Rectangle((xs[5], y - 3), xs[10] - xs[5], 6, fc="#FBEBC8", ec="none"))
    ax.add_patch(Rectangle((xs[10], y - 3), xs[400] - xs[10], 6, fc="#CFE8DB", ec="none"))
    ax.add_patch(Rectangle((xs[400], y - 3), xs[600] - xs[400] + 6, 6, fc="#F4D6D0", ec="none"))
    for v, x in xs.items():
        ax.plot([x, x], [y - 4.5, y + 4.5], color=TX, lw=1.3)
        ax.text(x, y - 8, f"{v}", ha="center", va="top", fontsize=9.5, fontweight="bold", color=TX)
    ax.text(xs[600] + 8, y - 8, "kPa", ha="left", va="top", fontsize=8.5, color=TX)
    ax.text((xs[10] + xs[400]) / 2, y, "faixa nos pontos de utilização", ha="center", va="center",
            fontsize=8.3, color=VD, fontweight="bold")
    ax.annotate("mínimo dinâmico em\nqualquer ponto da rede\n(0,5 mca)", xy=(xs[5], y + 4.5), xytext=(xs[5] - 8, y + 17),
                ha="center", va="bottom", fontsize=7.8, color=TX, arrowprops=dict(arrowstyle="-", color=CZ, lw=0.7))
    ax.annotate("mínimo dinâmico no\nponto de utilização\n(1 mca)", xy=(xs[10], y + 4.5), xytext=(xs[10] + 16, y + 17),
                ha="center", va="bottom", fontsize=7.8, color=TX, arrowprops=dict(arrowstyle="-", color=CZ, lw=0.7))
    ax.annotate("máximo estático no\nponto de utilização\n(40 mca)", xy=(xs[400], y + 4.5), xytext=(xs[400], y + 17),
                ha="center", va="bottom", fontsize=7.8, color=TX, arrowprops=dict(arrowstyle="-", color=CZ, lw=0.7))
    ax.annotate("pressão do ensaio\nde estanqueidade*", xy=(xs[600], y + 4.5), xytext=(xs[600], y + 17),
                ha="center", va="bottom", fontsize=7.8, color=TX, arrowprops=dict(arrowstyle="-", color=CZ, lw=0.7))
    ax.text(74, 8.5, "* 600 kPa ou 1,5 vez a máxima pressão de trabalho, o que for menor.",
            ha="center", va="center", fontsize=7.6, color=TX, style="italic")
    ax.text(74, 3.5, "Escala esquemática (fora de proporção). Sobrepressão por transientes: até 200 kPa acima da pressão dinâmica de projeto.",
            ha="center", va="center", fontsize=7.6, color=TX, style="italic")
    salvar(fig, "e4_pressoes")


# ---------------------------------------------------------------- E5: temperaturas
def e5():
    fig, ax = base(7.4, 3.4, (0, 148), (0, 68))
    y = 32
    pos = {38: 16, 45: 38, 70: 68, 80: 92, 90: 114, 95: 134}
    import numpy as np
    grad = np.linspace(0, 1, 256).reshape(1, -1)
    ax.imshow(grad, extent=(8, 142, y - 3, y + 3), cmap="YlOrRd", aspect="auto", vmin=-0.25, vmax=1.15, zorder=1)
    ax.add_patch(Rectangle((8, y - 3), 134, 6, fill=False, ec=CZ, lw=0.8, zorder=2))
    textos = {
        38: ("máximo recomendado:\nduchas higiênicas, jardins de\ninfância, certas clínicas e hospitais", "cima"),
        45: ("uso corporal: acima disso,\nlimitador automático\nobrigatório", "baixo"),
        70: ("limite em ambientes sanitários\ncom misturador convencional;\nmínimo da desinfecção térmica", "cima"),
        80: ("temperatura mínima\nda água no ensaio de\nestanqueidade", "baixo"),
        90: ("acima disso: precauções\ncontra danos ao sistema\ne aos usuários", "cima"),
        95: ("geração acima disso:\ncontrole térmico + corte\ncom intervenção manual", "baixo"),
    }
    for t, x in pos.items():
        ax.plot([x, x], [y - 4.5, y + 4.5], color=TX, lw=1.3, zorder=3)
        txt, lado = textos[t]
        if lado == "cima":
            ax.text(x, y + 6, f"{t} °C", ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=VM)
            ax.text(x, y + 11.5, txt, ha="center", va="bottom", fontsize=7.4, color=TX)
        else:
            ax.text(x, y - 6, f"{t} °C", ha="center", va="top", fontsize=9.5, fontweight="bold", color=VM)
            ax.text(x, y - 11.5, txt, ha="center", va="top", fontsize=7.4, color=TX)
    ax.text(75, 2.5, "Escala esquemática (fora de proporção).", ha="center", fontsize=7.6, color=TX, style="italic")
    salvar(fig, "e5_temperaturas")


# ---------------------------------------------------------------- E6: braço de flexão
def e6():
    fig, ax = base(6.2, 3.2, (0, 124), (0, 64))
    # ponto fixo à esquerda
    ax.add_patch(Rectangle((6, 44), 3, 12, fc=CZ, ec=CZ))
    ax.text(7.5, 59, "ponto fixo", ha="center", fontsize=7.8, color=TX)
    # trecho longo (frio)
    ax.plot([9, 84], [50, 50], color=VM, lw=4, solid_capstyle="butt")
    ax.plot([84, 84], [52, 14], color=VM, lw=4, solid_capstyle="butt")
    # posição dilatada (tracejada)
    import numpy as np
    ax.plot([84, 94], [50, 50], color=VM, lw=1.6, ls="--")
    ys = np.linspace(50, 14, 40)
    xs = 84 + 10 * ((ys - 14) / 36) ** 2
    ax.plot(xs, ys, color=VM, lw=1.6, ls="--")
    # ponto fixo inferior
    ax.add_patch(Rectangle((78, 9), 12, 3, fc=CZ, ec=CZ))
    ax.text(84, 4.5, "ponto fixo", ha="center", fontsize=7.8, color=TX)
    ax.text(46, 54.5, "trecho reto longo de água quente", ha="center", fontsize=8.3, color=TX)
    ax.annotate("", xy=(60, 46), xytext=(36, 46), arrowprops=dict(arrowstyle="->", color=VM, lw=1.0))
    ax.text(48, 42, "dilata ao aquecer", ha="center", fontsize=7.6, color=VM)
    cota(ax, (84, 57), (94, 57), "ΔL", lado=(0, 3.2))
    cota(ax, (104, 50), (104, 12), "braço de flexão", lado=(2.5, 0), fs=8.5, ha="left")
    ax.plot([94, 106], [50, 50], color=TX, lw=0.5, ls=":")
    ax.plot([90, 106], [12, 12], color=TX, lw=0.5, ls=":")
    salvar(fig, "e6_braco_flexao")


# ---------------------------------------------------------------- E7: refluxo em conjunto
def caixa(ax, x, y, w, h, texto, fc="white", ec=CZ, fs=8.3, cor=TX, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.2", fc=fc, ec=ec, lw=1.2))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=cor,
            fontweight="bold" if bold else "normal")


def e7():
    fig, ax = base(7.0, 2.9, (0, 140), (0, 58))
    caixa(ax, 2, 24, 22, 10, "rede\npública", fc=AZ_CL, ec=AZ)
    caixa(ax, 32, 24, 12, 10, "HD", ec=AZ, cor=AZ, bold=True)
    ax.plot([24.6, 31.4], [29, 29], color=AZ, lw=2.2)
    ax.plot([44.6, 66], [29, 29], color=AZ, lw=2.2)
    ax.plot([66, 66], [12, 46], color=AZ, lw=2.2)
    ax.text(55, 31.5, "tubulação\ncomum", ha="center", va="bottom", fontsize=7.8, color=TX)
    for y, nome in ((46, "Edificação A"), (12, "Edificação B")):
        ax.plot([66, 80], [y, y], color=AZ, lw=2.2)
        caixa(ax, 80, y - 5, 12, 10, "PR", fc="#FBEBC8", ec=AM, cor=AM, bold=True)
        ax.plot([92.6, 104], [y, y], color=AZ, lw=2.2)
        caixa(ax, 104, y - 6, 32, 12, nome, fc=CZ_CL)
    ax.text(90, 29, "um dispositivo de proteção\ncontra refluxo por edificação", ha="center", va="center",
            fontsize=7.8, color=AM, style="italic")
    salvar(fig, "e7_refluxo_conjunto")


for f in (e1, e2, e3, e4, e5, e6, e7):
    f()
print("ok")
