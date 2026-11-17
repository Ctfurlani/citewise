# Redis

Redis (; Remote Dictionary Server) is an in-memory key–value database, used as a distributed cache and message broker, with optional durability. Because it holds all data in memory and because of its design, Redis offers low-latency reads and writes, making it particularly suitable for use cases that require a cache.

The project was developed and maintained by Salvatore Sanfilippo, starting in 2009. From 2015 until 2020, he led a project core team sponsored by Redis Labs. Salvatore Sanfilippo left Redis as the maintainer in 2020. In 2021 Redis Labs dropped the Labs from its name and now is known simply as "Redis".

In 2018, some modules for Redis adopted a modified Apache 2.0 license with a Commons Clause. In 2024, the main Redis code switched from the open-source BSD-3 license to being dual-licensed under the Redis Source Available License v2 and the Server Side Public License v1. On May 1, 2025, Redis became tri-licensed beginning with version 8.0, with the GNU Affero General Public License as the third option.

The name Redis means Remote Dictionary Server. The Redis project began when Salvatore Sanfilippo (nicknamed antirez) was trying to improve the scalability of his Italian startup and developed a real-time web log analyzer. After encountering significant problems in scaling some types of workloads using traditional database systems, Sanfilippo began in 2009 to prototype a first proof of concept version of Redis in Tcl. Later, Sanfilippo translated that prototype to the C language and implemented the first data type, the list. After a few weeks of using the project internally with success, Sanfilippo decided to open source it, announcing the project on Hacker News. The project began to get traction, particularly among the Ruby community, with GitHub and Instagram being among the first companies adopting it.

Sanfilippo was hired by VMware in March 2010.

In May 2013, Redis was sponsored by Pivotal Software (a VMware spin-off).

In June 2015, development became sponsored by Redis Ltd.

In August 2018, to control usage of the software by managed cloud providers without adequate compensation, Redis Ltd. announced that it would relicense the optional Redis modules from the GNU Affero General Public License (AGPL) to the Apache License, but subject to an addendum known as the "Commons Clause" that restricts commercial usage. This made the modules source-available and no longer free software. The core Redis software remained under a BSD license, with Redis Ltd. committing to maintaining these terms.

In October 2018, Redis 5.0 was released, introducing Redis Stream – a new data structure that allows storage of multiple fields and string values with an automatic, time-based sequence at a single key.

In February 2019, citing confusion over the licensing terms, the Apache License with Commons Clause licensing terms for Redis modules was replaced with the "Redis Source Available License" (RSAL), which explicitly prohibits commercial use of the modules as part of "a database, a caching engine, a stream processing engine, a search engine, an indexing engine or an ML/DL/AI serving engine." The last revision of the modules under a free and open source license were forked by community members as the GoodFORM project.

In June 2020, Salvatore Sanfilippo stepped down as Redis' sole maintainer. Sanfilippo was succeeded by Yossi Gottlieb and Oran Agra.

In March 2024, Redis Ltd. announced that beginning with version 7.4, the core Redis software would be relicensed under the RSAL and Server Side Public License (SSPL), both of which are source-available and non-free. The Linux Foundation subsequently announced that it would fork the last BSD-licensed version of Redis as Valkey. In May 2025, Redis Ltd. announced that it would change the license again to the AGPL beginning on version 8.0, citing that forks had achieved their goal of creating a "level playing field" of differentiated products, and that Redis has achieved "record growth" since the change in license.

Sanfilippo returned to Redis in December 2024.

Redis is a system that functions as both a data store and a cache. Data is modified and read from the main computer memory while also being persisted to disk in a format optimized for sequential access rather than random access. The formatted data is only reconstructed into memory once the system restarts.

Redis uses a data model that differs from relational database management system (RDBMS).

Commands specify operations on abstract data types rather than queries to be executed by a database engine. Data is stored in structures designed for direct retrieval. It does not rely on secondary indexes, aggregations, or other features common in traditional RDBMS. The Redis implementation uses the fork system call to duplicate the process holding the data. This allows the parent process to continue serving clients while the child process persists the in-memory data to disk.

Redis maps keys to types of values. Redis supports a number of data types including Strings, JavaScript Object Notation (JSON) documents, Hashes (a collection of fields, each field is a name-value string pair), lists, sets, vector sets, and more.

The Redis Query Engine allows users to use Redis as a document database, a vector database, a secondary index, and a search engine. With Redis Query Engine, users can define indexes for hash and JSON documents, and use a rich query language for vector search, full-text search, geospatial queries, and aggregations.

Redis Pub/Sub (short for publish/subscribe) is a lightweight messaging capability. Publishers send messages to a channel, and subscribers receive messages from that channel.

A Redis transaction allows the execution of a group of commands in a single step. A request sent by another client will never be served during the execution of a transaction. This guarantees that the commands are executed as a single isolated operation.

Redis users can also upload and execute Lua scripts on the server.

As of May 1, 2025, for all version of Redis starting with 8.0, all data types are included in the same package and available under the Redis Source Available License v2. Previously some data types were separate and therefore available under difference licenses.

Source: https://en.wikipedia.org/wiki/Redis (Wikipedia, CC BY-SA 4.0)
