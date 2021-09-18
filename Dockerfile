FROM python:3.8.10-slim

RUN apt-get update \
    && apt-get install -y \
        imagemagick libmagickwand-dev \
        ghostscript --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ARG imagemagic_config=/etc/ImageMagick-6/policy.xml

RUN if [ -f $imagemagic_config ] ; \ 
    then sed -i 's/<policy domain="coder" rights="none" pattern="PDF" \/>/<policy domain="coder" rights="read|write" pattern="PDF" \/>/g' \
    $imagemagic_config ; else echo did not see file $imagemagic_config ; fi

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]