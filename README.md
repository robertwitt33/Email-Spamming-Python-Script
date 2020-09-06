# Email-Spamming-Python-Script

In this project, I was able to run this code in Visual Studio code for it to execute. It would first log into my Yahoo! Mail account, and from there it would send as many emails as I would like. All of this was automated.

The Python Library that I used for this was called Selenium. With this library, I was able to click on buttons and type in text boxes. This is essentially all that you need to do this project, but there are some other obstacles that you need to overcome as well. I had to reload the web page at a certain part of the script because Yahoo! was bringing me to different pages each time I logged in. This randomness may be to protect accounts from bots, but it did not fool me. After I signed in, I simply searched for Yahoo! Mail in the search bar and it pulled up my email inbox. From there, it would start sending the emails.

Another library that I used was the time library for Python. I was able to add delays in my code so that the computer could not recognize the automation as easily. From the computer’s perspective, it just looks like a very weird guy slowly sending a handful of emails out.



You are able to test this script out for yourself! Make sure you have Python downloaded, and from there you can use pip to download the Selenium library. From there, you can edit the username and the password, edit the amount of emails you would like to send, then click run!
