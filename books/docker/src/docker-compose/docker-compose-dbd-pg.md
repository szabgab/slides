# Docker Compose for Perl DBD::Pg (PostgreSQL)


These files were used to set up a local development environment for the Perl module [DBD::Pg](https://metacpan.org/pod/DBD::Pg)

```
git clone https://github.com/bucardo/dbdpg.git
cd dbdpg
```

Put the two files in that folder:

{% embed include file="src/examples/compose-for-dbd-pg/Dockerfile" %}

{% embed include file="src/examples/compose-for-dbd-pg/docker-compose.yaml" %}

In one terminal start Docker compose:

```
docker-compose up
```

In another terminal connect to the client container

```
docker exec -it dbdpg_client_1 bash
```

Now you can run the tests:

```
perl Makefile.PL
make
AUTHOR_TESTING=1
RELEASE_TESTING=1
make test
```

And you can also generate test coverage report:

```
cover -test
```


