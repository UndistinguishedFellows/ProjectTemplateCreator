import templates, sys

DEFAULT_JSON_URL = "https://bitbucket.org/Josef21296/various-resources/raw/56762ae64644c9ae65a7b0ce26220799010aaa28/Templates/templates_source.json"

if __name__ == "__main__":

    try:
        arg = sys.argv[1]
    except IndexError:
        print("WARNING: No template type argument passed, will use default one instead.")
        arg = "default"

    tmpl = templates.Templates(data_url=DEFAULT_JSON_URL)

    if arg == "-h":
        tmpl.Help()
        sys.exit()

    tmpl.CopyTemplate(arg)
