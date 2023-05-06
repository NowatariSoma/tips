# docker のコマンド

dockerを起動
```
sudo service docker start
```
dockerを終了
```
sudo service docker stop
```

## docker のイメージを起動

現在いるディレクトリの下にtargetというディレクトリを作り，docker 上のappディレクトリにマウントする．
```
docker run -d -it --name devtest -v "$(pwd)"/target:/app cupy/cupy
```
ほぼ上と同じ．現在いるディレクトリをdockerのappにマウントする．
docker run -it --name tmp -v "$(pwd)":/app cupy/cupy
```


sudo chown nowatari target/
sudo chgrp nowatari target/


cupyを動かす時にひたすらエラーが出た
環境変数を返納していなかったせいっぽい