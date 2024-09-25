Overview
This Python script is designed to monitor the availability of multiple URLs and check if they are up and showing a sign-in page. It runs on a continuous loop and uses color-coded output to indicate the status of each monitored URL.

Features:
Sign-in page detection: Detects if a URL returns a specific status code (401) indicating a sign-in page.
Customizable URLs: Easily monitor multiple URLs by adding them to the list.
Colored output: Uses ANSI escape codes to show status messages in different colors:
Green: Sign-in page detected.
Yellow: Page is up, but no sign-in page detected.
Red: Errors or the message indicating when the next check will occur.
Prerequisites
You will need to have Python 3.x installed on your machine. Additionally, the script requires the requests library to send HTTP requests to the URLs.
Install Dependencies: pip install requests
