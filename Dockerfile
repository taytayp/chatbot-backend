FROM python:2

WORKDIR /home/tay/Documents/chatbot-backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python" ]
