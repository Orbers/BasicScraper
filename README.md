# BasicScraper

## 1. Set up local environment variables
You can add local variables in a file called **config.ini* in root of project directory
This file should look like:

```bash
[LocalEnvironment]
chrome_path=/Applications/chromedriver
```

Where the chrome_path (above as '/Applications/chromedriver') is the folder where you have chromedriver installed

A typical configuration for a Windows PC might be:
```python
chromedriver = "\windows\chromedriver"
```

And a typical configuration for a MAC might be:
```python
chromedriver = "\Applications\chromedriver"
```
