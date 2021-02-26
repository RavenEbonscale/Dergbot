From python:3.8

WORKDIR /code

RUN pip  install praw
RUN pip install discord.py
RUN pip install python-dotenv
RUN pip install pytube
RUN pip install ffmpeg
RUN pip install tqdm


COPY ./ .
COPY discord.env .
CMD ["python","-u","DergBot.py"]