# Extract the domain name from a URL

## Challenge Description

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```

## Challenge Solutions

### Solution 01

```python
def domain_name(url):
    prefix = ['http://', 'https://', 'http://www.', 'https://www.', 'www.']
    for x in prefix:
        if url.startswith(x): url = url.replace(x, '')
    return url[:url.find('.')]
```

**DESCRIPTION:**

I really liked this one, first of all we check if out url starts with exact prefix as you can see in solution, if true, then replace it for nothing, and then we just return string util it’s find first dot