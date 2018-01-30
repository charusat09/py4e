import urllib.request, urllib.parse, urllib.error, re
urlfile = open('list_of_urls1.txt', 'a')
urls = ["https://mayurkumar.info/blog", "https://stackoverflow.com/questions/44760247/python3-string-interpolation-two-ways-neither-one-works"]

for url in urls:
    filehandle = urllib.request.urlopen(url)
    domain = re.findall('^(http.*\/\/.[^ ]+?\/)', url)[0]

    urlfile.write("-"*70)
    urlfile.write("\n")
    urlfile.write("Logs for:- {}\n".format(domain))
    urlfile.write("-"*70)
    urlfile.write("\n")

    url_count = 0
    counts = dict()
    for line in filehandle:
        href = re.findall('href="(.[^ >]*)"', line.decode())
        for url in href:
            url_count += 1
            counts[url] = counts.get(url, 0) + 1

    print(counts)
    count_list = list()
    sorted_list = sorted([(count, url) for url, count in counts.items()], reverse=True)

    for count, url in sorted_list:
        if not re.search("http", url):
            url = "{}{}".format(domain, url[1:-1])
        urlfile.write('url: {}\n'.format(url))
        urlfile.write('count: {}\n'.format(count))

    urlfile.write("-"*70)
    urlfile.write("\n")
    urlfile.write("Total URLs tracked: {}\n".format(url_count))
    urlfile.write("-"*70)
    urlfile.write("\n")
urlfile.close()
