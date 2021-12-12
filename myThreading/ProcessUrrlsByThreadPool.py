import concurrent.futures
import urllib.request

URLS = [
    'http://www.foxnews.com/',
    'http://www.cnn.com/',
    'http://europe.wsj.com/',
    'http://www.bbc.co.uk/',
    'http://some-made-up-domain.com/'
]

def loadUrl(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def processUrls():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futureToUrl = {executor.submit(loadUrl, url, 60): url for url in URLS} #submitted to thread pool, ==> map
        for future in concurrent.futures.as_completed(futureToUrl):
            url = futureToUrl[future] #getting url from map by giving future object
            try:
                data = future.result()
            except Exception as ex:
                print(f'{url} generated an exception {str(ex)}')
            else:
                print(f'{url} page is {len(data)} bytes')


if __name__ == '__main__':
    processUrls()
