# Token Calc

计算任何数据集`json`的Token数，动态支持各种json格式，只需准备好你的json文件即可。

# How to use

## Quick start

```bash
pip install -r requirements.txt
python calc_token.py <your-file.json>
```

## Local setup

Linux

### In online mode computer

1. start python venv

```bash
python -m venv env
source env/bin/activate
```

2. install python packages

```bash
pip install -r requirements.txt
```

3. run once

```bash
python calc_token.py <your-file.json>
```

4. copy tmp file

Because `tiktoken` package need online download `cl100k_base` in cache. We can download the necessary file, then "trick" tiktoken into caching it.
https://stackoverflow.com/questions/76106366/how-to-use-tiktoken-in-offline-mode-computer

```bash
cp -r /tmp/data-gym-cache .
```

5. tar.gz
```bash
cd ..
tar -czvf token-calc.tar.gz token-calc
```

### In your offline mode computer

6. setup env
```bash
tar -zxvf token-calc.tar.gz
cd token-calc
cd env/bin && rm python* && ln -s python3 python && ln -s python3 python3.10 && ln -s /usr/bin/python3 python3
vi activate # Edit "VIRTUAL_ENV" to your current dir
source env/bin/activate
```

7. copy tmp files
```bash
cp -r data-gym-cache /tmp
```

8. run python
```bash
python calc_token.py <your-file.json>
```