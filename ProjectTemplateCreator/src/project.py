import templates, sys

if __name__ == "__main__":

    tmpl = templates.Templates()

    try:
        arg = sys.argv[1]
    except IndexError:
        print("WARNING: No template type argument passed, will use default one instead [p5.js].")
        arg = "p5.js"

    if arg == "-h":
        tmpl.Help()
        sys.exit()

    tmpl.CopyTemplate(arg)
