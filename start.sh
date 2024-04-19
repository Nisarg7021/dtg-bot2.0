echo "Cloning Koyeb branch"
git clone -b koyeb https://github.com/Nisarg7021/DTG-linkszad-bot /DTG-linkszad-bot

cd /DTG-linkszad-bot || exit

pip3 install -U -r requirements.txt

echo "Starting Bot...."
python3 -m main



