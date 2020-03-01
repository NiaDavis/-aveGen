import re
from  six.moves.urllib.request import urlopen
def main():
    f = str(urlopen("https://quote.cnbc.com/quote-html-webservice/quote.htm?noform=1&partnerId=2&fund=1&exthrs=0&output=json&symbolType=issue&symbols=599362|579435|593933|49020635|49031016|5093160|617254|601065&requestMethod=extended").read())
    f.replace("\n", " ")
    pattern = re.compile(r'\"change_pct\":\"(-?[0-9.]+?)\".*?last\":\"([0-9.]+?)\".*?\"change\":\"(-?[0-9.]+?)\".*?\"onAirName\":\"(.+?)\"', flags = re.DOTALL)
    matches = re.findall(pattern, f)
    chart = [[matches[i][3], matches[i][1], matches[i][2], matches[i][0]] for i in range(len(matches))]
    print(chart)
main()
