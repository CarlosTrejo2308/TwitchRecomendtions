FROM python:3

WORKDIR /home/j_alejandro/Visual SC/NR/TwitchRecomendtions

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/saves/main.py" ]