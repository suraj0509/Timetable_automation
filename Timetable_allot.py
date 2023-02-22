theory_3 = ["chem", "beee"]
theory_2 = ["maths discrete", "maths graph"]
theory_1 = []
lab_3 = ["CSEPY", "CSEPY"]
lab_2 = ["CSEPY", "CSEPY"]
lab_1 = []

sample_timetable = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "TH12"],
                    ["I1", "H1", "B1", "A1", "G1", "TE12", "TD11", "TC11"],
                    ["B1", "A1", "C1", "D1", "E1", "F1", "TH11", "TI11"],
                    ["H1", "I1", "G1", "TC12", "TE11", "TF11", "TB12", "TA12"],
                    ["H1", "I1", "D1", "C1", "E1", "F1", "TA11", "TB11"]]


def get_rcode(a):
    nob = ["B", 0, "TB", 0]
    noc = ["C", 0, "TC", 0]
    nod = ["D", 0, "TD", 0]
    noe = ["E", 0, "TE", 0]
    nof = ["F", 0, "TF", 0]
    nog = ["G", 0, "TG", 0]
    noh = ["H", 0, "TH", 0]
    noi = ["I", 0, "TI", 0]
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            if len(a[i][j]) == 2 or len(a[i][j]) == 3 or len(a[i][j]) == 4:
                if a[i][j][0] == 'B':
                    nob[1] = nob[1] + 1
                if a[i][j][0] == 'C':
                    noc[1] = noc[1] + 1
                if a[i][j][0] == 'D':
                    nod[1] = nod[1] + 1
                if a[i][j][0] == 'E':
                    noe[1] = noe[1] + 1
                if a[i][j][0] == 'F':
                    nof[1] = nof[1] + 1
                if a[i][j][0] == 'G':
                    nog[1] = nog[1] + 1
                if a[i][j][0] == 'H':
                    noh[1] = noh[1] + 1
                if a[i][j][0] == 'I':
                    noi[1] = noi[1] + 1
                if a[i][j][0:2] == 'TB':
                    nob[3] = nob[3] + 1
                if a[i][j][0:2] == 'TC':
                    noc[3] = noc[3] + 1
                if a[i][j][0:2] == 'TD':
                    nod[3] = nod[3] + 1
                if a[i][j][0:2] == 'TE':
                    noe[3] = noe[3] + 1
                if a[i][j][0:2] == 'TF':
                    nof[3] = nof[3] + 1
                if a[i][j][0:2] == 'TG':
                    nog[3] = nog[3] + 1
                if a[i][j][0:2] == 'TH':
                    noh[3] = noh[3] + 1
                if a[i][j][0:2] == 'TI':
                    noi[3] = noi[3] + 1
    list = [nob, noc, nod, noe, nof, nog, noh, noi]
    return list


def gen_set01(theory_3, theory_2, theory_1, lab_3, lab_2, lab_1, sample_timetable):
    set_1_timetable = sample_timetable
    lab_3_comb = []
    dict_exact, dict_comb = {}, {}
    for x in set_1_timetable:
        x[4] = "Lunch"
    lab_3_comb = [[set_1_timetable[0][0], set_1_timetable[0][1], set_1_timetable[1][2], set_1_timetable[1][3],
                   set_1_timetable[2][0], set_1_timetable[2][1]],
                  [set_1_timetable[1][0], set_1_timetable[1][1], set_1_timetable[3][0], set_1_timetable[3][1],
                   set_1_timetable[4][0], set_1_timetable[4][1]],
                  [set_1_timetable[0][2], set_1_timetable[0][3], set_1_timetable[2][2], set_1_timetable[2][3],
                   set_1_timetable[4][2], set_1_timetable[4][3]]]
    lab_2_comb = [[set_1_timetable[0][6], set_1_timetable[0][7], set_1_timetable[3][2], set_1_timetable[3][3]],
                  [set_1_timetable[4][6], set_1_timetable[4][7], set_1_timetable[3][6], set_1_timetable[3][7]]]
    for x in range(0, len(lab_3)):
        for y in lab_3_comb[x]:
            for l in range(len(set_1_timetable)):
                for m in range(len(set_1_timetable[l])):
                    if set_1_timetable[l][m] == y:
                        set_1_timetable[l][m] = lab_3[x]
    for x in range(0, len(lab_2)):
        for y in lab_2_comb[x]:
            for l in range(len(set_1_timetable)):
                for m in range(len(set_1_timetable[l])):
                    if set_1_timetable[l][m] == y:
                        set_1_timetable[l][m] = lab_2[x]

    rem_codes = get_rcode(set_1_timetable)
    for i in rem_codes:
        print(i)
    for i in rem_codes:
        if len(theory_3) > 0:
            if i[1] + i[3] >= 3:
                if i[1] == 3:
                    dict_exact[i[0]] = theory_3[0]
                theory_3.pop(0)
            else:
                dict_comb[i[0]] = theory_3[0]
                dict_comb[i[2]] = theory_3[0]
                theory_3.pop(0)
    for i in set_1_timetable:
        print(i)
    print(dict_exact, dict_comb)


gen_set01(theory_3, theory_2, theory_1, lab_3, lab_2, lab_1, sample_timetable)
