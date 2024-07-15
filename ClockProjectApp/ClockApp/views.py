from datetime import datetime

from django.shortcuts import render

# Create your views here.
def digital_clock(request):
    ora_curenta = datetime.now()
    formatare_ora_curenta = ora_curenta.strftime("%H:%M:%S")
    formatare_ora_curenta = formatare_ora_curenta.replace(":", "o").replace(" ", "o")
    dict_ora = {

        '0': [
            " _ ",
            "| |",
            "|_|"
        ],
        '1': [
            "   ",
            "  |",
            "  |"
        ],
        '2': [
            " _ ",
            " _|",
            "|_ "
        ],
        '3': [
            " _ ",
            " _|",
            " _|"
        ],
        '4': [
            "   ",
            "|_|",
            "  |"
        ],
        '5': [
            " _ ",
            "|_ ",
            " _|"
        ],
        '6': [
            " _ ",
            "|_ ",
            "|_|"
        ],
        '7': [
            " _ ",
            "  |",
            "  |"
        ],
        '8': [
            " _ ",
            "|_|",
            "|_|"
        ],
        '9': [
            " _ ",
            "|_|",
            " _|"
        ],
        'o': [
            "   ",
            " o ",
            " o "
        ]
    }

    afisare_linii = ["", "", ""]
    for char in formatare_ora_curenta:
        if char in dict_ora:
            numar = dict_ora[char]
            for i in range(3):
                afisare_linii[i] += numar[i] + "   "

    return render(request, "ClockApp/clock.html", {"afisare_linii": afisare_linii})

