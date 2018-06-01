import templates, sys

if __name__ == "__main__":

    try:
        proj = sys.argv[1]
    except IndexError:
        print("WARNING: No template type argument passed, will use default one instead.")
        proj = "default"

    tmpl = templates.Templates(data_url=templates.DEFAULT_JSON_URL)

    if proj == "-h":
        tmpl.Help()
        sys.exit()

    tmpl.CopyTemplate(proj)
