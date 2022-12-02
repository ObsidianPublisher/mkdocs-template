from datetime import datetime
from dateutil import parser
from pathlib import Path
import urllib.parse
from babel.dates import format_date
import obsidiantools.api as otools
import os
import shutil
from pyvis.network import Network

print('COUCOU')
print(os.getcwd())
print(os.path.exists(Path(os.getcwd(), 'lib')))

def obsidian_graph():
    print('generate obsidian graph')
    vault = otools.Vault(os.getcwd()).connect().gather()
    graph = vault.graph
    net = Network(height="750px", width="750px", font_color="#7c7c7c", bgcolor="transparent")
    net.from_nx(graph)
    try:
        net.save_graph(str(Path(os.getcwd(), 'docs', 'assets', 'graph.html')))
    except OSError:
        pass
    shutil.rmtree(Path(os.getcwd(), 'lib'))
    print('done')
    return ''

obsidian_graph()

def logging(text):
    print(text)
    return ''

def time_time(time):
    time=time.replace('-', '/')
    time = parser.parse(time).isoformat()
    try:
        time = datetime.fromisoformat(time)
        return datetime.strftime(time,'%d %B %Y')
    except AttributeError:
        return datetime.strftime(str(time),'%d %B %Y')
    except ValueError:
        print('value error!')
        return time

def to_local_time(time, locale):
    date = time.replace('-', '/')
    date = parser.parse(date)
    return format_date(date, locale=locale)


def time_todatetime(time):
    return parser.parse(time)

def time_to_iso(time):
    time=time.replace('-', '/')
    
    try:
        return parser.parse(time).isoformat()
    except AttributeError:
        return time

def page_exists(page):
    return Path(page).exists()

def url_decode(url):
    return urllib.parse.unquote(url)

def on_env(env, config, files, **kwargs):
    env.filters['convert_time'] = time_time
    env.filters['iso_time'] = time_to_iso
    env.filters['time_todatetime'] = time_todatetime
    env.filters['page_exists'] = page_exists
    env.filters['url_decode'] = url_decode
    env.filters['logging'] = logging
    env.filters['to_local_time'] = to_local_time
    return env