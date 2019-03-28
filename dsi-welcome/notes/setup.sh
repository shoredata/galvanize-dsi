## Setup a data science development mac mini box

xcode-select --install

touch ~/.bashrc
touch ~/.bash_profile

# Install homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## Mac apps
brew tap caskroom/cask
brew install brew-cask
brew cask install google-chrome
brew cask install firefox
brew cask install mou
brew cask install iterm2
brew cask install xquartz
brew cask install virtualbox
brew cask install vagrant
brew cask install sublime-text
brew cask install postgres
brew cask install pgadmin3
brew cask install gephi
brew cask install java

echo 'export PATH="~/Applications/Postgres.app/Contents/Versions/latest/bin/:$PATH"' >> ~/.bash_profile
 
## mac packages
brew install wget
brew install mongodb
brew install graphviz
brew install imagemagick
brew install terminal-notifier
brew install gcc
 
cd /Applications
wget https://justgetflux.com/mac/Flux.zip
unzip Flux.zip
rm Flux.zip

# Run the rest of the script from a safe place
cd /tmp
 
# python
curl -L http://repo.continuum.io/archive/Anaconda2-4.0.0-MacOSX-x86_64.sh > anaconda_script.sh
bash anaconda_script.sh
# update Anaconda to current version
conda update conda
conda update anaconda
rm ~/Desktop/Launcher.app
rm anaconda_script.sh
source ~/.bash_profile
conda install --yes statsmodels
conda install --yes networkx
conda install --yes pymc
pip install pymongo
wget -nc http://py.processing.org/processing.py-0202-macosx.tgz
conda install -c https://conda.binstar.org/trent psycopg2
rm processing.py-0202-macosx.tgz
pip install unittest2
pip install pytest

# vowpal wabbit
brew install automake
brew install libtool
brew install boost
brew install boost-build
brew install vowpal-wabbit

# git clone https://github.com/JohnLangford/vowpal_wabbit.git ~/vowpal_wabbit
# cd ~/vowpal_wabbit
# autoreconf --force --install      # Options copy any needed autoconf files to local
# ./configure
# make
# make install
# cd

# graphlab
sudo pip install graphlab-create
echo '[Product]
product_key=D868-7DBE-AC8A-0343-45F3-E250-34B4-24CA' > ~/.graphlab/config

source ~/.bash_profile
echo "print 'hi'" > hello.py
ipython hello.py
rm hello.py

# iPython startup files
curl https://gist.githubusercontent.com/rsepassi/2cdde6c6d4b36916cb37/raw/e8fe5ba808fb9701fb13d3e8e35c49fb333d0b46/autoreload_startup.ipy > ~/.ipython/profile_default/startup/autoreload_startup.ipy
curl https://gist.githubusercontent.com/rsepassi/aa5618ed05fad3279cd2/raw/3d924a57789c30d2aab6bbbe7b1301d0d79b0282/data_stack.py > ~/.ipython/profile_default/startup/data_stack.py

# Countdown timer
curl https://gist.githubusercontent.com/rsepassi/51129804cd6fae107a84/raw/74f41346994a1cdd79d500fa840e29c710a7a872/countdown.sh >> ~/.bashrc
 
# R
brew update
brew tap homebrew/science
brew install r

echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
echo "source ~/.bashrc" >> ~/.bash_profile

# You may need to run this several times because it may time out...
echo 'import nltk
nltk.download("all")' | python

pip install seaborn
pip install plotly
pip install flask
pip install graphlab-create
pip install mrjob
pip install mechanize
brew install pig
brew install hive
brew install git
brew install --HEAD hub
