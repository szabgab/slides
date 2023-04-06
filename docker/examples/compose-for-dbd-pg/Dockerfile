FROM perl:5.36
RUN apt-get update && \
    apt-get install -y libaspell-dev
RUN cpanm --notest DBI Perl::Critic Text::SpellChecker Devel::Cover


# docker build -t dbdpg .
# docker run -it --workdir /opt -v$(pwd):/opt --name dbdpg dbdpg bash
# docker container start -i dbdpg


