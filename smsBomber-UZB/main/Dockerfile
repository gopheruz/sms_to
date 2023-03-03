FROM python:3
WORKDIR /sms-bomb
# install dependencies  
COPY . ./
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt 
# copy whole project to your docker home directory.
# run this command to install all dependencies  
# start server  
CMD python3 main.py 