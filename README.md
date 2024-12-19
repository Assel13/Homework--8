# My Jupyter Notebook Docker Project

## How to Run

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/my-docker-jupyter-project.git
    ```

2. Navigate to the project directory:

    ```sh
    cd my-docker-jupyter-project
    ```

3. Build and run the container using Docker Compose:

    ```sh
    docker-compose up -d
    ```

4. Access Jupyter Notebook at:

    ```
    http://localhost:8888/?token=your_token_here
    ```

## Note
- The `docker-compose.yml` file ensures that the URL remains the same and the container restarts automatically.
