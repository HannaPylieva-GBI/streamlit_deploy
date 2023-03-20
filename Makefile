.PHONY: run run-container gcloud-deploy

run:
	@streamlit run app.py --server.port=5050 --server.address=0.0.0.0

run-container:
	@docker build . -t streamlit_app
	@docker run -p 5050:8080 streamlit_app

gcloud-deploy:
	@gcloud app deploy app.yaml
