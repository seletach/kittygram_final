FROM python:3.9 

WORKDIR /app 
 
COPY requirements.txt . 
 
RUN pip install -r requirements.txt --no-cache-dir 
 
COPY . .

RUN chmod +x ./backend_static_script.sh

ENTRYPOINT [ "./backend_static_script.sh" ]

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "kittygram_backend.wsgi"]
