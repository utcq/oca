import core.scraper as web
import utils.dumper as dmp
import core.resolver as rslv
import sys

if len(sys.argv) < 2:
    print("Usage: oca [URL]")
    exit(0)

url = sys.argv[1]
chall = web.Scraper(url).get_challenge()
chall.resolve_tags()
dmp.print_chall(chall)
chall.get_files()
resolver = rslv.PlResolve(chall)
resolver.load_plugins()
resolver.run_plugins()