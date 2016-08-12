sed -i '/^\s*$/d' rawjson.json
sed -i 's/\\u....//g' rawjson.json
sed -i 's/\\\///g' rawjson.json
#sed -i 's/\s*[^}]$/""\}/g' parsertest.json
#sed -i 's/\}""\}/\}/g' parsertest.json
