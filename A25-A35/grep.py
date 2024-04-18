import re


def grep(pattern, flags, files):


    match, inversed, line_nb, file_name, spam_name = [], [], [], [], []

    xmatch = pattern if "-x" not in flags.split() else "^" + pattern + "$"

    for file in files:

        with open(file, encoding="UTF8") as f:

            for i, line in enumerate(f.readlines()):

                p = xmatch if "-i" not in flags.split() else xmatch.lower()

                l = line if "-i" not in flags.split() else line.lower()

                if re.search(p, l):

                    match.append(line)

                    inversed.append(False)

                else:

                    inversed.append(line)

                    match.append(False)


                if (

                    file + "\n" not in file_name

                    and "-l" in flags.split()

                    and (

                        ("-v" not in flags.split() and re.search(p, l))

                        or ("-v" in flags.split() and not re.search(p, l))

                    )

                ):

                    file_name.append(file + "\n")

                line_nb.append(str(i + 1))


                spam_name.append(file)

    out = []

    for i, nb in enumerate(line_nb):

        title = spam_name[i] if len(files) > 2 else ""

        n = nb if "-n" in flags.split() else ""

        tmp = ""

        if "-v" in flags.split() and inversed[i]:

            tmp = ":".join(x for x in [title, n, inversed[i]] if x)

        elif "-v" not in flags.split() and match[i]:

            tmp = ":".join(x for x in [title, n, match[i]] if x)


        if tmp:

            out.append(tmp)

    if (any(match) and "-v" not in flags.split()) or (

        any(inversed) and "-v" in flags.split()

    ):

        if "-l" in flags.split():

            if len(file_name) == 1:

                return file_name[0]

            return "".join(file_name)

        return "".join(out)
    return ""
