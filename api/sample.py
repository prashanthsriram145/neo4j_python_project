from flask import Flask
from neo4j import GraphDatabase

with GraphDatabase.driver(
    "bolt://localhost:7687", 
    auth=("new_neo4j", "neo4j@145")
    ) as driver:
        driver.verify_connectivity()
        with driver.session() as session:
            query = """
                match (m:Movie) return m
            """
            moviesList = session.run(query)
            for movie in moviesList:
                print(movie)