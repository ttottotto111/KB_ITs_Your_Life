
# 

cd /content

echo "Installing konlpy....."
! pip3 install konlpy
echo "Done"


echo "Installing mecab-0.996-ko-0.9.2.tar.gz....."

echo "Downloading mecab-0.996-ko-0.9.2.tar.gz......."
echo "from https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz"
! wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz 
echo "Done"

echo "Unpacking mecab-0.996-ko-0.9.2.tar.gz......."
! tar xvfz mecab-0.996-ko-0.9.2.tar.gz > /dev/null 2>&1 
echo "Done"

echo "Change Directory to mecab-0.996-ko-0.9.2......."
cd mecab-0.996-ko-0.9.2/

echo "installing mecab-0.996-ko-0.9.2.tar.gz........"
echo 'configure'
! ./configure > /dev/null 2>&1
echo 'make'
! make > /dev/null 2>&1
echo 'make check'
! make check > /dev/null 2>&1
echo 'make install'
! make install > /dev/null 2>&1

echo 'ldconfig'
! ldconfig > /dev/null 2>&1
echo "Done"

echo "Change Directory to /content"
cd ../

echo "Downloading mecab-ko-dic-2.1.1-20180720.tar.gz......."
echo "from https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz"
! wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
echo "Done"
 
echo "Unpacking  mecab-ko-dic-2.1.1-20180720.tar.gz......."
! tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz > /dev/null 2>&1
echo "Done"

echo "Change Directory to mecab-ko-dic-2.1.1-20180720"
cd mecab-ko-dic-2.1.1-20180720/
echo "Done"

echo "installing........"
echo 'configure'
! ./configure > /dev/null 2>&1
echo 'make'
! make > /dev/null 2>&1
echo 'make install'
! make install > /dev/null 2>&1

echo 'bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/v0.6.0/scripts/mecab.sh)'
echo 'https://github.com/konlpy/konlpy/issues/395#issue-1099168405 - 2022.01.11'
#! bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)  > /dev/null 2>&1
! bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/v0.6.0/scripts/mecab.sh)  > /dev/null 2>&1
echo "Done"

echo "Successfully Installed"

echo "Now you can use Mecab"
echo "from konlpy.tag import Mecab"
echo "mecab = Mecab()"

echo "????????? ?????? ?????? ?????? : https://bit.ly/3k0ZH53"

echo "NameError: name 'Tagger' is not defined ?????? ?????? ??? ???????????? ????????? ????????????"
echo "???????????? ?????? ????????? ???????????? tana??? ???????????????."
echo "light ?????? ?????? : Dogdriip??? ( https://github.com/Dogdriip )"
echo "????????? ??????????????? combacsa??? ???????????????."
