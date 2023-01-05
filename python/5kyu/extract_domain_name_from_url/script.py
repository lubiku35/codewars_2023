def domain_name(url):
    prefix = ['http://', 'https://', 'http://www.', 'https://www.', 'www.']
    for x in prefix:
        if url.startswith(x): url = url.replace(x, '')
    return url[:url.find('.')]




