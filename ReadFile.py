def read_verbi_intransitivi():

    verbi_intransitivi = []

    with open('verbi_intransitivi.txt', encoding="utf-8") as fp:
        try:
            line = fp.readline()
            cnt = 1
            while line:
                verbi_intransitivi.append(line.strip())
                line = fp.readline()
                cnt += 1
        finally:
            fp.close()

    return verbi_intransitivi


def read_verbi_riflessivi():

    verbi_riflessivi = []

    with open('verbi_riflessivi.txt', encoding="utf-8") as fp:
        try:
            line = fp.readline()
            cnt = 1
            while line:
                verbi_riflessivi.append(line.strip())
                line = fp.readline()
                cnt += 1
        finally:
            fp.close()

    return verbi_riflessivi



