import scraper as web
import dumper as dmp
import resolver as rslv
import sys

if len(sys.argv) < 2:
    print("Usage: oca [URL]")
    exit(0)

url = sys.argv[1]
chall = web.get_challenge(url)
dmp.print_chall(chall)
web.download_files(chall)
resolver = rslv.PlResolve(chall)
resolver.load_plugins()
resolver.run_plugins()