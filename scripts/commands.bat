REM --commands for docker--
REM docker build --pull --no-cache -t hostile-tweets-ex:latest .
REM docker login
REM docker tag hostile-tweets-ex:latest docker.io/0533orel/hostile-tweets-ex:latest
REM docker push docker.io/0533orel/hostile-tweets-ex:latest

REM --for test run in bash--
REM ==============================================================================
REM docker run -p 8000:8000 \
REM   -e MONGO_URI="mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/" \
REM   -e MONGO_DB="IranMalDB" \
REM   -e MONGO_COLLECTION="tweets" \
REM   hostile-tweets-ex:latest
REM ==============================================================================
REM --for check--
REM curl http://localhost:8000/health
REM curl http://localhost:8000/get_data_processed

cd C:\PyCharm\hostile_tweets_ex

REM --commands for openshift---
REM oc login etc.
REM --- CLEANUP---
oc delete all --all
oc delete pvc --all
oc delete configmap --all
oc delete secret --all


REM --- CREATE ---
oc apply -f infra\secrets.yaml
oc apply -f infra\configmap.yaml
oc apply -f infra\deployment.yaml
oc apply -f infra\service.yaml
oc apply -f infra\route.yaml

REM --- STATUS ---
oc rollout status deployment/hostile-tweets
oc get route hostile-tweets-route

pause

