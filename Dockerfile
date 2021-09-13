FROM python:2.7-slim
RUN apt-get update && apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-recommended && apt-get clean
COPY ./ /
COPY names/ /
RUN pip install -r requirements.txt
ADD flask_webapp.py /
ADD genpdf.py /
CMD [ "python", "./flask_webapp.py" ]
EXPOSE 5000

