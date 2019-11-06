# project variables
GCP_PROJECT_ID=parrot-256516

.PHONY: deploy
deploy:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/parrot/backend . && \
	gcloud beta run deploy parrot-api --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/parrot/backend \
	--platform managed --region us-central1 --allow-unauthenticated
