# UI for perusasion project
To run locally in docker, runt he following command:
```
docker run  --mount src=`pwd`,target=/local_data,type=bind -p 5050:8080 streamlit_app
```