REM --commands for docker--
REM docker build -t hostile-tweets-ex:latest .
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


