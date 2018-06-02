import templates, sys, os

if __name__ == "__main__":

    try:
        proj = sys.argv[1]
    except IndexError:
        print("WARNING: No project template passed, will use default one instead.")
        proj = "default"

    local_json = os.path.join(os.path.dirname(os.path.realpath(__file__)), templates.DEFAULT_JSON_NAME)
    tmpl = templates.Templates(data_path=local_json, data_url=templates.DEFAULT_JSON_URL)

    if proj == "-h":
        tmpl.Help()
        sys.exit()

    tmpl.CopyTemplate(proj)
