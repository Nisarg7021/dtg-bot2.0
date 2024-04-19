if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Nisarg7021/dtg-bot2.0.git /dtg-bot2.0
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /dtg-bot2.0
fi
cd /dtg-bot2.0
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m main
https://github.com/
