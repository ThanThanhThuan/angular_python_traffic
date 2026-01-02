from neo4j import GraphDatabase

class GraphDB:
    def __init__(self):
        # Update URI and Auth based on your Neo4j settings
        # Use 'bolt://' and port 7687
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "YourVeryLongPassword123!"))

    def close(self):
        self.driver.close()

    def get_road_network(self):
        query = """
        MATCH (n:Intersection)-[r:ROAD]->(m:Intersection)
        RETURN n.lat AS lat1, n.lon AS lon1, m.lat AS lat2, m.lon AS lon2, r.avg_speed_kmh AS speed
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]

db = GraphDB()