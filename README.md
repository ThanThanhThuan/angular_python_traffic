## Traffic & Mobility Insights

🚦 Project: Traffic & Mobility Insights

A full-stack application for visualizing urban road networks, analyzing historical congestion, and predicting commute times using Machine Learning. The system treats the city as a graph network to optimize routing and insights.

🏗 Architecture

    Frontend: Angular (Standalone Components) + Leaflet.js (Map rendering).

    Backend: Python Flask (REST API) + Scikit-Learn (Traffic Prediction).

    Database: Neo4j (Graph Database) - Stores Intersections (Nodes) and Roads (Relationships).

    External Data: OpenStreetMap (Tiles) + TransportAPI (Live Data).

🚀 How to Run the Project
1. Start the Database (Neo4j)

    Open Neo4j Desktop. (Or browser, with Neo4j in Docker)

    Start the database (ensure port is 7687).

    Run the Cypher Seed Data (Create nodes/relationships) in the Neo4j Browser.

2. Start the Backend
cd backend
- (Optional) source venv/bin/activate
python app.py
- Verify it is running at http://localhost:5000
3. Start the Frontend
cd frontend
ng serve
- Wait for "Local: http://localhost:4200/"
<img width="1383" height="887" alt="image" src="https://github.com/user-attachments/assets/16b71fa7-bc36-4561-b74b-9539492cf634" />


  

4. View the App

    Open your browser manually to http://localhost:4200.
