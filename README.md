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

3. Build and run the container using a different port (e.g., 8889):

    ```sh
    docker run -p 8889:8888 my-jupyter-notebook
    ```

4. Access Jupyter Notebook at:

    ```
    http://localhost:8889/?token=your_token_here
    ```

## Docker Image
You can pull the Docker image from Docker Hub:

```sh
docker pull your-dockerhub-username/my-jupyter-notebook
