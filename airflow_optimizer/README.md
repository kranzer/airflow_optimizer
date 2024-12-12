
# Airflow Task Optimizer

This service optimizes the selection of Snowflake warehouses for Airflow tasks based on execution statistics. It uses historical task data to determine the most cost-effective warehouse size that meets performance goals.

---

## Features
- Cleans and validates input data to remove corrupted or irrelevant records.
- Aggregates duplicate task IDs for accurate performance analysis.
- Automatically assigns the most suitable Snowflake warehouse for each task.

---

## Requirements
- **Python 3.8 or later**
- **Docker** (optional, for containerized deployment)

---

## Installation
### Step 1: Clone the Repository
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd airflow_task_optimizer
   ```

### Step 2: Install Dependencies
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
### Run Locally
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Use an HTTP client (e.g., Postman, `curl`) to send a POST request to the service:
   ```bash
   curl -X POST http://localhost:5555/optimize-warehouse \
        -H "Content-Type: application/json" \
        -d '[{"TASK_ID": "task1", "DURATION": 25, "NUMBER_OF_CAMPAIGNS": 120}]'
   ```

3. Example response:
   ```json
   {
       "task1": "X-Large"
   }
   ```

---

### Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t airflow-task-optimizer .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5555:5555 airflow-task-optimizer
   ```

3. Use the same `curl` or HTTP client requests as described in the "Run Locally" section.

---

## Testing
Run unit tests to verify the service:
```bash
pytest tests/
```

---

## Input Format
The service accepts a list of task execution statistics as JSON, with the following structure:
```json
[
    {
        "TASK_ID": "task1",
        "DURATION": 25,
        "NUMBER_OF_CAMPAIGNS": 120
    },
    {
        "TASK_ID": "task2",
        "DURATION": 15,
        "NUMBER_OF_CAMPAIGNS": 50
    }
]
```

- **TASK_ID**: Unique identifier for the task (string, required).
- **DURATION**: Execution duration in seconds (positive number, required).
- **NUMBER_OF_CAMPAIGNS**: Number of campaigns processed by the task (number, optional).

---

## Output Format
The service returns a JSON object mapping each `TASK_ID` to a warehouse size:
```json
{
    "task1": "X-Large",
    "task2": "Medium"
}
```

---

## Deployment
For cloud deployment, use the `Dockerfile` and deployment scripts to deploy on platforms like AWS, GCP, or Heroku.

---

## License
This project is licensed under the MIT License.
