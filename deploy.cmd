::
:: Deploy to GAE
::
:: What's the date on Windows
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "timestamp=%HH%%Min%%Sec%"
set "datestamp=%YYYY%-%MM%-%DD%"
::
:: Then deploy
c:\python27\python "C:\Program Files (x86)\Google\google_appengine\appcfg.py"^
 update ./web_app -V %datestamp% 
:: C:\Python27\python "c:\Program Files\Google\google_appengine\appcfg.py"^
:: update ./web_app -V %datestamp% 
pause