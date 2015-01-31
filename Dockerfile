# Base off of OpenSUSE latest.
FROM opensuse:latest

RUN zypper --non-interactive --no-gpg-checks ref
RUN zypper --non-interactive up
RUN zypper --non-interactive in python3 python3-pip python3-virtualenv git python3-devel gcc make

ENV PATH=/virtualenv/bin:$PATH

RUN mkdir /mesosphere

COPY ./requirements.txt /mesosphere/

RUN mkdir virtualenv && virtualenv /virtualenv

RUN pip install -r /mesosphere/requirements.txt
RUN pip install gunicorn

COPY ./ /mesosphere

EXPOSE 8000

CMD cd /mesosphere && gunicorn -b 0.0.0.0:8000 mesosphere.wsgi:application
