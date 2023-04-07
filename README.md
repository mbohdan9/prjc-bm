# train model
Open terminal in model folder, where train_model.sh located.
Run 
`bash train_model.sh`
to generate a new serialized model file
"text_complexity_model.joblib"

# run fast api for model inference

Open terminal in project root folder, where Dockerfile is located.
Build and run docker image with model to use text complexity prediction:

`docker build -t mymodelapi .`

`docker run -v $PWD/model:/model --name mymodelapicont -p 80:80 mymodelapi`

Open http://localhost/docs for documentation
Use POST http://localhost/predict for predicting text complexity

Body example:
{
    "excerpt": "Here is test string for simple text"
}

Response example:
{
    "target": -0.48087047917320835
}

# serialized model file and metrics
https://drive.google.com/drive/folders/1SR5Qh_zJFo5MgfJJIOBUwuiyRRSypJDd?usp=share_link
(file put into model folder)
