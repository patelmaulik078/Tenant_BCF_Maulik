import yaml
import jinja2
from pprint import pprint

def segment_load():
# load Yaml file

    with open('test.yaml') as f:
        segment = yaml.safe_load(f.read())
    return segment


def main():
 # Render Jinja template from segment_jinja2

    segment=segment_load()
    l3_var = {
        "segment": segment,
        "dhcp" : segment['dhcp']
    }
    templates = jinja2.Environment(loader=jinja2.FileSystemLoader('jinja_template'), autoescape=True)

    output = templates.get_template('new_segment.jinja2').render(l3_var)
    print(output)

if __name__ == '__main__':
    main()











